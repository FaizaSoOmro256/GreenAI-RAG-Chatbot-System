"""
Monitoring utility for tracking application performance metrics.
This module provides functions for recording, analyzing, and displaying 
performance metrics for the GreenAI application.
"""

import time
import datetime
import threading
import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from collections import deque, defaultdict
import random
import shutil
import glob
import zipfile

# Constants
METRICS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "metrics")
os.makedirs(METRICS_DIR, exist_ok=True)
METRICS_FILE = os.path.join(METRICS_DIR, "performance_metrics.json")
BACKUP_DIR = os.path.join(METRICS_DIR, "backups")
os.makedirs(BACKUP_DIR, exist_ok=True)
MAX_HISTORY_SIZE = 1000  # Maximum number of metrics to keep in memory
MAX_BACKUPS = 10  # Maximum number of backup files to keep
MAX_METRICS_AGE_DAYS = 30  # Only keep metrics from the last 30 days
AUTO_TRIM_FREQUENCY = 0.2  # 20% chance to auto-trim on each save operation

# Thread-safe storage for metrics
class MetricsStore:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(MetricsStore, cls).__new__(cls)
                cls._instance._init()
            return cls._instance
    
    def _init(self):
        """Initialize the metrics store."""
        self.metrics = {
            "response_times": deque(maxlen=MAX_HISTORY_SIZE),
            "embedding_times": deque(maxlen=MAX_HISTORY_SIZE),
            "token_counts": deque(maxlen=MAX_HISTORY_SIZE),
            "cache_stats": deque(maxlen=MAX_HISTORY_SIZE),
            "error_counts": defaultdict(int),
            "query_counts_by_language": defaultdict(int),
            "query_counts_by_hour": defaultdict(int)
        }
        self.load_metrics()
    
    def record_response_time(self, query_type, duration_ms, timestamp=None):
        """Record a response time metric."""
        if timestamp is None:
            timestamp = datetime.datetime.now().isoformat()
        
        with self._lock:
            self.metrics["response_times"].append({
                "timestamp": timestamp,
                "type": query_type,
                "duration_ms": duration_ms
            })
    
    def record_embedding_time(self, num_texts, duration_ms, timestamp=None):
        """Record embedding generation time metric."""
        if timestamp is None:
            timestamp = datetime.datetime.now().isoformat()
        
        with self._lock:
            self.metrics["embedding_times"].append({
                "timestamp": timestamp,
                "num_texts": num_texts,
                "duration_ms": duration_ms
            })
    
    def record_token_count(self, input_tokens, output_tokens, timestamp=None):
        """Record token count metrics."""
        if timestamp is None:
            timestamp = datetime.datetime.now().isoformat()
        
        with self._lock:
            self.metrics["token_counts"].append({
                "timestamp": timestamp,
                "input_tokens": input_tokens,
                "output_tokens": output_tokens
            })
    
    def record_cache_stats(self, hits, misses, timestamp=None):
        """Record cache performance stats."""
        if timestamp is None:
            timestamp = datetime.datetime.now().isoformat()
        
        with self._lock:
            self.metrics["cache_stats"].append({
                "timestamp": timestamp,
                "hits": hits,
                "misses": misses
            })
    
    def record_error(self, error_type):
        """Record an error occurrence."""
        with self._lock:
            self.metrics["error_counts"][error_type] += 1
    
    def record_query(self, language, timestamp=None):
        """Record a query by language."""
        if timestamp is None:
            now = datetime.datetime.now()
            timestamp = now
            hour = now.hour
        else:
            if isinstance(timestamp, str):
                timestamp = datetime.datetime.fromisoformat(timestamp)
            hour = timestamp.hour
        
        with self._lock:
            self.metrics["query_counts_by_language"][language] += 1
            self.metrics["query_counts_by_hour"][hour] += 1
    
    def get_avg_response_time(self, last_n=None, query_type=None):
        """Get average response time, optionally filtered."""
        with self._lock:
            times = list(self.metrics["response_times"])
            
            if query_type:
                times = [t for t in times if t["type"] == query_type]
            
            if last_n and last_n < len(times):
                times = times[-last_n:]
            
            if not times:
                return 0
            
            return sum(t["duration_ms"] for t in times) / len(times)
    
    def get_cache_hit_rate(self, last_n=None):
        """Get cache hit rate as a percentage."""
        with self._lock:
            stats = list(self.metrics["cache_stats"])
            
            if last_n and last_n < len(stats):
                stats = stats[-last_n:]
            
            if not stats:
                return 0
            
            total_hits = sum(s["hits"] for s in stats)
            total_misses = sum(s["misses"] for s in stats)
            total = total_hits + total_misses
            
            return (total_hits / total) * 100 if total > 0 else 0
    
    def get_error_distribution(self):
        """Get distribution of errors by type."""
        with self._lock:
            return dict(self.metrics["error_counts"])
    
    def get_query_distribution_by_language(self):
        """Get distribution of queries by language."""
        with self._lock:
            return dict(self.metrics["query_counts_by_language"])
    
    def get_query_distribution_by_hour(self):
        """Get distribution of queries by hour of day."""
        with self._lock:
            return dict(self.metrics["query_counts_by_hour"])
    
    def save_metrics(self):
        """Save metrics to disk."""
        try:
            with self._lock:
                # Auto-trim old metrics periodically
                if random.random() < AUTO_TRIM_FREQUENCY:
                    trim_result = self.trim_old_metrics()
                    if trim_result["success"] and any(trim_result["removed"].values()):
                        print(f"Auto-trimmed metrics older than {trim_result['cutoff_date']}: {trim_result['removed']}")
                
                # Convert deques to lists for serialization
                serializable_metrics = {
                    "response_times": list(self.metrics["response_times"]),
                    "embedding_times": list(self.metrics["embedding_times"]),
                    "token_counts": list(self.metrics["token_counts"]),
                    "cache_stats": list(self.metrics["cache_stats"]),
                    "error_counts": dict(self.metrics["error_counts"]),
                    "query_counts_by_language": dict(self.metrics["query_counts_by_language"]),
                    "query_counts_by_hour": dict(self.metrics["query_counts_by_hour"])
                }
                
                with open(METRICS_FILE, 'w') as f:
                    json.dump(serializable_metrics, f)
                
                # Create a backup periodically (10% chance each save)
                if random.random() < 0.1:
                    self.create_backup()
                    
        except Exception as e:
            print(f"Error saving metrics: {str(e)}")
    
    def create_backup(self, backup_name=None):
        """Create a backup of the current metrics data."""
        try:
            with self._lock:
                # Generate backup filename based on current timestamp
                if backup_name is None:
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    backup_name = f"metrics_backup_{timestamp}.json"
                
                backup_path = os.path.join(BACKUP_DIR, backup_name)
                
                # Convert deques to lists for serialization
                serializable_metrics = {
                    "response_times": list(self.metrics["response_times"]),
                    "embedding_times": list(self.metrics["embedding_times"]),
                    "token_counts": list(self.metrics["token_counts"]),
                    "cache_stats": list(self.metrics["cache_stats"]),
                    "error_counts": dict(self.metrics["error_counts"]),
                    "query_counts_by_language": dict(self.metrics["query_counts_by_language"]),
                    "query_counts_by_hour": dict(self.metrics["query_counts_by_hour"]),
                    "backup_timestamp": datetime.datetime.now().isoformat(),
                    "backup_info": "Automatically created backup"
                }
                
                with open(backup_path, 'w') as f:
                    json.dump(serializable_metrics, f)
                
                # Clean up old backups if we exceed the maximum
                self._cleanup_old_backups()
                
                return {"success": True, "backup_path": backup_path}
        
        except Exception as e:
            print(f"Error creating backup: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def restore_from_backup(self, backup_file):
        """Restore metrics from a backup file."""
        try:
            backup_path = os.path.join(BACKUP_DIR, backup_file)
            
            # Make sure the backup file exists
            if not os.path.exists(backup_path):
                return {"success": False, "error": f"Backup file {backup_file} not found"}
            
            # Create a backup of the current state before restoring
            current_timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            pre_restore_backup = f"pre_restore_backup_{current_timestamp}.json"
            self.create_backup(pre_restore_backup)
            
            # Load the backup data
            with open(backup_path, 'r') as f:
                loaded_metrics = json.load(f)
                
                with self._lock:
                    # Convert lists back to deques with size limit
                    self.metrics["response_times"] = deque(
                        loaded_metrics.get("response_times", []),
                        maxlen=MAX_HISTORY_SIZE
                    )
                    self.metrics["embedding_times"] = deque(
                        loaded_metrics.get("embedding_times", []),
                        maxlen=MAX_HISTORY_SIZE
                    )
                    self.metrics["token_counts"] = deque(
                        loaded_metrics.get("token_counts", []),
                        maxlen=MAX_HISTORY_SIZE
                    )
                    self.metrics["cache_stats"] = deque(
                        loaded_metrics.get("cache_stats", []),
                        maxlen=MAX_HISTORY_SIZE
                    )
                    self.metrics["error_counts"] = defaultdict(
                        int, loaded_metrics.get("error_counts", {})
                    )
                    self.metrics["query_counts_by_language"] = defaultdict(
                        int, loaded_metrics.get("query_counts_by_language", {})
                    )
                    self.metrics["query_counts_by_hour"] = defaultdict(
                        int, loaded_metrics.get("query_counts_by_hour", {})
                    )
            
            # Save the restored metrics to the main file
            self.save_metrics()
            
            return {
                "success": True,
                "backup_date": loaded_metrics.get("backup_timestamp", "Unknown date"),
                "pre_restore_backup": pre_restore_backup
            }
        
        except Exception as e:
            print(f"Error restoring from backup: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def _cleanup_old_backups(self):
        """Remove old backups if we exceed the maximum number."""
        try:
            # Get all backup files
            backup_files = glob.glob(os.path.join(BACKUP_DIR, "metrics_backup_*.json"))
            
            # Sort by modification time (oldest first)
            backup_files.sort(key=os.path.getmtime)
            
            # Remove oldest files if we have too many
            if len(backup_files) > MAX_BACKUPS:
                files_to_remove = backup_files[:(len(backup_files) - MAX_BACKUPS)]
                for file_path in files_to_remove:
                    os.remove(file_path)
                    print(f"Removed old backup: {os.path.basename(file_path)}")
        
        except Exception as e:
            print(f"Error cleaning up old backups: {str(e)}")
    
    def export_metrics_zip(self):
        """Export all metrics and backups as a zip file."""
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            zip_filename = f"metrics_export_{timestamp}.zip"
            zip_path = os.path.join(METRICS_DIR, zip_filename)
            
            # Save current metrics before exporting
            self.save_metrics()
            
            # Create a zip file
            with zipfile.ZipFile(zip_path, 'w') as zipf:
                # Add the main metrics file
                if os.path.exists(METRICS_FILE):
                    zipf.write(METRICS_FILE, arcname=os.path.basename(METRICS_FILE))
                
                # Add all backup files
                for backup_file in glob.glob(os.path.join(BACKUP_DIR, "*.json")):
                    arcname = os.path.join("backups", os.path.basename(backup_file))
                    zipf.write(backup_file, arcname=arcname)
            
            return {"success": True, "zip_path": zip_path, "filename": zip_filename}
        
        except Exception as e:
            print(f"Error exporting metrics: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def load_metrics(self):
        """Load metrics from disk if available."""
        if not os.path.exists(METRICS_FILE):
            return
        
        try:
            with open(METRICS_FILE, 'r') as f:
                loaded_metrics = json.load(f)
                
                with self._lock:
                    # Convert lists back to deques with size limit
                    self.metrics["response_times"] = deque(
                        loaded_metrics.get("response_times", []),
                        maxlen=MAX_HISTORY_SIZE
                    )
                    self.metrics["embedding_times"] = deque(
                        loaded_metrics.get("embedding_times", []),
                        maxlen=MAX_HISTORY_SIZE
                    )
                    self.metrics["token_counts"] = deque(
                        loaded_metrics.get("token_counts", []),
                        maxlen=MAX_HISTORY_SIZE
                    )
                    self.metrics["cache_stats"] = deque(
                        loaded_metrics.get("cache_stats", []),
                        maxlen=MAX_HISTORY_SIZE
                    )
                    self.metrics["error_counts"] = defaultdict(
                        int, loaded_metrics.get("error_counts", {})
                    )
                    self.metrics["query_counts_by_language"] = defaultdict(
                        int, loaded_metrics.get("query_counts_by_language", {})
                    )
                    self.metrics["query_counts_by_hour"] = defaultdict(
                        int, loaded_metrics.get("query_counts_by_hour", {})
                    )
        except Exception as e:
            print(f"Error loading metrics: {str(e)}")
    
    def trim_old_metrics(self, days=MAX_METRICS_AGE_DAYS):
        """Remove metrics older than the specified number of days."""
        try:
            with self._lock:
                # Calculate the cutoff timestamp
                cutoff_date = datetime.datetime.now() - datetime.timedelta(days=days)
                cutoff_timestamp = cutoff_date.isoformat()
                
                # Keep track of how many records are removed
                removed_counts = {
                    "response_times": 0,
                    "embedding_times": 0,
                    "token_counts": 0,
                    "cache_stats": 0
                }
                
                # Filter response times
                new_response_times = deque(maxlen=MAX_HISTORY_SIZE)
                for item in self.metrics["response_times"]:
                    if item["timestamp"] >= cutoff_timestamp:
                        new_response_times.append(item)
                    else:
                        removed_counts["response_times"] += 1
                self.metrics["response_times"] = new_response_times
                
                # Filter embedding times
                new_embedding_times = deque(maxlen=MAX_HISTORY_SIZE)
                for item in self.metrics["embedding_times"]:
                    if item["timestamp"] >= cutoff_timestamp:
                        new_embedding_times.append(item)
                    else:
                        removed_counts["embedding_times"] += 1
                self.metrics["embedding_times"] = new_embedding_times
                
                # Filter token counts
                new_token_counts = deque(maxlen=MAX_HISTORY_SIZE)
                for item in self.metrics["token_counts"]:
                    if item["timestamp"] >= cutoff_timestamp:
                        new_token_counts.append(item)
                    else:
                        removed_counts["token_counts"] += 1
                self.metrics["token_counts"] = new_token_counts
                
                # Filter cache stats
                new_cache_stats = deque(maxlen=MAX_HISTORY_SIZE)
                for item in self.metrics["cache_stats"]:
                    if item["timestamp"] >= cutoff_timestamp:
                        new_cache_stats.append(item)
                    else:
                        removed_counts["cache_stats"] += 1
                self.metrics["cache_stats"] = new_cache_stats
                
                # We don't trim the counts like error_counts, they're cumulative
                
                return {
                    "success": True,
                    "removed": removed_counts,
                    "cutoff_date": cutoff_date.strftime("%Y-%m-%d")
                }
                
        except Exception as e:
            print(f"Error trimming old metrics: {str(e)}")
            return {"success": False, "error": str(e)}

# Global instance
metrics_store = MetricsStore()

# Timer context manager for easy measurement
class Timer:
    def __init__(self, metric_type=None, **kwargs):
        self.start_time = None
        self.metric_type = metric_type
        self.kwargs = kwargs
    
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        duration_ms = (time.time() - self.start_time) * 1000
        
        if self.metric_type == "response":
            metrics_store.record_response_time(
                self.kwargs.get("query_type", "general"),
                duration_ms
            )
        elif self.metric_type == "embedding":
            metrics_store.record_embedding_time(
                self.kwargs.get("num_texts", 1),
                duration_ms
            )
        
        # Automatically save metrics periodically
        if random.random() < 0.1:  # ~10% chance to save on each measurement
            metrics_store.save_metrics()
        
        return False  # Don't suppress exceptions

# Streamlit dashboard for monitoring
def render_monitoring_dashboard():
    """Render a monitoring dashboard in Streamlit."""
    st.title("Green AI Performance Monitoring")
    
    # Create tabs for different sections
    main_tabs = st.tabs(["Performance Metrics", "Backup & Restore", "Export", "Data Management"])
    
    with main_tabs[0]:
        # Overview metrics
        st.header("Overview")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            avg_response = metrics_store.get_avg_response_time(last_n=100)
            st.metric("Avg Response Time (last 100)", f"{avg_response:.2f} ms")
        
        with col2:
            cache_hit_rate = metrics_store.get_cache_hit_rate()
            st.metric("Cache Hit Rate", f"{cache_hit_rate:.1f}%")
        
        with col3:
            query_count = sum(metrics_store.get_query_distribution_by_language().values())
            st.metric("Total Queries", query_count)
        
        # Response time trend
        st.header("Response Time Trend")
        
        # Convert deque to dataframe for plotting
        response_times = list(metrics_store.metrics["response_times"])
        if response_times:
            df = pd.DataFrame(response_times)
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df = df.set_index('timestamp')
            
            # Resample by hour and calculate mean
            hourly_avg = df.resample('H')['duration_ms'].mean()
            
            # Create the plot
            fig, ax = plt.subplots(figsize=(10, 5))
            hourly_avg.plot(ax=ax)
            ax.set_ylabel('Response Time (ms)')
            ax.set_title('Average Response Time by Hour')
            st.pyplot(fig)
        else:
            st.info("No response time data available yet.")
        
        # Language distribution
        st.header("Query Distribution by Language")
        lang_dist = metrics_store.get_query_distribution_by_language()
        
        if lang_dist:
            fig, ax = plt.subplots(figsize=(8, 8))
            ax.pie(
                lang_dist.values(),
                labels=lang_dist.keys(),
                autopct='%1.1f%%',
                startangle=90
            )
            ax.axis('equal')
            st.pyplot(fig)
        else:
            st.info("No language distribution data available yet.")
        
        # Query distribution by hour
        st.header("Query Distribution by Hour of Day")
        hour_dist = metrics_store.get_query_distribution_by_hour()
        
        if hour_dist:
            # Ensure all hours are represented (0-23)
            hours = {str(h): hour_dist.get(str(h), 0) for h in range(24)}
            
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.bar(hours.keys(), hours.values())
            ax.set_xlabel('Hour of Day')
            ax.set_ylabel('Number of Queries')
            ax.set_title('Query Distribution by Hour')
            st.pyplot(fig)
        else:
            st.info("No hourly distribution data available yet.")
        
        # Error distribution
        st.header("Error Distribution")
        error_dist = metrics_store.get_error_distribution()
        
        if error_dist:
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.bar(error_dist.keys(), error_dist.values())
            ax.set_xlabel('Error Type')
            ax.set_ylabel('Count')
            ax.set_title('Error Distribution')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            st.pyplot(fig)
        else:
            st.info("No error data available yet.")
        
        # Save button
        if st.button("Save Metrics to Disk", key="save_metrics_btn"):
            metrics_store.save_metrics()
            st.success("Metrics saved successfully!")
    
    with main_tabs[1]:
        st.header("Backup & Restore")
        
        # Create backup section
        st.subheader("Create Backup")
        backup_col1, backup_col2 = st.columns([3, 1])
        
        with backup_col1:
            st.markdown("Create a backup of current metrics data. Backups can be used to restore data if needed.")
        
        with backup_col2:
            if st.button("Create Backup", key="create_backup_btn", use_container_width=True):
                result = metrics_store.create_backup()
                if result["success"]:
                    st.success(f"Backup created successfully at {os.path.basename(result['backup_path'])}")
                else:
                    st.error(f"Failed to create backup: {result.get('error', 'Unknown error')}")
        
        # List available backups
        st.subheader("Available Backups")
        
        # Get all backup files
        backup_files = glob.glob(os.path.join(BACKUP_DIR, "*.json"))
        
        if not backup_files:
            st.info("No backups available yet.")
        else:
            # Sort by modification time (newest first)
            backup_files.sort(key=os.path.getmtime, reverse=True)
            
            # Create a dataframe with backup info
            backup_info = []
            for backup_path in backup_files:
                filename = os.path.basename(backup_path)
                mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(backup_path))
                size = os.path.getsize(backup_path) / 1024  # Size in KB
                
                # Try to extract backup timestamp from the file
                timestamp = "Unknown"
                try:
                    with open(backup_path, 'r') as f:
                        data = json.load(f)
                        if "backup_timestamp" in data:
                            timestamp = data["backup_timestamp"]
                except:
                    pass
                
                backup_info.append({
                    "Filename": filename,
                    "Creation Date": mod_time.strftime("%Y-%m-%d %H:%M:%S"),
                    "Size (KB)": f"{size:.2f}",
                    "Backup Timestamp": timestamp
                })
            
            backup_df = pd.DataFrame(backup_info)
            st.dataframe(backup_df, use_container_width=True)
            
            # Restore from backup
            st.subheader("Restore from Backup")
            
            # Select backup file
            selected_backup = st.selectbox(
                "Select a backup to restore",
                options=[info["Filename"] for info in backup_info],
                index=0
            )
            
            restore_col1, restore_col2 = st.columns([3, 1])
            
            with restore_col1:
                st.markdown(f"This will restore metrics data from backup file: **{selected_backup}**")
                st.warning("This will overwrite current metrics data. A backup of current data will be created before restoration.")
            
            with restore_col2:
                if st.button("Restore", key="restore_backup_btn", use_container_width=True, type="primary"):
                    # Confirm before restoring
                    result = metrics_store.restore_from_backup(selected_backup)
                    
                    if result["success"]:
                        st.success(f"Successfully restored from backup. Current data backed up as {result['pre_restore_backup']}")
                    else:
                        st.error(f"Failed to restore from backup: {result.get('error', 'Unknown error')}")
    
    with main_tabs[2]:
        st.header("Export Metrics")
        
        # Export options
        st.subheader("Export Options")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown("Export all metrics data and backups as a ZIP file. This is useful for transferring data between instances or for offline analysis.")
        
        with col2:
            if st.button("Export as ZIP", key="export_zip_btn", use_container_width=True):
                with st.spinner("Creating export ZIP file..."):
                    result = metrics_store.export_metrics_zip()
                    
                    if result["success"]:
                        # Provide download button for the ZIP file
                        with open(result["zip_path"], "rb") as f:
                            st.download_button(
                                label="Download ZIP",
                                data=f,
                                file_name=result["filename"],
                                mime="application/zip",
                                key="download_zip_btn"
                            )
                        st.success(f"Export created successfully: {result['filename']}")
                    else:
                        st.error(f"Failed to create export: {result.get('error', 'Unknown error')}")

    with main_tabs[3]:
        st.header("Data Management")
        
        # Metrics info section
        st.subheader("Metrics Data Info")
        
        # Calculate metrics data size
        response_times_count = len(metrics_store.metrics["response_times"])
        embedding_times_count = len(metrics_store.metrics["embedding_times"])
        token_counts_count = len(metrics_store.metrics["token_counts"])
        cache_stats_count = len(metrics_store.metrics["cache_stats"])
        
        # Display stats in a table
        data_info = {
            "Metric Type": ["Response Times", "Embedding Times", "Token Counts", "Cache Stats", "Total"],
            "Records": [
                response_times_count,
                embedding_times_count,
                token_counts_count,
                cache_stats_count,
                response_times_count + embedding_times_count + token_counts_count + cache_stats_count
            ]
        }
        
        st.dataframe(pd.DataFrame(data_info), use_container_width=True)
        
        # Metrics trimming section
        st.subheader("Trim Old Metrics")
        st.markdown("Remove metrics data older than a specified number of days to conserve storage space.")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            # Age selector
            days_to_keep = st.slider(
                "Keep data from the last N days:",
                min_value=7,
                max_value=365,
                value=MAX_METRICS_AGE_DAYS,
                step=1
            )
            
        with col2:
            trim_button = st.button(
                "Trim Old Data",
                key="trim_old_data_btn",
                use_container_width=True,
                type="primary"
            )
        
        if trim_button:
            with st.spinner(f"Trimming data older than {days_to_keep} days..."):
                # Create a backup before trimming
                backup_result = metrics_store.create_backup()
                
                if backup_result["success"]:
                    # Perform the trimming
                    trim_result = metrics_store.trim_old_metrics(days=days_to_keep)
                    
                    if trim_result["success"]:
                        # Calculate total removed
                        total_removed = sum(trim_result["removed"].values())
                        
                        if total_removed > 0:
                            st.success(f"Successfully removed {total_removed} records older than {trim_result['cutoff_date']}.")
                            
                            # Display detailed results
                            st.markdown("### Removed Records by Type")
                            trim_details = {
                                "Metric Type": list(trim_result["removed"].keys()),
                                "Records Removed": list(trim_result["removed"].values())
                            }
                            st.dataframe(pd.DataFrame(trim_details), use_container_width=True)
                            
                            # Save the trimmed data
                            metrics_store.save_metrics()
                            
                            # Prompt to refresh
                            st.info("Page will refresh to show updated metrics data.")
                            time.sleep(2)
                            st.rerun()
                        else:
                            st.info(f"No data found older than {trim_result['cutoff_date']}. Nothing to remove.")
                    else:
                        st.error(f"Error trimming data: {trim_result.get('error', 'Unknown error')}")
                else:
                    st.error(f"Error creating backup before trimming: {backup_result.get('error', 'Unknown error')}")
        
        # Auto-trim settings
        st.subheader("Auto-Trimming Settings")
        st.markdown("The system automatically trims old data based on these settings.")
        
        st.info(f"""
        Current settings:
        - Keep data for {MAX_METRICS_AGE_DAYS} days
        - {int(AUTO_TRIM_FREQUENCY * 100)}% chance to auto-trim on each save operation
        
        These settings can be adjusted by modifying the constants in the monitoring.py file.
        """)

# Make sure pandas and matplotlib are available
try:
    import pandas as pd
    import matplotlib.pyplot as plt
except ImportError:
    print("Warning: pandas or matplotlib not available. Monitoring dashboard will not work.")

# Example usage:
# with Timer(metric_type="response", query_type="weather"):
#     # do some work that takes time
#     time.sleep(1)
#
# with Timer(metric_type="embedding", num_texts=5):
#     # generate embeddings
#     time.sleep(0.5)
#
# # Record other metrics
# metrics_store.record_token_count(input_tokens=150, output_tokens=50)
# metrics_store.record_cache_stats(hits=5, misses=2)
# metrics_store.record_error("API_TIMEOUT")
# metrics_store.record_query("english")
#
# # Save metrics to disk
# metrics_store.save_metrics() 
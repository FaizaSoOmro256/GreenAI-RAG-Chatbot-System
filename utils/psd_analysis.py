"""
Power Spectral Density (PSD) analysis module for climate data.
Provides functions to analyze climate patterns using frequency domain analysis.
"""

import numpy as np
from scipy import signal
import pandas as pd
from typing import Dict, List, Tuple, Union, Optional

def calculate_psd(data: np.ndarray, 
                 sampling_rate: float = 1.0, 
                 nperseg: Optional[int] = None,
                 noverlap: Optional[int] = None) -> Tuple[np.ndarray, np.ndarray]:
    """
    Calculate Power Spectral Density (PSD) for a time series.
    
    Args:
        data: Time series data
        sampling_rate: Sampling rate in Hz (default: 1.0)
        nperseg: Length of each segment (default: None, will use N/8)
        noverlap: Number of points to overlap between segments (default: None, will use nperseg//2)
        
    Returns:
        Tuple of (frequencies, power spectral density)
    """
    try:
        # Remove any NaN values
        data = data[~np.isnan(data)]
        
        # Calculate PSD using Welch's method
        frequencies, psd = signal.welch(data, 
                                       fs=sampling_rate,
                                       nperseg=nperseg,
                                       noverlap=noverlap)
        
        return frequencies, psd
    except Exception as e:
        return np.array([]), np.array([])

def analyze_climate_cycles(data: Dict[str, List[float]], 
                          sampling_rate: float = 1.0) -> Dict[str, Dict[str, float]]:
    """
    Analyze climate cycles in time series data.
    
    Args:
        data: Dictionary with climate variables as keys and time series as values
        sampling_rate: Sampling rate in Hz (default: 1.0)
        
    Returns:
        Dictionary with dominant frequencies and their powers for each variable
    """
    results = {}
    
    for variable, time_series in data.items():
        try:
            # Convert to numpy array
            series = np.array(time_series)
            
            # Calculate PSD
            frequencies, psd = calculate_psd(series, sampling_rate)
            
            if len(frequencies) > 0 and len(psd) > 0:
                # Find dominant frequencies (peaks)
                peak_indices, _ = signal.find_peaks(psd, height=np.max(psd)*0.1)
                
                if len(peak_indices) > 0:
                    # Sort peaks by power
                    peak_powers = psd[peak_indices]
                    sorted_indices = np.argsort(peak_powers)[::-1]
                    
                    # Get top 3 dominant frequencies
                    dominant_freqs = frequencies[peak_indices[sorted_indices[:3]]]
                    dominant_powers = peak_powers[sorted_indices[:3]]
                    
                    # Calculate periods (in days if sampling_rate is 1/day)
                    periods = 1 / dominant_freqs
                    
                    results[variable] = {
                        'frequencies': dominant_freqs.tolist(),
                        'periods': periods.tolist(),
                        'powers': dominant_powers.tolist()
                    }
                else:
                    results[variable] = {
                        'frequencies': [],
                        'periods': [],
                        'powers': []
                    }
            else:
                results[variable] = {
                    'frequencies': [],
                    'periods': [],
                    'powers': []
                }
        except Exception as e:
            results[variable] = {
                'frequencies': [],
                'periods': [],
                'powers': []
            }
    
    return results

def detect_climate_anomalies(data: np.ndarray, 
                            window_size: int = 30,
                            threshold: float = 2.0) -> List[Dict[str, Union[int, float]]]:
    """
    Detect anomalies in climate time series using PSD analysis.
    
    Args:
        data: Time series data
        window_size: Size of the sliding window
        threshold: Standard deviations for anomaly detection
        
    Returns:
        List of dictionaries with anomaly information
    """
    anomalies = []
    
    try:
        # Remove any NaN values
        data = data[~np.isnan(data)]
        
        if len(data) < window_size:
            return anomalies
        
        # Calculate PSD for the entire series
        _, full_psd = calculate_psd(data)
        
        # Use sliding window to detect anomalies
        for i in range(len(data) - window_size + 1):
            window = data[i:i+window_size]
            _, window_psd = calculate_psd(window)
            
            if len(window_psd) > 0 and len(full_psd) > 0:
                # Compare window PSD to full series PSD
                if len(window_psd) < len(full_psd):
                    # Resample window_psd to match full_psd length
                    window_psd = signal.resample(window_psd, len(full_psd))
                
                # Calculate difference
                diff = np.abs(window_psd - full_psd)
                
                # Check if difference exceeds threshold
                if np.max(diff) > threshold * np.std(diff):
                    anomalies.append({
                        'start_index': i,
                        'end_index': i + window_size - 1,
                        'severity': float(np.max(diff) / np.std(diff))
                    })
    except Exception as e:
        pass
    
    return anomalies

def get_climate_psd_report(district: str, 
                          variable: str = 'temperature',
                          days: int = 365) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
    """
    Generate a PSD analysis report for a specific district and climate variable.
    
    Args:
        district: Name of the district
        variable: Climate variable to analyze (temperature, rainfall, etc.)
        days: Number of days of historical data to analyze
        
    Returns:
        Dictionary with PSD analysis results
    """
    try:
        # Import here to avoid circular imports
        from utils.real_time_data import get_district_climate_trend
        
        # Get historical data
        trend_data = get_district_climate_trend(district)
        
        if 'error' in trend_data:
            return {
                'status': 'error',
                'message': f"Could not retrieve data for {district}",
                'analysis': []
            }
        
        # Extract time series data
        if variable in trend_data and 'time_series' in trend_data[variable]:
            time_series = trend_data[variable]['time_series']
            
            # Convert to numpy array
            data = np.array(time_series)
            
            # Calculate PSD
            frequencies, psd = calculate_psd(data, sampling_rate=1/24)  # Assuming hourly data
            
            # Find dominant frequencies
            peak_indices, _ = signal.find_peaks(psd, height=np.max(psd)*0.1)
            
            if len(peak_indices) > 0:
                # Sort peaks by power
                peak_powers = psd[peak_indices]
                sorted_indices = np.argsort(peak_powers)[::-1]
                
                # Get top 5 dominant frequencies
                dominant_freqs = frequencies[peak_indices[sorted_indices[:5]]]
                dominant_powers = peak_powers[sorted_indices[:5]]
                
                # Calculate periods (in days)
                periods = 1 / dominant_freqs
                
                # Format results
                analysis = []
                for i in range(min(5, len(periods))):
                    period_days = periods[i]
                    
                    # Interpret the period
                    if period_days < 1:
                        interpretation = f"{int(period_days*24)} hours"
                    elif period_days < 7:
                        interpretation = f"{period_days:.1f} days"
                    elif period_days < 30:
                        interpretation = f"{period_days/7:.1f} weeks"
                    elif period_days < 365:
                        interpretation = f"{period_days/30:.1f} months"
                    else:
                        interpretation = f"{period_days/365:.1f} years"
                    
                    analysis.append({
                        'period': interpretation,
                        'frequency': f"{dominant_freqs[i]:.4f} cycles/day",
                        'power': f"{dominant_powers[i]:.4f}",
                        'significance': "High" if dominant_powers[i] > np.mean(psd) + 2*np.std(psd) else "Moderate"
                    })
                
                return {
                    'status': 'success',
                    'district': district,
                    'variable': variable,
                    'analysis': analysis
                }
            else:
                return {
                    'status': 'success',
                    'district': district,
                    'variable': variable,
                    'analysis': [{
                        'period': 'No significant cycles detected',
                        'frequency': 'N/A',
                        'power': 'N/A',
                        'significance': 'Low'
                    }]
                }
        else:
            return {
                'status': 'error',
                'message': f"No time series data available for {variable} in {district}",
                'analysis': []
            }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e),
            'analysis': []
        } 
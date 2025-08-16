import json
import os
from typing import Dict, List, Any, Optional
import requests
from datetime import datetime
import logging
import numpy as np
from scipy import stats

class DataIntegrator:
    def __init__(self, config_path: str = "data/chatbot/data_integration.json"):
        self.config = self._load_config(config_path)
        self.logger = self._setup_logger()
        self.cache = {}
        
    def _load_config(self, config_path: str) -> Dict:
        """Load the data integration configuration."""
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            raise Exception(f"Error loading config: {str(e)}")

    def _setup_logger(self) -> logging.Logger:
        """Setup logging configuration."""
        logger = logging.getLogger('DataIntegrator')
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def get_climate_data(self, district: str) -> Dict:
        """Get climate data for a specific district."""
        try:
            # Load district data
            district_data = self._load_json_data(self.config['data_sources']['climate_data']['district_data']['file_path'])
            
            # Get real-time sensor data
            sensor_data = self._get_sensor_data(district)
            
            # Get weather service data
            weather_data = self._get_weather_data(district)
            
            # Combine and validate data
            combined_data = self._combine_climate_data(
                district_data.get(district, {}),
                sensor_data,
                weather_data
            )
            
            # Add statistical analysis
            aggregated_data = self._aggregate_climate_data(combined_data)
            combined_data.update(aggregated_data)
            
            return combined_data
        except Exception as e:
            self.logger.error(f"Error getting climate data: {str(e)}")
            return {}

    def get_research_data(self, topic: str) -> List[Dict]:
        """Get research data for a specific topic."""
        try:
            research_data = self._load_json_data(self.config['data_sources']['research_data']['papers']['file_path'])
            return research_data.get(topic, [])
        except Exception as e:
            self.logger.error(f"Error getting research data: {str(e)}")
            return []

    def get_sdg_data(self, goal: str) -> Dict:
        """Get SDG data for a specific goal."""
        try:
            sdg_data = self._load_json_data(self.config['data_sources']['sdg_data']['indicators']['file_path'])
            return sdg_data.get(goal, {})
        except Exception as e:
            self.logger.error(f"Error getting SDG data: {str(e)}")
            return {}

    def _load_json_data(self, file_path: str) -> Dict:
        """Load data from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            self.logger.error(f"Error loading JSON data: {str(e)}")
            return {}

    def _get_sensor_data(self, district: str) -> Dict:
        """Get real-time sensor data for a district."""
        try:
            sensor_config = self._load_json_data(self.config['data_sources']['climate_data']['sensor_data']['file_path'])
            # Implement sensor data fetching logic here
            return {}
        except Exception as e:
            self.logger.error(f"Error getting sensor data: {str(e)}")
            return {}

    def _get_weather_data(self, district: str) -> Dict:
        """Get weather data from external services."""
        try:
            weather_config = self.config['api_integrations']['weather_services']
            # Implement weather API calls here
            return {}
        except Exception as e:
            self.logger.error(f"Error getting weather data: {str(e)}")
            return {}

    def _combine_climate_data(self, district_data: Dict, sensor_data: Dict, weather_data: Dict) -> Dict:
        """Combine data from different sources."""
        try:
            combined_data = district_data.copy()
            
            # Update with real-time sensor data
            if sensor_data:
                combined_data.update(sensor_data)
            
            # Update with weather service data
            if weather_data:
                combined_data.update(weather_data)
            
            # Validate combined data
            self._validate_data(combined_data)
            
            return combined_data
        except Exception as e:
            self.logger.error(f"Error combining climate data: {str(e)}")
            return district_data

    def _validate_data(self, data: Dict) -> bool:
        """Validate data according to defined rules."""
        try:
            validation_rules = self.config['data_processing']['validation']['rules']
            
            # Validate temperature
            if 'temperature' in data:
                temp = float(data['temperature'])
                if not (validation_rules['temperature_range'][0] <= temp <= validation_rules['temperature_range'][1]):
                    raise ValueError(f"Temperature {temp} outside valid range")
            
            # Validate humidity
            if 'humidity' in data:
                humidity = float(data['humidity'])
                if not (validation_rules['humidity_range'][0] <= humidity <= validation_rules['humidity_range'][1]):
                    raise ValueError(f"Humidity {humidity} outside valid range")
            
            return True
        except Exception as e:
            self.logger.error(f"Data validation error: {str(e)}")
            return False

    def process_query(self, query: str) -> Dict:
        """Process a user query and return relevant data."""
        try:
            # Determine query intent
            intent = self._determine_intent(query)
            
            # Get relevant data based on intent
            if intent == 'climate_inquiry':
                district = self._extract_district(query)
                if district is None:
                    # Try to get regional data if no specific district is mentioned
                    if any(region in query.lower() for region in ['northern', 'southern', 'central', 'western', 'eastern']):
                        region = self._extract_region(query)
                        return self.get_region_data(region)
                    return {
                        'error': 'No specific district mentioned',
                        'message': 'Please specify a district in Sindh to get climate information. You can ask about:\n' +
                                 '• Specific districts (e.g., Karachi, Hyderabad, Larkana)\n' +
                                 '• Regions (e.g., Northern Sindh, Southern Sindh)\n' +
                                 '• General climate information'
                    }
                
                # Get climate data for the district
                climate_data = self.get_climate_data(district)
                if not climate_data:
                    return {
                        'error': 'Data unavailable',
                        'message': f'I apologize, but I could not retrieve climate data for {district} at the moment. Please try again later.'
                    }
                return climate_data
                
            elif intent == 'research_inquiry':
                topic = self._extract_topic(query)
                research_data = self.get_research_data(topic)
                if not research_data:
                    return {
                        'error': 'No research data found',
                        'message': f'I could not find research data about {topic}. Please try a different topic or ask about climate information.'
                    }
                return research_data
                
            elif intent == 'sdg_inquiry':
                goal = self._extract_goal(query)
                sdg_data = self.get_sdg_data(goal)
                if not sdg_data:
                    return {
                        'error': 'No SDG data found',
                        'message': f'I could not find SDG data for {goal}. Please try a different goal or ask about climate information.'
                    }
                return sdg_data
                
            else:
                return {
                    'error': 'Unknown query intent',
                    'message': 'I\'m not sure what information you\'re looking for. You can ask about:\n' +
                             '• Climate information for specific districts\n' +
                             '• Research findings\n' +
                             '• Sustainable development goals'
                }
                
        except Exception as e:
            self.logger.error(f"Error processing query: {str(e)}")
            return {
                'error': 'Processing error',
                'message': 'I encountered an error while processing your request. Please try rephrasing your question or ask about a specific district in Sindh.'
            }

    def _determine_intent(self, query: str) -> str:
        """Determine the intent of a user query."""
        try:
            query_lower = query.lower()
            
            # Climate-related keywords
            climate_keywords = [
                'climate', 'weather', 'temperature', 'rainfall', 'humidity',
                'forecast', 'climate change', 'weather conditions',
                'rain', 'wind', 'pressure', 'heat', 'cold',
                'season', 'monsoon', 'drought', 'flood'
            ]
            
            # Research-related keywords
            research_keywords = [
                'research', 'study', 'paper', 'publication', 'findings',
                'analysis', 'report', 'survey', 'investigation',
                'data', 'statistics', 'trend', 'pattern'
            ]
            
            # SDG-related keywords
            sdg_keywords = [
                'sdg', 'sustainable', 'development', 'goal', 'target',
                'sustainability', 'environmental', 'conservation',
                'green', 'eco', 'renewable', 'clean energy'
            ]
            
            # Count keyword matches for each intent
            climate_matches = sum(1 for keyword in climate_keywords if keyword in query_lower)
            research_matches = sum(1 for keyword in research_keywords if keyword in query_lower)
            sdg_matches = sum(1 for keyword in sdg_keywords if keyword in query_lower)
            
            # Determine intent based on highest match count
            if climate_matches > research_matches and climate_matches > sdg_matches:
                return 'climate_inquiry'
            elif research_matches > climate_matches and research_matches > sdg_matches:
                return 'research_inquiry'
            elif sdg_matches > climate_matches and sdg_matches > research_matches:
                return 'sdg_inquiry'
            
            # Default to climate inquiry if no clear intent or equal matches
            return 'climate_inquiry'
            
        except Exception as e:
            self.logger.error(f"Error determining intent: {str(e)}")
            return 'climate_inquiry'  # Default intent

    def _extract_district(self, query: str) -> Optional[str]:
        """Extract district name from query."""
        try:
            # List of known districts in Sindh with common variations
            districts = {
                "Karachi": ["karachi", "khi"],
                "Hyderabad": ["hyderabad", "hyd"],
                "Sukkur": ["sukkur", "suk"],
                "Larkana": ["larkana", "lark"],
                "Nawabshah": ["nawabshah", "nawabshah"],
                "Mirpur Khas": ["mirpur khas", "mirpurkhas", "mk"],
                "Thatta": ["thatta"],
                "Badin": ["badin"],
                "Tharparkar": ["tharparkar", "thar"],
                "Dadu": ["dadu"],
                "Khairpur": ["khairpur"],
                "Jacobabad": ["jacobabad"],
                "Shikarpur": ["shikarpur"],
                "Ghotki": ["ghotki"],
                "Sanghar": ["sanghar"]
            }
            
            # Convert query to lowercase for case-insensitive matching
            query_lower = query.lower()
            
            # Check for each district and its variations
            for district, variations in districts.items():
                if any(variation in query_lower for variation in variations):
                    return district
            
            # If no district is found, return None
            return None
            
        except Exception as e:
            self.logger.error(f"Error extracting district: {str(e)}")
            return None

    def _extract_topic(self, query: str) -> str:
        """Extract research topic from query."""
        # Implement topic extraction logic here
        return 'climate_change'  # Default topic

    def _extract_goal(self, query: str) -> str:
        """Extract SDG goal from query."""
        # Implement goal extraction logic here
        return 'SDG 13'  # Default goal

    def _process_time_series_data(self, data: List[Dict], metric: str) -> Dict:
        """Process time series data to extract trends and statistics."""
        try:
            values = [float(d[metric]) for d in data if metric in d]
            if not values:
                return {}
            
            return {
                'mean': np.mean(values),
                'median': np.median(values),
                'std': np.std(values),
                'trend': self._calculate_trend(values),
                'anomalies': self._detect_anomalies(values)
            }
        except Exception as e:
            self.logger.error(f"Error processing time series data: {str(e)}")
            return {}

    def _calculate_trend(self, values: List[float]) -> str:
        """Calculate trend direction and magnitude."""
        try:
            if len(values) < 2:
                return "insufficient_data"
            
            slope, _, r_value, _, _ = stats.linregress(range(len(values)), values)
            
            if abs(r_value) < 0.3:
                return "no_significant_trend"
            elif slope > 0:
                return "increasing"
            else:
                return "decreasing"
        except Exception as e:
            self.logger.error(f"Error calculating trend: {str(e)}")
            return "error"

    def _detect_anomalies(self, values: List[float], threshold: float = 2.0) -> List[int]:
        """Detect anomalies using z-score method."""
        try:
            z_scores = np.abs(stats.zscore(values))
            return [i for i, z in enumerate(z_scores) if z > threshold]
        except Exception as e:
            self.logger.error(f"Error detecting anomalies: {str(e)}")
            return []

    def _aggregate_climate_data(self, data: Dict) -> Dict:
        """Aggregate climate data with statistical analysis."""
        try:
            aggregated = {}
            
            # Process temperature data
            if 'temperature_history' in data:
                aggregated['temperature_stats'] = self._process_time_series_data(
                    data['temperature_history'], 'temperature'
                )
            
            # Process rainfall data
            if 'rainfall_history' in data:
                aggregated['rainfall_stats'] = self._process_time_series_data(
                    data['rainfall_history'], 'rainfall'
                )
            
            # Add current conditions
            aggregated['current_conditions'] = {
                k: v for k, v in data.items() 
                if k in ['temperature', 'humidity', 'wind_speed', 'rainfall']
            }
            
            return aggregated
        except Exception as e:
            self.logger.error(f"Error aggregating climate data: {str(e)}")
            return {}

    def _extract_key_metrics(self, data: Dict) -> Dict:
        """Extract key metrics from research papers or SDG data."""
        try:
            metrics = {}
            
            if 'papers' in data:
                metrics['total_papers'] = len(data['papers'])
                metrics['recent_papers'] = len([p for p in data['papers'] 
                    if datetime.now().year - int(p.get('year', 0)) <= 2])
                metrics['key_findings'] = [p.get('key_findings', []) for p in data['papers'][:3]]
            
            if 'indicators' in data:
                metrics['total_indicators'] = len(data['indicators'])
                metrics['achieved_targets'] = len([i for i in data['indicators'] 
                    if i.get('status', '') == 'achieved'])
                metrics['in_progress'] = len([i for i in data['indicators'] 
                    if i.get('status', '') == 'in_progress'])
            
            return metrics
        except Exception as e:
            self.logger.error(f"Error extracting key metrics: {str(e)}")
            return {} 
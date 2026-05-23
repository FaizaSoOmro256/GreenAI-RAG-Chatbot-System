"""
Green AI Climate Chatbot - Core Implementation
Provides climate data and response generation functionality.
"""

import json
import logging
import streamlit as st
from typing import Dict, Any, Optional, List, Set
from pathlib import Path
import re
import random
from datetime import datetime
import dateutil.parser
import pytz

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Optional water resources data (used in some responses)
try:
    from utils.water_resources import (
        WATER_AVAILABILITY,
        WATER_SOURCES,
        WATER_QUALITY_ISSUES,
        WATER_PROJECTIONS,
        get_water_stress_category,
    )
except Exception:
    WATER_AVAILABILITY = {}
    WATER_SOURCES = {}
    WATER_QUALITY_ISSUES = {}
    WATER_PROJECTIONS = {}
    def get_water_stress_category(availability):
        return "Unknown"

# Optional NGO profiles (role-specific data)
try:
    from data.ngo_profiles import get_ngo_brief as _get_ngo_brief
except Exception:
    def _get_ngo_brief(district: str, lang: str = "urdu") -> str:
        return ""

class ChatBot:
    """Climate data chatbot core functionality."""
    
    def __init__(self, data_dir: str = 'data/chatbot'):
        self.data_dir = Path(data_dir)
        # Load complete district list from data module to ensure coverage (29 districts)
        try:
            from data.district_data import sindh_districts as _all_districts
            self.districts = set(_all_districts)
        except Exception:
            # Fallback to a reasonable default set
            self.districts = {
                'karachi', 'hyderabad', 'sukkur', 'larkana', 'mirpurkhas', 'nawabshah',
                'thatta', 'badin', 'tharparkar', 'dadu', 'jacobabad', 'kashmore',
                'ghotki', 'khairpur', 'naushahro feroze', 'shaheed benazirabad',
                'sanghar', 'tando allahyar', 'tando muhammad khan', 'matiari',
                'umerkot', 'jamshoro', 'shikarpur', 'sujawal'
            }
        self.karachi_divisions = {
            'central', 'east', 'south', 'west', 'malir', 'korangi'
        }
        
        # Load all data sources
        self.tehsil_data = self._load_tehsil_data()
        self.admin_units = self._load_admin_units()
        self.sensor_config = self._load_sensor_config()
        self.district_data = {}
        self.climate_data = {}
        self._initialize_data()

        # Build a normalization map from climate data keys to support space/underscore differences
        self.climate_key_by_normalized: Dict[str, str] = {}
        for key in self.climate_data.keys():
            norm = self._normalize_name(key)
            self.climate_key_by_normalized[norm] = key

        # Ensure every district has a climate entry (create minimal placeholders if missing)
        try:
            for district_name in sorted(self.districts):
                # Prefer underscored lower-case keys for climate_data
                underscored_key = district_name.strip().lower().replace(' ', '_')
                # If already present (either underscored or spaced variant), skip
                if underscored_key in self.climate_data:
                    continue
                if district_name.lower() in self.climate_data:
                    continue
                # Create a minimal placeholder climate profile
                self.climate_data[underscored_key] = {
                    "climate_profile": {
                        "temperature": {
                            "annual_average": "N/A",
                            "summer_max": "N/A",
                            "winter_min": "N/A",
                            "trend": "N/A"
                        },
                        "rainfall": {
                            "annual_average": "N/A",
                            "monsoon_contribution": "N/A",
                            "rainy_days": "N/A",
                            "trend": "N/A"
                        },
                        "humidity": {
                            "annual_average": "N/A",
                            "summer": "N/A",
                            "winter": "N/A",
                            "trend": "N/A"
                        },
                        "wind": {
                            "average_speed": "N/A",
                            "prevailing_direction": "N/A"
                        }
                    }
                }
                # Also add a basic district_data entry if missing
                if underscored_key not in self.district_data:
                    self.district_data[underscored_key] = {
                        "environmental_issues": [],
                        "climate_challenges": [],
                        "conservation_efforts": []
                    }
                # Register in normalization map
                self.climate_key_by_normalized[self._normalize_name(underscored_key)] = underscored_key
        except Exception:
            pass
        
        self.district_patterns = {
            'karachi': r'\b(?:karachi|khi|کراچی|ڪراچي)\b',
            'hyderabad': r'\b(?:hyderabad|hyd|حیدرآباد|حيدرآباد)\b',
            'thatta': r'\b(?:thatta|ٺٽو|تھٹہ)\b',
            'sukkur': r'\b(?:sukkur|سکھر|سکر)\b',
            'larkana': r'\b(?:larkana|لاڑکانہ|لاڙڪاڻو)\b',
            'mirpurkhas': r'\b(?:mirpurkhas|میرپورخاص|ميرپورخاص)\b',
            'nawabshah': r'\b(?:nawabshah|نوابشاہ|نوابشاھ)\b',
            'jacobabad': r'\b(?:jacobabad|جیکب آباد|جيڪب آباد)\b',
            'shikarpur': r'\b(?:shikarpur|شکارپور|شڪارپور)\b',
            'dadu': r'\b(?:dadu|دادو)\b',
            'jamshoro': r'\b(?:jamshoro|جامشورو|جامشورو)\b',
            'tharparkar': r'\b(?:tharparkar|thar|تھرپارکر|ٿرپارڪر)\b',
            'badin': r'\b(?:badin|بدین|بدين)\b',
            'sanghar': r'\b(?:sanghar|سانگھڑ|سانگھر)\b',
            'khairpur': r'\b(?:khairpur|خیرپور|خيرپور)\b',
            'ghotki': r'\b(?:ghotki|گھوٹکی|گهوٽڪي)\b',
            'kashmore': r'\b(?:kashmore|قاضی احمد|قاضي احمد)\b',
            'umerkot': r'\b(?:umerkot|عمرکوٹ|عمرڪوٽ)\b',
            'matiari': r'\b(?:matiari|mtyari|مٹیاری|مٽياري)\b',
            'tando allahyar': r'\b(?:tando allahyar|ٽنڊو الہ يار|ٹنڈو الہ یار)\b',
            'tando muhammad khan': r'\b(?:tando muhammad khan|ٽنڊو محمد خان|ٹنڈو محمد خان)\b',
            'naushahro feroze': r'\b(?:naushahro feroze|نوشہرو فیروز|نوشھرو فيروز)\b'
        }

    def _normalize_name(self, text: str) -> str:
        """Normalize names by lowercasing and collapsing spaces/underscores for robust matching."""
        return re.sub(r'[\s_]+', ' ', text.strip().lower())
        
    def _initialize_data(self):
        """Initialize all district and climate data including Karachi divisions."""
        try:
            # Import comprehensive climate data from new module
            try:
                import data.comprehensive_climate_data as comprehensive_climate
                self.climate_data = comprehensive_climate.district_climate_data
            except ImportError:
                # Fallback to original climate data
                import data.district_climate_data as climate_data
                self.climate_data = climate_data.district_climate_data
            
            # Import district data
            import data.district_data as district_data
            self.district_data = getattr(district_data, 'district_data', {})
            
            # Add Karachi divisions data if not present
            for division in self.karachi_divisions:
                key = f"karachi {division}"
                if key not in self.climate_data:
                    self.climate_data[key] = {
                        "climate_profile": {
                            "temperature": {
                                "annual_average": "27.5°C",
                                "summer_max": "40°C",
                                "winter_min": "13°C",
                                "trend": "Increasing by 0.4°C per decade"
                            },
                            "rainfall": {
                                "annual_average": "220mm",
                                "monsoon_contribution": "75%",
                                "rainy_days": "25-30 days per year",
                                "trend": "Variable with urban influence"
                            },
                            "humidity": {
                                "annual_average": "70%",
                                "summer": "80-85%",
                                "winter": "50-60%"
                            },
                            "wind": {
                                "average_speed": "12 km/h",
                                "prevailing_direction": "Southwest",
                                "dust_storms": "5-8 per year"
                            }
                        },
                        "climate_risks": {
                            "urban_heat_island": {
                                "temperature_difference": "2-4°C higher than suburbs",
                                "affected_areas": "Dense urban areas",
                                "impact": "Increased energy demand and health risks"
                            },
                            "flooding": {
                                "risk_level": "Moderate to High",
                                "frequency": "2-3 times per monsoon",
                                "affected_areas": "Low-lying areas and old drainage zones",
                                "mitigation": "Drainage system upgrades"
                            },
                            "air_quality": {
                                "main_pollutants": "PM2.5, NO2, CO",
                                "critical_periods": "Winter months",
                                "monitoring": "Continuous air quality monitoring",
                                "mitigation": "Traffic management and industrial controls"
                            }
                        }
                    }
                
                if key not in self.district_data:
                    self.district_data[key] = {
                        "environmental_issues": [
                            "Urban heat island effect",
                            "Air pollution from traffic and industry",
                            "Limited green spaces",
                            "Waste management challenges"
                        ],
                        "climate_challenges": [
                            "Rising temperatures",
                            "Urban flooding during monsoon",
                            "Air quality degradation",
                            "Heat wave vulnerability"
                        ],
                        "conservation_efforts": [
                            "Urban forestry initiatives",
                            "Air quality monitoring",
                            "Drainage system improvements",
                            "Green building practices"
                        ]
                    }
        except Exception as e:
            logger.error(f"Error initializing data: {str(e)}")
            self.district_data = {}
            self.climate_data = {}
            
    def _load_tehsil_data(self) -> Dict:
        """Load tehsil data from Python module."""
        try:
            import data.tehsil_data as td
            return {
                'tehsils': td.sindh_tehsils,
                'demographics': td.tehsil_demographics,
                'development': td.tehsil_development,
                'economy': td.tehsil_economy,
                'climate': td.tehsil_climate,
                'administrative': td.tehsil_administrative_units
            }
        except Exception as e:
            logger.error(f"Error loading tehsil data: {str(e)}")
            return {}
            
    def _load_admin_units(self) -> Dict:
        """Load administrative units data from Python module."""
        try:
            import data.administrative_units as au
            return {
                'hierarchy': au.administrative_hierarchy,
                'flow': au.administrative_flow,
                'responsibilities': au.level_responsibilities
            }
        except Exception as e:
            logger.error(f"Error loading administrative units data: {str(e)}")
            return {}

    def _load_sensor_config(self) -> Dict:
        """Load sensor configuration data."""
        try:
            with open(self.data_dir / 'sensor_integration.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading sensor configuration: {str(e)}")
            return {}

    def get_tehsil_info(self, tehsil: str) -> str:
        """Get comprehensive information about a tehsil."""
        try:
            response = [f"Information about {tehsil.title()} Tehsil:"]
            
            # Demographics
            demo = self.tehsil_data.get('demographics', {}).get(tehsil, {})
            if demo:
                response.append("\nDemographic Information:")
                response.append(f"• Population: {demo.get('population', 'N/A'):,}")
                response.append(f"• Area: {demo.get('area', 'N/A')} km²")
                response.append(f"• Population Density: {demo.get('density', 'N/A')} per km²")
                response.append(f"• Urban/Rural Ratio: {demo.get('urban_rural_ratio', 'N/A')}")
                response.append(f"• Literacy Rate: {demo.get('literacy_rate', 'N/A')}")
                if 'major_languages' in demo:
                    response.append(f"• Major Languages: {', '.join(demo['major_languages'])}")
            
            # Development Indicators
            dev = self.tehsil_data.get('development', {}).get(tehsil, {})
            if dev:
                response.append("\nDevelopment Indicators:")
                
                if 'education' in dev:
                    response.append("\nEducation Facilities:")
                    edu = dev['education']
                    response.append(f"• Primary Schools: {edu.get('primary_schools', 'N/A')}")
                    response.append(f"• Secondary Schools: {edu.get('secondary_schools', 'N/A')}")
                    response.append(f"• Colleges: {edu.get('colleges', 'N/A')}")
                    response.append(f"• Universities: {edu.get('universities', 'N/A')}")
                
                if 'healthcare' in dev:
                    response.append("\nHealthcare Facilities:")
                    health = dev['healthcare']
                    response.append(f"• Hospitals: {health.get('hospitals', 'N/A')}")
                    response.append(f"• Basic Health Units: {health.get('basic_health_units', 'N/A')}")
                    response.append(f"• Dispensaries: {health.get('dispensaries', 'N/A')}")
                
                if 'infrastructure' in dev:
                    response.append("\nInfrastructure:")
                    infra = dev['infrastructure']
                    response.append(f"• Road Network: {infra.get('road_network', 'N/A')}")
                    response.append(f"• Electricity Coverage: {infra.get('electricity_coverage', 'N/A')}")
                    response.append(f"• Water Supply Coverage: {infra.get('water_supply', 'N/A')}")
                    response.append(f"• Sewerage Coverage: {infra.get('sewerage', 'N/A')}")
            
            # Economic Activities
            econ = self.tehsil_data.get('economy', {}).get(tehsil, {})
            if econ:
                response.append("\nEconomic Profile:")
                if 'major_industries' in econ:
                    response.append("Major Industries:")
                    response.extend(f"• {industry}" for industry in econ['major_industries'])
                
                if 'agricultural_products' in econ:
                    response.append("\nMajor Agricultural Products:")
                    response.extend(f"• {product}" for product in econ['agricultural_products'])
                
                if 'employment_sectors' in econ:
                    response.append("\nEmployment by Sector:")
                    for sector, percentage in econ['employment_sectors'].items():
                        response.append(f"• {sector.title()}: {percentage}")
            
            # Climate and Environmental Data
            climate = self.tehsil_data.get('climate', {}).get(tehsil, {})
            if climate:
                response.append("\nClimate and Environmental Profile:")
                
                if 'temperature' in climate:
                    response.append("\nTemperature:")
                    temp = climate['temperature']
                    response.append(f"• Summer Maximum: {temp.get('summer_max', 'N/A')}")
                    response.append(f"• Summer Minimum: {temp.get('summer_min', 'N/A')}")
                    response.append(f"• Winter Maximum: {temp.get('winter_max', 'N/A')}")
                    response.append(f"• Winter Minimum: {temp.get('winter_min', 'N/A')}")
                
                if 'rainfall' in climate:
                    response.append("\nRainfall:")
                    rain = climate['rainfall']
                    response.append(f"• Annual Average: {rain.get('annual_average', 'N/A')}")
                    response.append(f"• Monsoon Contribution: {rain.get('monsoon_contribution', 'N/A')}")
                
                if 'environmental_issues' in climate:
                    response.append("\nEnvironmental Issues:")
                    response.extend(f"• {issue}" for issue in climate['environmental_issues'])
            
            # Administrative Units
            admin = self.tehsil_data.get('administrative', {}).get(tehsil, {})
            if admin:
                response.append("\nAdministrative Structure:")
                response.append(f"• Union Councils: {admin.get('union_councils', 'N/A')}")
                response.append(f"• Revenue Circles: {admin.get('revenue_circles', 'N/A')}")
                response.append(f"• Police Stations: {admin.get('police_stations', 'N/A')}")
                
                if 'administrative_offices' in admin:
                    response.append("\nAdministrative Offices:")
                    for office_type, offices in admin['administrative_offices'].items():
                        response.append(f"• {office_type.replace('_', ' ').title()}: {', '.join(offices)}")
            
            return '\n'.join(response)
            
        except Exception as e:
            logger.error(f"Error getting tehsil info: {str(e)}")
            return f"Sorry, I encountered an error while getting information about {tehsil.title()} Tehsil."

    def get_admin_unit_info(self, unit_type: str) -> str:
        """Get information about administrative units."""
        try:
            hierarchy = self.admin_units.get('hierarchy', {})
            if not unit_type.lower() in [k.lower() for k in hierarchy.keys()]:
                return f"No information available about {unit_type}."
            
            for key, data in hierarchy.items():
                if unit_type.lower() == key.lower():
                    response = [f"Information about {key}:"]
                    response.append(f"\nDescription: {data.get('description', 'N/A')}")
                    
                    if 'responsibilities' in data:
                        response.append("\nResponsibilities:")
                        response.extend(f"• {resp}" for resp in data['responsibilities'])
                    
                    if 'typical_composition' in data:
                        response.append("\nTypical Composition:")
                        response.extend(f"• {comp}" for comp in data['typical_composition'])
                    
                    if 'functions' in data:
                        response.append("\nFunctions:")
                        response.extend(f"• {func}" for func in data['functions'])
                    
                    if 'components' in data:
                        response.append("\nComponents:")
                        response.extend(f"• {comp}" for comp in data['components'])
                    
                    if 'characteristics' in data:
                        response.append("\nCharacteristics:")
                        response.extend(f"• {char}" for char in data['characteristics'])
                    
                    if 'features' in data:
                        response.append("\nFeatures:")
                        response.extend(f"• {feat}" for feat in data['features'])
                    
                    if 'management' in data:
                        response.append("\nManagement:")
                        response.extend(f"• {mgmt}" for mgmt in data['management'])
                    
                    return '\n'.join(response)
            
            return f"Could not find detailed information about {unit_type}."
            
        except Exception as e:
            logger.error(f"Error getting administrative unit info: {str(e)}")
            return f"Sorry, I encountered an error while getting information about {unit_type}."

    def find_tehsil(self, query: str) -> Optional[str]:
        """Find tehsil name in query."""
        query = query.lower()
        for division_data in self.tehsil_data.get('tehsils', {}).values():
            for district_tehsils in division_data.values():
                for tehsil in district_tehsils:
                    if tehsil.lower() in query:
                        return tehsil
        return None

    def load_data(self, filename: str) -> Dict:
        """Load data from JSON file."""
        try:
            # First try to load from data/chatbot directory
            file_path = self.data_dir / filename
            if not file_path.exists():
                # If not found, try data directory
                file_path = Path('data') / filename
                if not file_path.exists():
                    logger.error(f"Could not find {filename} in either {self.data_dir} or data/")
                return {}
            
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading {filename}: {str(e)}")
            return {}

    def get_about_info(self) -> str:
        """Get information about Green AI."""
        return """Green AI is an advanced climate information system designed specifically for Sindh, Pakistan. Here's what makes it special:

• Purpose: Provides real-time climate and environmental data for all districts in Sindh
• Features:
  - District-specific climate information
  - Environmental issue tracking
  - Agricultural impact assessment
  - Adaptation measures and recommendations
  - Historical climate patterns
  - Future climate projections

• Data Sources:
  - Local weather stations
  - Environmental monitoring systems
  - Agricultural databases
  - Climate research institutions
  - Government environmental reports

• Key Benefits:
  - Helps communities understand local climate challenges
  - Supports agricultural planning and adaptation
  - Tracks environmental changes over time
  - Provides actionable insights for sustainability
  - Makes climate data accessible to everyone

Green AI aims to empower Sindh's communities with the knowledge they need to address climate challenges and build a sustainable future."""

    def get_team_info(self) -> str:
        """Get information about the project team."""
        return """The Green AI project is developed by a dedicated team from the Department of Computer Science at University of Sufism and Modern Sciences, Bhitshah:

• Project Team:
  - Faiza Soomro (Team Lead)
  - Damini Lohana
  - Sahrish Turk

• Project Supervisor: 
  - Madam Zojan Memon
    Faculty Member, Department of Information and Computing
    University of Sufism and Modern Sciences, Bhitshah

The team is focused on developing innovative AI solutions for climate monitoring and adaptation in Sindh."""

    def get_sdg_info(self) -> str:
        """Get information about SDG relevance."""
        return """Green AI primarily addresses SDG 13 - Climate Action, while contributing to several other SDGs:

• SDG 13 - Climate Action:
  - Strengthening climate resilience
  - Improving climate adaptation capacity
  - Enhancing climate change awareness
  - Supporting evidence-based decision making

• Related SDGs:
  - SDG 2: Zero Hunger (Agricultural resilience)
  - SDG 11: Sustainable Cities
  - SDG 15: Life on Land
  - SDG 17: Partnerships for the Goals

The project helps achieve these targets through:
• Data-driven climate monitoring
• Community-focused adaptation strategies
• Agricultural sustainability support
• Environmental protection measures"""

    def get_future_plans(self) -> str:
        """Get information about project future plans."""
        return """Green AI's future development plans include:

Phase 1 (Current):
• District-level climate data integration
• Basic climate analysis and reporting
• Environmental issue tracking

Phase 2 (Upcoming):
• Enhanced data analytics
• Multi-language support (Sindhi, Urdu)
• Mobile application development
• Real-time weather alerts

Phase 3 (Future):
• Advanced climate prediction models
• Satellite data integration
• Community engagement platform
• Agricultural advisory system

Long-term vision:
• Comprehensive climate monitoring
• Province-wide implementation
• Integration with national systems
• International collaboration"""

    def get_research_info(self) -> str:
        """Get information about research and findings."""
        return """Our climate research in Sindh has revealed several key findings:

Temperature Trends:
• Average temperature increase of 0.5°C per decade
• More frequent heat waves
• Extended summer seasons

Rainfall Patterns:
• Increased monsoon intensity
• More erratic rainfall distribution
• Extended dry periods

Coastal Impacts:
• Rising sea levels affecting Thatta and Badin
• Increased coastal erosion
• Saltwater intrusion

Agricultural Effects:
• Changed growing seasons
• Increased water stress
• New pest patterns

Research Methods:
• Historical data analysis
• Satellite imagery
• Ground station monitoring
• Community surveys"""

    def get_adaptation_info(self) -> str:
        """Get information about climate adaptation measures."""
        return """Climate adaptation measures for Sindh include:

Agricultural Adaptations:
• Drought-resistant crop varieties
• Water-efficient irrigation
• Crop diversification
• Changed planting schedules

Coastal Protection:
• Mangrove restoration
• Sea wall construction
• Coastal zone management
• Community relocation plans

Urban Solutions:
• Green infrastructure
• Heat island reduction
• Water conservation
• Flood management

Water Management:
• Rainwater harvesting
• Groundwater protection
• Water recycling
• Efficient distribution

Implementation Progress:
• Pilot projects in key districts
• Community participation
• Government support
• NGO partnerships"""

    def get_technical_info(self) -> str:
        """Get information about technical capabilities."""
        return """Green AI Technical Capabilities:

Data Integration:
• Real-time weather APIs
• Satellite data feeds
• Ground station networks
• Historical databases

Update Frequency:
• Weather data: Hourly
• Climate trends: Monthly
• Environmental indicators: Weekly
• Agricultural data: Seasonal

Language Support:
• Current: English
• Planned: Sindhi, Urdu
• Technical terms glossary
• Local context adaptation

System Features:
• Climate data analysis
• District-level reporting
• Trend visualization
• Adaptation recommendations

Limitations:
• Data coverage varies by district
• Some historical gaps exist
• Real-time data depends on connectivity
• Projections have uncertainty ranges"""

    def get_sensor_info(self, sensor_type: str = None) -> str:
        """Get information about available sensors and their configurations."""
        try:
            if not self.sensor_config:
                return "Sensor configuration data is not available."
            
            configs = self.sensor_config.get('sensor_configurations', {})
            if not sensor_type:
                # Return overview of all sensor types
                response = ["Available Sensor Systems:"]
                for sensor, config in configs.items():
                    response.append(f"\n{sensor.replace('_', ' ').title()}:")
                    response.append(f"• Update Frequency: {config.get('data_refresh_rate', 'N/A')}")
                    response.append("• Monitored Parameters:")
                    response.extend(f"  - {param.replace('_', ' ').title()}" 
                                 for param in config.get('api_endpoints', {}).keys())
                return '\n'.join(response)
            
            # Return detailed info for specific sensor type
            sensor_type = sensor_type.lower().replace(' ', '_')
            if sensor_type not in configs:
                return f"No information available for {sensor_type} sensors."
            
            config = configs[sensor_type]
            response = [f"{sensor_type.replace('_', ' ').title()} Sensor System:"]
            
            # Data collection details
            response.append(f"\nData Collection:")
            response.append(f"• Update Frequency: {config.get('data_refresh_rate', 'N/A')}")
            
            # Parameters monitored
            if 'api_endpoints' in config:
                response.append("\nMonitored Parameters:")
                for param in config['api_endpoints'].keys():
                    response.append(f"• {param.replace('_', ' ').title()}")
            
            # Alert thresholds
            if 'alert_thresholds' in config:
                response.append("\nAlert Thresholds:")
                for param, thresholds in config['alert_thresholds'].items():
                    response.append(f"\n{param.replace('_', ' ').title()}:")
                    for level, value in thresholds.items():
                        response.append(f"• {level.replace('_', ' ').title()}: {value}")
            
            # Add notification settings
            notif = self.sensor_config.get('notification_settings', {})
            if notif:
                response.append("\nNotification System:")
                response.append("• Alert Channels: " + 
                              ', '.join(notif.get('alert_channels', [])))
                
                response.append("\nAlert Priority Levels:")
                for priority, details in notif.get('alert_priorities', {}).items():
                    response.append(f"\n{priority.title()}:")
                    response.append(f"• Channels: {', '.join(details.get('channels', []))}")
                    response.append(f"• Response Time: {details.get('response_time', 'N/A')}")
            
            # Add analysis capabilities
            analysis = self.sensor_config.get('data_analysis', {})
            if analysis:
                response.append("\nData Analysis Capabilities:")
                
                trend = analysis.get('trend_analysis', {})
                if trend:
                    response.append("\nTrend Analysis:")
                    response.append("• Time Periods: " + 
                                  ', '.join(trend.get('time_periods', [])))
                    response.append("• Metrics: " + 
                                  ', '.join(trend.get('metrics', [])))
                
                predict = analysis.get('predictive_models', {}).get(sensor_type, {})
                if predict:
                    response.append("\nPredictive Modeling:")
                    response.append(f"• Forecast Period: {predict.get('forecast_period', 'N/A')}")
                    response.append(f"• Confidence Threshold: {predict.get('confidence_threshold', 'N/A')}")
                    response.append(f"• Update Frequency: {predict.get('update_frequency', 'N/A')}")
            
            return '\n'.join(response)
            
        except Exception as e:
            logger.error(f"Error getting sensor info: {str(e)}")
            return "Sorry, I encountered an error while retrieving sensor information."

    def is_about_query(self, query: str) -> bool:
        """Check if query is asking about Green AI."""
        query = query.lower().strip()
        
        # About question patterns
        about_patterns = [
            'what is', 'what does', 'who is', 'tell me about', 'explain',
            'describe', 'how does', 'purpose of', 'goal of', 'objective of'
        ]
        
        # Project references
        project_refs = [
            'ecosphere', 'green', 'greenai', 'green ai', 'the system', 'this system',
            'this assistant', 'this project', 'the project'
        ]

        # Check for exact about patterns
        has_about = any(pattern in query for pattern in about_patterns)
        has_project = any(ref in query for ref in project_refs)

        # Special case for direct "what is Green AI" type questions (legacy Ecosphere queries still supported)
        if query.startswith('what') and any(ref in query for ref in ['ecosphere', 'green', 'greenai', 'green ai']):
            return True

        return has_about and has_project

    def is_team_query(self, query: str) -> bool:
        """Check if query is about team information."""
        query = query.lower().strip()
        
        # Direct team/creator questions
        team_patterns = [
            'team', 'creator', 'developer', 'who made', 'who created',
            'who developed', 'who built', 'who is creating', 'who is developing',
            'who are the creators', 'who are the developers', 'who is behind',
            'team behind', 'developed by', 'created by', 'built by', 'supervisor',
            'supervising', 'faculty', 'department', 'university', 'people behind',
            'members', 'who works', 'working on', 'tell me about the team'
        ]
        
        # Team member names
        team_members = [
            'faiza', 'soomro', 'damini', 'lohana', 'sahrish', 'turk',
            'zojan', 'memon', 'madam'
        ]
        
        # Check for exact team question patterns
        has_team_pattern = any(pattern in query for pattern in team_patterns)
        has_team_member = any(member in query for member in team_members)
        has_project_ref = any(ref in query for ref in ['ecosphere', 'greenai', 'green ai', 'greenai', 'green ai', 'project', 'this', 'the'])
        
        # Return true if we have a team pattern or team member name
        return has_team_pattern or has_team_member or (has_project_ref and 'who' in query)

    def is_sdg_query(self, query: str) -> bool:
        """Check if query is about SDGs."""
        query = query.lower()
        sdg_keywords = {'sdg', 'sustainable', 'development', 'goal', 'climate action', 'climate goal'}
        return any(keyword in query for keyword in sdg_keywords)

    def is_future_query(self, query: str) -> bool:
        """Check if query is about future plans."""
        query = query.lower().strip()
        future_keywords = {
            'future', 'plan', 'next', 'improve', 'phase', 'timeline', 'expand',
            'upcoming', 'roadmap', 'development', 'what will', 'going to',
            'enhancement', 'future development', 'what are the plans',
            'what is planned', 'what is next', 'what comes next',
            'how will it improve', 'future features', 'upcoming features'
        }
        return any(keyword in query for keyword in future_keywords)

    def is_research_query(self, query: str) -> bool:
        """Check if query is about research findings."""
        query = query.lower()
        research_patterns = {
            'research', 'finding', 'study', 'analysis', 'trend', 'change', 'data',
            'how is', 'what is happening', 'what are the changes', 'climate change',
            'temperature', 'rainfall', 'weather', 'climate', 'changing'
        }
        locations = {'sindh', 'province', 'region', 'area'}
        
        # Check for climate change related patterns
        if 'how' in query and 'climate' in query and 'change' in query:
            return True
            
        # Check for general research patterns
        has_research = any(pattern in query for pattern in research_patterns)
        has_location = any(location in query for location in locations)
        
        return has_research and (has_location or 'climate' in query)

    def is_adaptation_query(self, query: str) -> bool:
        """Check if query is about adaptation measures."""
        query = query.lower()
        adaptation_keywords = {'adapt', 'solution', 'measure', 'action', 'address', 'implement', 'protect'}
        return any(keyword in query for keyword in adaptation_keywords)

    def is_technical_query(self, query: str) -> bool:
        """Check if query is about technical aspects."""
        query = query.lower()
        technical_keywords = {'api', 'data', 'language', 'update', 'work', 'capability', 'feature', 'technical'}
        return any(keyword in query for keyword in technical_keywords)

    def is_sensor_query(self, query: str) -> bool:
        """Check if query is about sensors."""
        query = query.lower()
        sensor_keywords = {
            'sensor', 'monitor', 'measurement', 'reading', 'temperature',
            'humidity', 'rainfall', 'wind', 'air quality', 'water quality',
            'weather station', 'pm2.5', 'pm10', 'aqi', 'ph', 'turbidity'
        }
        return any(keyword in query for keyword in sensor_keywords)

    # ---------------------- General Climate Knowledge ----------------------
    def is_general_climate_topic(self, query: str) -> bool:
        """Detect broad, non-district climate questions (e.g., climate change, policy, renewable energy)."""
        query = query.lower()
        general_keywords = {
            # Basics
            'climate change', 'global warming', 'greenhouse effect', 'carbon footprint',
            # Energy
            'renewable energy', 'solar', 'wind energy', 'wind power', 'energy efficiency', 'led',
            # Water
            'water management', 'conserve water', 'water scarcity', 'glacier', 'melting glaciers',
            # Agriculture
            'climate-smart', 'drought-resistant', 'food security', 'crop yields',
            # Urban
            'urban heat island', 'green building', 'green buildings', 'smart city',
            # Policy/finance
            'paris agreement', 'ndc', 'nationally determined contribution', 'climate finance', 'policy',
            # Justice/social
            'climate justice', 'vulnerable communities', 'inclusive', 'gender', 'migration',
            # Transport/waste/circular
            'public transportation', 'electric vehicles', 'ev', 'cycling', 'circular economy', 'compost', 'recycling', 'plastic waste',
            # Nature/biodiversity
            'mangrove', 'biodiversity', 'ecosystem-based', 'nature-based', 'forests',
            # Technical
            'carbon sequestration', 'carbon markets', 'emissions trading', 'climate modeling', 'tipping points',
            # Education/awareness
            'educate', 'communication', 'media', 'schools', 'youth',
            # Disaster/resilience
            'adaptation', 'resilience', 'early warning', 'disaster', 'risk reduction'
        }
        return any(k in query for k in general_keywords)

    def generate_general_climate_response(self, query: str) -> str:
        """Return concise, actionable responses for broad climate questions using built-in knowledge."""
        q = query.lower()

        # Basics
        if ('climate change' in q and any(k in q for k in ['what is', 'explain', 'define', 'simple'])) or 'what is climate change' in q:
            return (
                "Climate change is the long‑term shift in average weather patterns caused mainly by human activities "
                "that increase greenhouse gases (CO2, CH4, N2O). It leads to higher temperatures, erratic rainfall, "
                "sea‑level rise, and more extreme events."
            )
        if 'greenhouse effect' in q:
            return (
                "The greenhouse effect is the warming of Earth as gases like CO2 and methane trap outgoing heat. "
                "A stronger (enhanced) greenhouse effect from human emissions drives global warming."
            )
        if 'carbon footprint' in q or 'reduce my emissions' in q:
            return (
                "Reduce your carbon footprint by: switching to LED lighting; using public transport/carpooling; "
                "installing rooftop solar where possible; efficient appliances; avoiding single‑use plastics; "
                "eating seasonal foods; and conserving water and electricity."
            )

        # Energy
        if 'renewable energy' in q or 'solar' in q or 'wind' in q:
            return (
                "Sindh has strong renewable potential: Jhimpir–Gharo wind corridor and high solar irradiance. "
                "Households can adopt rooftop solar, solar water heaters, and efficient appliances; "
                "governments can expand wind/solar parks and modernize the grid."
            )
        if 'energy efficiency' in q or 'led' in q:
            return (
                "Energy efficiency tips: LED lighting, inverter ACs, star‑rated appliances, insulation/shading, "
                "smart plugs, and turning devices fully off. Businesses should audit loads and fix peak demand."
            )

        # Water
        if 'water' in q and ('conserve' in q or 'management' in q or 'scarcity' in q):
            return (
                "Sustainable water management: canal lining, drip/sprinkler irrigation, rainwater harvesting, "
                "leak repair, low‑flow fixtures, groundwater recharge, and watershed protection."
            )
        if 'glacier' in q:
            return (
                "Melting glaciers first increase early‑summer river flows then reduce late‑summer supply, raising flood and drought risks. "
                "Adapt via storage, demand management, and early‑warning systems."
            )

        # Agriculture
        if 'climate-smart' in q or 'drought-resistant' in q or 'food security' in q or 'crop yield' in q:
            return (
                "Climate‑smart agriculture: drought‑/heat‑tolerant varieties, adjusted sowing dates, mulching, "
                "precision/drip irrigation, soil organic matter, diversified crops, and agromet advisories."
            )

        # Urban
        if 'urban heat island' in q or 'green building' in q or 'smart city' in q:
            return (
                "Urban heat solutions: cool/green roofs, shade trees, reflective pavements, permeable surfaces, "
                "ventilated street canyons, and heat‑health action plans. Green buildings use insulation, cross‑ventilation, "
                "efficient HVAC, and daylighting."
            )

        # Policy/finance
        if 'paris agreement' in q:
            return (
                "The Paris Agreement is a global pact to limit warming well below 2°C (aim 1.5°C) via national climate plans (NDCs), "
                "regular updates, transparency, and climate finance for developing countries."
            )
        if 'ndc' in q or 'nationally determined contribution' in q:
            return (
                "Pakistan's updated NDC (2021) targets a 50% reduction in projected 2030 emissions (15% unconditional, 35% conditional on finance), "
                "with adaptation priorities in water, agriculture, disaster risk reduction, and resilient cities."
            )
        if 'climate finance' in q:
            return (
                "Climate finance refers to funding for mitigation and adaptation from public and private sources, including grants, concessional loans, "
                "and carbon markets (e.g., GCF, MDBs, bilateral programs)."
            )
        if 'climate justice' in q:
            return (
                "Climate justice emphasizes fair burden‑sharing and protection of vulnerable groups, ensuring inclusive planning, social safety nets, "
                "and equitable access to finance and technology."
            )

        # Transport/waste/circular
        if 'electric vehicle' in q or 'ev' in q or 'public transportation' in q or 'cycling' in q:
            return (
                "Low‑carbon mobility: prioritize public transport and bus rapid transit, enable cycling/walking, adopt EVs for fleets, "
                "and manage traffic for cleaner air and lower emissions."
            )
        if 'circular economy' in q or 'recycling' in q or 'compost' in q or 'plastic' in q:
            return (
                "Circular economy actions: reduce single‑use plastics, segregate waste at source, recycle materials, compost organics, "
                "and design products for durability and reuse."
            )

        # Nature/biodiversity
        if 'mangrove' in q or 'biodiversity' in q or 'nature-based' in q or 'ecosystem-based' in q or 'forests' in q:
            return (
                "Nature‑based solutions: protect/restored mangroves in the Indus Delta, expand urban/peri‑urban forests, conserve wetlands, "
                "and use ecosystem‑based adaptation (buffers, corridors, restoration) to reduce risk and store carbon."
            )

        # Technical
        if 'carbon sequestration' in q:
            return (
                "Carbon sequestration stores CO2 in forests, soils, wetlands, and geological formations; it includes natural and engineered methods."
            )
        if 'carbon market' in q or 'emissions trading' in q:
            return (
                "Carbon markets allow trading of emission reductions via cap‑and‑trade or crediting (offsets) to lower costs and spur mitigation."
            )
        if 'climate modeling' in q:
            return (
                "Climate modeling uses physics‑based models (GCMs/RCMs) and scenarios to project temperature, rainfall, and extremes for planning."
            )
        if 'tipping point' in q:
            return (
                "Climate tipping points are thresholds where small changes trigger large, irreversible shifts (e.g., ice sheet loss, monsoon shifts)."
            )
        if 'ai' in q and ('monitor' in q or 'climate' in q or 'adapt' in q):
            return (
                "AI supports climate by: fusing sensor/satellite data, spotting trends and anomalies, forecasting hazards, "
                "optimizing irrigation/energy use, and powering early‑warning and decision dashboards."
            )

        # Education/awareness and disaster/resilience
        if 'educate' in q or 'communication' in q or 'schools' in q or 'youth' in q or 'media' in q:
            return (
                "Effective climate education: age‑appropriate curricula, local examples, hands‑on projects, myth‑busting, and community campaigns; "
                "engage youth via clubs, hackathons, and citizen science."
            )
        if 'early warning' in q or 'disaster' in q or 'resilience' in q or 'risk reduction' in q:
            return (
                "Resilience measures: multi‑hazard early‑warning systems, risk‑informed land‑use, flood‑safe infrastructure, shelters, "
                "and community drills with clear evacuation plans."
            )

        # Monitoring, partnerships, behavior, transfer, engagement
        if 'indicator' in q or 'monitoring' in q and ('impact' in q or 'adaptation' in q or 'progress' in q):
            return (
                "Track climate action with indicators such as GHG trends, renewable share, water efficiency, heat‑health outcomes, "
                "flood losses avoided, early‑warning coverage, and ecosystem restoration hectares."
            )
        if 'partnership' in q or 'collaborat' in q or 'cooperate' in q:
            return (
                "Build partnerships across government, academia, private sector, NGOs, and communities; co‑design projects, share data, "
                "and align funding to scale proven solutions."
            )
        if 'behavior' in q or 'nudge' in q or 'habit' in q:
            return (
                "Behavior change: feedback on bills, social norms, default green options, visible prompts, and incentives for saving water/energy."
            )
        if 'technology transfer' in q or 'tech transfer' in q:
            return (
                "Technology transfer uses licensing, joint ventures, training, and open standards to localize climate tech and build capacity."
            )
        if 'community' in q and ('engage' in q or 'organize' in q or 'participatory' in q or 'leadership' in q):
            return (
                "Community engagement: participatory planning, local climate committees, citizen science, micro‑grants, and leadership training."
            )
        if 'research' in q or 'data' in q and ('collect' in q or 'priorit' in q or 'access' in q):
            return (
                "Research priorities: high‑resolution climate data, water balance, heat‑health, crop stress, and coastal risks; "
                "improve open data portals and university‑policy collaboration."
            )

        # Success stories, future, economy/social
        if 'success' in q or 'case' in q or 'story' in q:
            return (
                "Examples in Sindh: large‑scale mangrove restoration in the Indus Delta; Jhimpir–Gharo wind corridor; "
                "urban forestry pilots; drip irrigation adoption in water‑stressed districts."
            )
        if '2050' in q or 'future' in q and ('scenario' in q or 'prepare' in q or 'long-term' in q):
            return (
                "By 2050: hotter summers, erratic monsoon, higher sea level; prepare via resilient infrastructure, water storage, "
                "renewables, nature‑based buffers, and climate‑smart agriculture."
            )
        if 'job' in q or 'green job' in q or 'opportunit' in q and ('econom' in q or 'business' in q):
            return (
                "Green jobs: solar/wind installation and O&M, energy audits, building retrofits, mangrove restoration, water efficiency, "
                "recycling and circular businesses."
            )
        if 'econom' in q or 'social impact' in q or 'vulnerable' in q:
            return (
                "Economic/social impacts: heat stress on labor and health, crop losses, flood damages, and coastal risks; "
                "target support for vulnerable groups and climate‑resilient livelihoods."
            )

        # Generic helpful response for other broad climate questions
        return (
            "Here's a concise guide: causes (GHG emissions, land use), impacts in Sindh (heat, erratic monsoon, floods/droughts, coastal risks), "
            "and solutions: energy efficiency, solar/wind, water conservation, climate‑smart agriculture, nature‑based measures, and resilient cities."
        )

    def find_district(self, query: str) -> Optional[str]:
        """Find district name in query."""
        query = query.lower().strip()
        normalized_query = self._normalize_name(query)
        
        # First check for Karachi divisions with different word orders
        for division in self.karachi_divisions:
            patterns = [
                f"karachi {division}",  # e.g. "karachi central"
                f"{division} karachi",  # e.g. "central karachi"
                division  # e.g. "central" (when context is clearly about Karachi)
            ]
            if any(pattern in query for pattern in patterns):
                # Prefer exact climate data key if present
                prefer_key = self.climate_key_by_normalized.get(self._normalize_name(f"karachi_{division}"))
                return prefer_key or f"karachi_{division}"
        
        # Then check for general districts
        for district in self.districts:
            if district in query:
                # Normalize both sides and look up a known climate key
                normalized = self._normalize_name(district)
                if normalized in self.climate_key_by_normalized:
                    return self.climate_key_by_normalized[normalized]
                # Try underscore variant
                underscore_variant = self._normalize_name(district.replace(' ', '_'))
                return self.climate_key_by_normalized.get(underscore_variant, district)
                
        return None

    def is_climate_query(self, query: str) -> bool:
        """Check if query is about climate."""
        query = query.lower().strip()
        climate_keywords = {
            'climate', 'weather', 'temperature', 'rainfall', 'rain',
            'humidity', 'monsoon', 'heat', 'cold', 'precipitation',
            'weather like', "what's the climate", 'how is the climate',
            'what is the climate', 'climate like'
        }
        return any(keyword in query for keyword in climate_keywords)

    def get_district_info(self, district: str, query: str = "") -> str:
        """Get comprehensive information about a district."""
        try:
            if not district:
                return "District not found."
            
            # Import district data from Python module
            from data.district_climate_data import district_climate_data
            
            # Normalize district name to match data format
            district = district.lower()
            
            # Find the matching district key (case-insensitive)
            district_key = next((k for k in district_climate_data.keys() if k.lower() == district), None)
            if not district_key:
                return f"No data available for {district.title()}"
            
            district_data = district_climate_data[district_key]
            query = query.lower()
            
            # If query is specifically about climate
            if "climate" in query:
                if 'climate_profile' in district_data:
                    return self.format_climate_profile(district_data['climate_profile'])
                else:
                    return f"Climate profile not available for {district.title()}"
            
            # For other weather-related queries
            if any(word in query for word in ["weather", "temperature", "rainfall", "humidity", "wind"]):
                if 'climate_profile' in district_data:
                    return self.format_climate_profile(district_data['climate_profile'])
                else:
                    return f"Weather information not available for {district.title()}"
            
            # Default to showing climate profile
            if 'climate_profile' in district_data:
                return self.format_climate_profile(district_data['climate_profile'])
            
            return f"No detailed information available for {district.title()}"
            
        except Exception as e:
            logger.error(f"Error getting district info: {str(e)}")
            return f"Sorry, I encountered an error while getting information about {district.title()}. Please try again."

    def process_climate_query(self, district_data: dict, query: str) -> str:
        """Process specific climate data queries."""
        if "rainfall" in query or "precipitation" in query:
            return f"Annual rainfall: {district_data['climate_profile']['rainfall']['annual_average']}"
        elif "temperature" in query:
            temp = district_data['climate_profile']['temperature']
            return f"Temperature: {temp['annual_average']} (Average), Range: {temp['min']} to {temp['max']}"
        else:
            return self.format_climate_profile(district_data['climate_profile'])

    def format_climate_profile(self, climate_profile: dict) -> str:
        """Format comprehensive climate profile data into a visually appealing, readable response."""
        try:
            response = []

            # Temperature - Comprehensive data
            temp = climate_profile.get('temperature', {})
            if temp:
                response.append("\n------------------------------")
                response.append("🌡️ <b>Temperature</b>")
                response.append(f"  • <b>Annual average:</b> {temp.get('annual_average', 'N/A')}")
                
                # Daily averages by season
                daily_avg = temp.get('daily_average', {})
                if daily_avg:
                    response.append("  • <b>Daily averages by season:</b>")
                    for season, range_temp in daily_avg.items():
                        response.append(f"    - {season.title()}: {range_temp}")
                
                # Seasonal averages
                seasonal_avg = temp.get('seasonal_averages', {})
                if seasonal_avg:
                    response.append("  • <b>Seasonal averages:</b>")
                    for season, avg_temp in seasonal_avg.items():
                        response.append(f"    - {season.title()}: {avg_temp}")
                
                # Temperature extremes
                extremes = temp.get('extremes', {})
                if extremes:
                    response.append("  • <b>Temperature extremes:</b>")
                    if 'highest_recorded' in extremes:
                        response.append(f"    - Highest recorded: {extremes['highest_recorded']}")
                    if 'lowest_recorded' in extremes:
                        response.append(f"    - Lowest recorded: {extremes['lowest_recorded']}")
                    if 'summer_max' in extremes:
                        response.append(f"    - Summer maximum: {extremes['summer_max']}")
                    if 'winter_min' in extremes:
                        response.append(f"    - Winter minimum: {extremes['winter_min']}")
                
                if temp.get('trend'):
                    response.append(f"  • <b>Trend:</b> {temp['trend']}")

            # Precipitation - Comprehensive data
            precip = climate_profile.get('precipitation', {})
            if precip:
                response.append("\n🌧️ <b>Precipitation</b>")
                response.append(f"  • <b>Annual total:</b> {precip.get('annual_total', 'N/A')}")
                
                # Rainfall details
                rainfall = precip.get('rainfall', {})
                if rainfall:
                    response.append("  • <b>Rainfall:</b>")
                    response.append(f"    - Annual: {rainfall.get('annual', 'N/A')}")
                    response.append(f"    - Monsoon contribution: {rainfall.get('monsoon_contribution', 'N/A')}")
                    response.append(f"    - Rainy days: {rainfall.get('rainy_days', 'N/A')}")
                
                # Other precipitation types
                if 'snowfall' in precip:
                    response.append(f"  • <b>Snowfall:</b> {precip['snowfall']}")
                if 'sleet' in precip:
                    response.append(f"  • <b>Sleet:</b> {precip['sleet']}")
                if 'hail' in precip:
                    response.append(f"  • <b>Hail:</b> {precip['hail']}")
                
                # Seasonal totals
                seasonal_totals = precip.get('seasonal_totals', {})
                if seasonal_totals:
                    response.append("  • <b>Seasonal totals:</b>")
                    for season, total in seasonal_totals.items():
                        response.append(f"    - {season.title()}: {total}")
                
                if 'patterns' in precip:
                    response.append(f"  • <b>Patterns:</b> {precip['patterns']}")
                if 'variability' in precip:
                    response.append(f"  • <b>Variability:</b> {precip['variability']}")

            # Humidity - Comprehensive data
            humidity = climate_profile.get('humidity', {})
            if humidity:
                response.append("\n💧 <b>Humidity</b>")
                response.append(f"  • <b>Annual average:</b> {humidity.get('annual_average', 'N/A')}")
                
                # Seasonal variations
                seasonal_variations = humidity.get('seasonal_variations', {})
                if seasonal_variations:
                    response.append("  • <b>Seasonal variations:</b>")
                    for season, range_humidity in seasonal_variations.items():
                        response.append(f"    - {season.title()}: {range_humidity}")
                
                # Daily patterns
                daily_patterns = humidity.get('daily_patterns', {})
                if daily_patterns:
                    response.append("  • <b>Daily patterns:</b>")
                    for time, range_humidity in daily_patterns.items():
                        response.append(f"    - {time.title()}: {range_humidity}")
                
                if humidity.get('trend'):
                    response.append(f"  • <b>Trend:</b> {humidity['trend']}")

            # Wind Patterns - Comprehensive data
            wind = climate_profile.get('wind_patterns', {})
            if wind:
                response.append("\n💨 <b>Wind Patterns</b>")
                
                # Prevailing directions
                directions = wind.get('prevailing_directions', {})
                if directions:
                    response.append("  • <b>Prevailing directions:</b>")
                    for season, direction in directions.items():
                        response.append(f"    - {season.title()}: {direction}")
                
                # Wind speeds
                speeds = wind.get('wind_speeds', {})
                if speeds:
                    response.append("  • <b>Wind speeds:</b>")
                    for condition, speed in speeds.items():
                        response.append(f"    - {condition.replace('_', ' ').title()}: {speed}")
                
                # Seasonal changes
                seasonal_changes = wind.get('seasonal_changes', {})
                if seasonal_changes:
                    response.append("  • <b>Seasonal changes:</b>")
                    for change, description in seasonal_changes.items():
                        response.append(f"    - {change.replace('_', ' ').title()}: {description}")

            # Atmospheric Pressure - Comprehensive data
            pressure = climate_profile.get('atmospheric_pressure', {})
            if pressure:
                response.append("\n🌬️ <b>Atmospheric Pressure</b>")
                response.append(f"  • <b>Annual average:</b> {pressure.get('annual_average', 'N/A')}")
                
                # Variations
                variations = pressure.get('variations', {})
                if variations:
                    response.append("  • <b>Variations:</b>")
                    for type_var, value in variations.items():
                        response.append(f"    - {type_var.replace('_', ' ').title()}: {value}")
                
                if 'weather_system_effects' in pressure:
                    response.append(f"  • <b>Weather system effects:</b> {pressure['weather_system_effects']}")

            # Sunshine and Solar Radiation - Comprehensive data
            sunshine = climate_profile.get('sunshine_solar_radiation', {})
            if sunshine:
                response.append("\n☀️ <b>Sunshine and Solar Radiation</b>")
                
                if 'sunny_days' in sunshine:
                    response.append(f"  • <b>Sunny days:</b> {sunshine['sunny_days']}")
                if 'cloudy_days' in sunshine:
                    response.append(f"  • <b>Cloudy days:</b> {sunshine['cloudy_days']}")
                
                # Solar radiation
                solar = sunshine.get('solar_radiation', {})
                if solar:
                    response.append("  • <b>Solar radiation:</b>")
                    response.append(f"    - Annual average: {solar.get('annual_average', 'N/A')}")
                    response.append(f"    - Summer peak: {solar.get('summer_peak', 'N/A')}")
                    response.append(f"    - Winter minimum: {solar.get('winter_minimum', 'N/A')}")
                
                # Sunlight intensity
                intensity = sunshine.get('sunlight_intensity', {})
                if intensity:
                    response.append("  • <b>Sunlight intensity:</b>")
                    if 'peak_hours' in intensity:
                        response.append(f"    - Peak hours: {intensity['peak_hours']}")
                    if 'uv_index' in intensity:
                        response.append(f"    - UV index: {intensity['uv_index']}")
                    if 'shading_factor' in intensity:
                        response.append(f"    - Shading factor: {intensity['shading_factor']}")

            # Cloud Cover - Comprehensive data
            clouds = climate_profile.get('cloud_cover', {})
            if clouds:
                response.append("\n☁️ <b>Cloud Cover</b>")
                response.append(f"  • <b>Annual average:</b> {clouds.get('annual_average', 'N/A')}")
                
                # Seasonal coverage
                seasonal_coverage = clouds.get('seasonal_coverage', {})
                if seasonal_coverage:
                    response.append("  • <b>Seasonal coverage:</b>")
                    for season, coverage in seasonal_coverage.items():
                        response.append(f"    - {season.replace('_', ' ').title()}: {coverage}")
                
                # Cloud types
                cloud_types = clouds.get('cloud_types', {})
                if cloud_types:
                    response.append("  • <b>Cloud types:</b>")
                    for cloud_type, frequency in cloud_types.items():
                        response.append(f"    - {cloud_type.title()}: {frequency}")
                
                if 'thickness' in clouds:
                    response.append(f"  • <b>Thickness:</b> {clouds['thickness']}")

            # Evaporation and Transpiration - Comprehensive data
            evap = climate_profile.get('evaporation_transpiration', {})
            if evap:
                response.append("\n💨 <b>Evaporation and Transpiration</b>")
                response.append(f"  • <b>Annual evaporation:</b> {evap.get('annual_evaporation', 'N/A')}")
                
                # Seasonal rates
                seasonal_rates = evap.get('seasonal_rates', {})
                if seasonal_rates:
                    response.append("  • <b>Seasonal rates:</b>")
                    for season, rate in seasonal_rates.items():
                        response.append(f"    - {season.replace('_', ' ').title()}: {rate}")
                
                # Transpiration
                transpiration = evap.get('transpiration', {})
                if transpiration:
                    response.append("  • <b>Transpiration:</b>")
                    if 'vegetation_impact' in transpiration:
                        response.append(f"    - Vegetation impact: {transpiration['vegetation_impact']}")
                    if 'water_cycle' in transpiration:
                        response.append(f"    - Water cycle: {transpiration['water_cycle']}")

            # Storms and Extreme Weather - Comprehensive data
            storms = climate_profile.get('storms_extreme_weather', {})
            if storms:
                response.append("\n⚡ <b>Storms and Extreme Weather</b>")
                
                # Heat waves
                heat_waves = storms.get('heat_waves', {})
                if heat_waves:
                    response.append("  • <b>Heat waves:</b>")
                    response.append(f"    - Frequency: {heat_waves.get('frequency', 'N/A')}")
                    response.append(f"    - Duration: {heat_waves.get('duration', 'N/A')}")
                    response.append(f"    - Peak temperature: {heat_waves.get('peak_temperature', 'N/A')}")
                
                # Dust storms
                dust_storms = storms.get('dust_storms', {})
                if dust_storms:
                    response.append("  • <b>Dust storms:</b>")
                    response.append(f"    - Frequency: {dust_storms.get('frequency', 'N/A')}")
                    response.append(f"    - Peak season: {dust_storms.get('peak_season', 'N/A')}")
                    response.append(f"    - Intensity: {dust_storms.get('intensity', 'N/A')}")
                
                # Droughts
                droughts = storms.get('droughts', {})
                if droughts:
                    response.append("  • <b>Droughts:</b>")
                    response.append(f"    - Frequency: {droughts.get('frequency', 'N/A')}")
                    response.append(f"    - Duration: {droughts.get('duration', 'N/A')}")
                    response.append(f"    - Severity: {droughts.get('severity', 'N/A')}")
                
                # Thunderstorms
                thunderstorms = storms.get('thunderstorms', {})
                if thunderstorms:
                    response.append("  • <b>Thunderstorms:</b>")
                    response.append(f"    - Frequency: {thunderstorms.get('frequency', 'N/A')}")
                    response.append(f"    - Peak season: {thunderstorms.get('peak_season', 'N/A')}")
                    if 'lightning' in thunderstorms:
                        response.append(f"    - Lightning: {thunderstorms['lightning']}")

            # Seasonal Patterns - Comprehensive data
            seasons = climate_profile.get('seasonal_patterns', {})
            if seasons:
                response.append("\n🌱 <b>Seasonal Patterns</b>")
                
                for season_name, season_data in seasons.items():
                    if isinstance(season_data, dict):
                        response.append(f"  • <b>{season_name.title()}:</b>")
                        response.append(f"    - Duration: {season_data.get('duration', 'N/A')}")
                        response.append(f"    - Characteristics: {season_data.get('characteristics', 'N/A')}")
                        if 'temperature_range' in season_data:
                            response.append(f"    - Temperature range: {season_data['temperature_range']}")
                        if 'rainfall' in season_data:
                            response.append(f"    - Rainfall: {season_data['rainfall']}")

            response.append("\n------------------------------")
            return "\n".join(response)
        except Exception as e:
            logger.error(f"Error formatting climate profile: {str(e)}")
            return "Sorry, I had trouble formatting the climate information. Please try asking about specific aspects like temperature or rainfall."

    def get_welcome_message(self) -> str:
        """Get welcome message for new chat sessions."""
        return """Welcome to Green AI Climate Assistant! 👋

I can help you with:
• Information about the Green AI project and team
• Climate data for all districts in Sindh
• Environmental issues and adaptation measures
• Research findings and technical details
• SDG goals and future plans

Try asking:
• "What is Green AI?"
• "Tell me about the team"
• "What's happening in Thatta?"
• "How can we adapt to climate change?"
• "What are the future plans?"

Just ask your question and I'll help you find the information you need!"""

    def get_default_response(self) -> str:
        """Get default response for empty or unrecognized queries."""
        return """I can help you with various topics:

• Project Information: Ask about Green AI, the team, or SDG goals
• Climate Data: Get information about any district in Sindh
• Research Findings: Learn about our climate research
• Adaptation Measures: Discover climate solutions
• Technical Details: Understand our capabilities

Try asking a specific question about any of these topics!"""

    def get_response(self, query: str) -> str:
        """Generate a focused response to the user query."""
        try:
            # Clean and normalize the query
            query = query.strip().lower()
            
            # Handle empty queries with minimal prompt
            if not query:
                return "Hello! Please ask me a specific question about climate, weather, water resources, or agriculture in any district of Sindh."

            # Find district first since many queries are district-specific
            district = self.find_district(query)
            
            # Handle district-specific queries with focused responses
            if district:
                if self.is_water_query(query):
                    return self.get_water_resources_info(district)
                elif self.is_agriculture_query(query):
                    return self.get_agriculture_info(district)
                elif self.is_weather_query(query):
                    return self.get_weather_info(district)
                elif self.is_climate_query(query):
                    return self.get_climate_info(district)
                else:
                    # Only return overview if query is general about the district
                    return self.get_district_overview(district)

            # Handle specific project-related queries with direct responses
            if self.is_team_query(query):
                return self.get_team_info()
            elif self.is_about_query(query):
                return self.get_about_info()
            elif self.is_sdg_query(query):
                return self.get_sdg_info()
            elif self.is_future_query(query):
                return self.get_future_plans()
            elif self.is_adaptation_query(query):
                return self.get_adaptation_info()
            elif self.is_research_query(query):
                return self.get_research_info()
            elif self.is_technical_query(query):
                return self.get_technical_info()
            elif self.is_sensor_query(query):
                # Extract specific sensor type from query
                sensor_type = None
                for sensor_type_keyword in ["temperature", "rainfall", "humidity", "wind", "air quality", "water quality"]:
                    if sensor_type_keyword in query:
                        sensor_type = sensor_type_keyword
                        break
                return self.get_sensor_info(sensor_type)

            # If we reach here, return a general climate response
            return self.generate_general_climate_response(query)
        except Exception as e:
            logger.exception("Error generating response")
            return f"Sorry, I ran into an error processing your question: {str(e)}"

    def get_capabilities(self) -> str:
        """Return information about chatbot capabilities."""
        return """I can help you with:
• Real-time weather data for all districts in Sindh
• Climate change trends and impacts
• Water resource information
• Agricultural data and recommendations
• Environmental issues and solutions
• District-specific climate analysis

Just ask me about any district in Sindh!"""

    def is_water_query(self, query: str) -> bool:
        """Check if query is about water resources."""
        water_keywords = {
            'water', 'river', 'rainfall', 'precipitation', 'irrigation',
            'groundwater', 'aquifer', 'dam', 'reservoir', 'canal',
            'drinking water', 'water quality', 'water supply', 'water resources',
            'water management', 'flood', 'drought'
        }
        return any(keyword in query.lower() for keyword in water_keywords)

    def is_climate_query(self, query: str) -> bool:
        """Check if query is about climate patterns."""
        climate_keywords = {
            'climate', 'temperature', 'rainfall pattern', 'seasonal',
            'monsoon', 'weather pattern', 'climate change', 'global warming',
            'extreme weather', 'heat wave', 'cold wave', 'climate trend'
        }
        return any(keyword in query.lower() for keyword in climate_keywords)

    def is_agriculture_query(self, query: str) -> bool:
        """Check if query is about agriculture."""
        agriculture_keywords = {
            'agriculture', 'farming', 'crop', 'harvest', 'yield',
            'soil', 'irrigation', 'cultivation', 'livestock',
            'agricultural', 'farmer', 'farm', 'growing season'
        }
        return any(keyword in query.lower() for keyword in agriculture_keywords)

    def is_weather_query(self, query: str) -> bool:
        """Check if query is about current weather."""
        weather_keywords = {
            'weather', 'temperature', 'humidity', 'wind',
            'rain', 'sunny', 'cloudy', 'forecast', 'today',
            'current', 'now', 'present'
        }
        return any(keyword in query.lower() for keyword in weather_keywords)

    def get_district_overview(self, district: str) -> str:
        """Get comprehensive overview of a district."""
        try:
            climate_info = self.climate_data.get(district, {})
            if not climate_info:
                return f"I don't have detailed information about {district} at the moment."
            
            response = [f"Overview of {district}:"]
            
            # Climate information
            if 'climate' in climate_info:
                response.append(f"\nClimate: {climate_info['climate']}")
            
            # Rainfall information
            if 'rainfall' in climate_info and 'annual' in climate_info['rainfall']:
                response.append(f"Annual Rainfall: {climate_info['rainfall']['annual']}")
            
            # Challenges
            if 'challenges' in climate_info:
                response.append("\nKey Environmental Challenges:")
                for challenge in climate_info['challenges']:
                    response.append(f"• {challenge['type']} ({challenge['severity']})")
            
            # Water resources (optional)
            water_key = self._water_key(district)
            if water_key:
                water_status = WATER_AVAILABILITY.get(water_key)
                if water_status is not None:
                    stress_category = get_water_stress_category(water_status)
                    response.append(f"\nWater Resources:")
                    response.append(f"• Availability: {water_status} m³ per capita")
                    response.append(f"• Status: {stress_category}")
            
            # Add recommendations
            response.append("\nRecommended Focus Areas:")
            response.append("• Water conservation and management")
            response.append("• Sustainable agriculture practices")
            response.append("• Climate change adaptation")
            
            return "\n".join(response)
        except Exception as e:
            return f"I encountered an error while retrieving information about {district}: {str(e)}"

    def get_water_resources_info(self, district: str) -> str:
        """Get detailed water resources information for a district."""
        try:
            water_key = self._water_key(district)
            if not water_key:
                return f"I don't have water resources data for {district}."
            
            water_status = WATER_AVAILABILITY.get(water_key)
            stress_category = get_water_stress_category(water_status) if water_status is not None else "Unknown"
            sources = WATER_SOURCES.get(water_key, {})
            quality = WATER_QUALITY_ISSUES.get(water_key, {})
            projection = WATER_PROJECTIONS.get(water_key, 0)
            
            response = [f"Water Resources Analysis for {district}:"]
            
            # Current status
            response.append(f"\nCurrent Status:")
            response.append(f"• Water Availability: {water_status} m³ per capita")
            response.append(f"• Stress Level: {stress_category}")
            
            # Water sources
            if sources:
                response.append("\nWater Sources:")
                for source, percentage in sources.items():
                    if percentage > 0:
                        response.append(f"• {source}: {percentage}%")
            
            # Quality issues
            if quality:
                response.append("\nWater Quality Concerns:")
                for issue, severity in quality.items():
                    if severity >= 7:
                        response.append(f"• {issue}: High Risk (Level {severity}/10)")
                    elif severity >= 4:
                        response.append(f"• {issue}: Moderate Risk (Level {severity}/10)")
            
            # Future projections
            if projection:
                response.append(f"\nFuture Outlook:")
                response.append(f"• Projected change by 2050: {projection}%")
            
            return "\n".join(response)
        except Exception as e:
            return f"I encountered an error while retrieving water resources information: {str(e)}"

    def _water_key(self, district: str) -> Optional[str]:
        """Map various district name forms to water resource keys (title-cased)."""
        try:
            if not WATER_AVAILABILITY:
                return None
            name = (district or "").strip().lower().replace('_', ' ')
            # Collapse Karachi divisions to Karachi
            if name.startswith('karachi'):
                key = 'Karachi'
            elif name == 'mirpurkhas' or name == 'mirpur khas':
                key = 'Mirpur Khas'
            else:
                key = name.title()
            return key if key in WATER_AVAILABILITY else None
        except Exception:
            return None

    def get_climate_info(self, district: str) -> str:
        """Get detailed climate information for a district using real-time sensor data."""
        try:
            # First, try to get real-time sensor data
            try:
                from sensors.district_sensor_manager import DistrictSensorManager
                sensor_manager = DistrictSensorManager()
                
                # Get real-time temperature and humidity data
                # Handle Karachi divisions - if user asks for "karachi", use "karachi central" as default
                sensor_district = district.lower()
                if sensor_district == 'karachi':
                    sensor_district = 'karachi central'
                
                temp_humidity_data = sensor_manager.get_sensor_data(sensor_district, 'temp_humidity')
                air_quality_data = sensor_manager.get_sensor_data(sensor_district, 'air_quality')
                
                # Check if we have at least temperature/humidity data
                if temp_humidity_data:
                    response = [f"🌡️ <b>Real-Time Climate Data for {district.title()}</b>"]
                    
                    # Current temperature and humidity
                    if 'temperature' in temp_humidity_data:
                        response.append(f"\n<b>Temperature:</b> {temp_humidity_data['temperature']}°C")
                    if 'humidity' in temp_humidity_data:
                        response.append(f"<b>Humidity:</b> {temp_humidity_data['humidity']}%")
                    
                    # Air quality information (only if available)
                    if air_quality_data and 'aqi' in air_quality_data:
                        aqi = air_quality_data['aqi']
                        aqi_status = "Good" if aqi <= 50 else "Moderate" if aqi <= 100 else "Unhealthy for Sensitive Groups" if aqi <= 150 else "Unhealthy"
                        response.append(f"<b>Air Quality Index:</b> {aqi} ({aqi_status})")
                    
                    if air_quality_data and 'pm25' in air_quality_data:
                        response.append(f"<b>PM2.5:</b> {air_quality_data['pm25']} µg/m³")
                    if air_quality_data and 'co2' in air_quality_data:
                        response.append(f"<b>CO2:</b> {air_quality_data['co2']} ppm")
                    
                    response.append(f"\n<b>Last Updated:</b> {self._format_last_updated(temp_humidity_data.get('timestamp', 'N/A'))}")
                    
                    # Add historical climate profile if available
                    climate_info = self._get_historical_climate_data(district)
                    if climate_info:
                        response.append(f"\n\n📊 <b>Historical Climate Profile:</b>")
                        response.append(climate_info)
                    
                    return "\n".join(response)
                    
            except Exception as e:
                # If sensor data fails, fall back to historical data
                pass
            
            # Fallback to historical climate data
            return self._get_historical_climate_data(district)
            
        except Exception as e:
            return f"I encountered an error while retrieving climate information: {str(e)}"
    
    def _get_historical_climate_data(self, district: str) -> str:
        """Get historical climate data for a district."""
        try:
            # Try multiple lookup strategies for district names
            climate_info = None
            
            # Strategy 1: Direct lookup
            climate_info = self.climate_data.get(district.lower(), {})
            
            # Strategy 2: If empty, try normalized lookup
            if not climate_info:
                normalized = self._normalize_name(district)
                if normalized in self.climate_key_by_normalized:
                    climate_key = self.climate_key_by_normalized[normalized]
                    climate_info = self.climate_data.get(climate_key, {})
            
            # Strategy 3: If still empty, try underscore variant
            if not climate_info:
                underscore_variant = district.lower().replace(' ', '_')
                climate_info = self.climate_data.get(underscore_variant, {})
            
            # Strategy 4: If still empty, try space variant
            if not climate_info:
                space_variant = district.lower().replace('_', ' ')
                climate_info = self.climate_data.get(space_variant, {})
            
            if not climate_info:
                return f"I don't have historical climate data for {district}."
            
            # Many entries use a nested 'climate_profile'; prefer that format
            if 'climate_profile' in climate_info and isinstance(climate_info['climate_profile'], dict):
                return f"Climate Analysis for {district.title()}:\n\n" + self.format_climate_profile(climate_info['climate_profile'])

            # Fallback: handle older flat structures
            response = [f"Climate Analysis for {district.title()}:"]

            # Basic climate info
            if 'climate' in climate_info:
                response.append(f"\nClimate Type: {climate_info['climate']}")

            # Temperature information
            if 'temperature' in climate_info:
                temp = climate_info['temperature']
                response.append("\nTemperature Patterns:")
                if 'average' in temp:
                    response.append(f"• Annual Average: {temp['average']}°C")
                if 'summer_max' in temp:
                    response.append(f"• Summer Maximum: {temp['summer_max']}°C")
                if 'winter_min' in temp:
                    response.append(f"• Winter Minimum: {temp['winter_min']}°C")
                if 'trend' in temp:
                    response.append(f"• Temperature Trend: {temp['trend']}")

            # Rainfall patterns
            if 'rainfall' in climate_info:
                rainfall = climate_info['rainfall']
                response.append("\nRainfall Patterns:")
                if 'annual' in rainfall:
                    response.append(f"• Annual Average: {rainfall['annual']}")
                if 'monsoon_contribution' in rainfall:
                    response.append(f"• Monsoon Contribution: {rainfall['monsoon_contribution']}")
                if 'rainy_days' in rainfall:
                    response.append(f"• Average Rainy Days: {rainfall['rainy_days']}")
                if 'trend' in rainfall:
                    response.append(f"• Rainfall Trend: {rainfall['trend']}")

            # Humidity information
            if 'humidity' in climate_info:
                humidity = climate_info['humidity']
                response.append("\nHumidity Levels:")
                if 'annual_average' in humidity:
                    response.append(f"• Annual Average: {humidity['annual_average']}")
                if 'summer' in humidity:
                    response.append(f"• Summer: {humidity['summer']}")
                if 'winter' in humidity:
                    response.append(f"• Winter: {humidity['winter']}")

            # Wind information
            if 'wind' in climate_info:
                wind = climate_info['wind']
                response.append("\nWind Conditions:")
                if 'average_speed' in wind:
                    response.append(f"• Average Speed: {wind['average_speed']}")
                if 'prevailing_direction' in wind:
                    response.append(f"• Prevailing Direction: {wind['prevailing_direction']}")

            # Climate challenges
            if 'challenges' in climate_info:
                climate_challenges = [c for c in climate_info['challenges'] 
                                   if 'climate' in c['type'].lower()]
                if climate_challenges:
                    response.append("\nClimate-related Challenges:")
                    for challenge in climate_challenges:
                        response.append(f"• {challenge['type']} ({challenge['severity']})")

            return "\n".join(response)
            
        except Exception as e:
            logger.error(f"Error getting climate information: {str(e)}")
            return f"I encountered an error while retrieving climate information for {district}."

    def get_agriculture_info(self, district: str) -> str:
        """Get agricultural information for a district."""
        try:
            district_info = self.climate_data.get(district.lower(), {})
            if not district_info:
                return f"Agricultural data is not available for {district}."
            
            response = []
            
            # Only include relevant agricultural data
            if 'agriculture' in district_info:
                ag_info = district_info['agriculture']
                if 'major_crops' in ag_info:
                    response.append(f"Major Crops: {', '.join(ag_info['major_crops'])}")
                if 'growing_season' in ag_info:
                    response.append(f"Growing Season: {ag_info['growing_season']}")
                if 'soil_type' in ag_info:
                    response.append(f"Soil Type: {ag_info['soil_type']}")

            # Add water availability if critical for agriculture
            if district in WATER_AVAILABILITY:
                water_status = WATER_AVAILABILITY[district]
                if water_status < 1000:  # Only show if there's water stress
                    response.append(f"Water Availability: {water_status} m³ per capita (Water Stressed)")

            # Only show severe agricultural challenges
            if 'challenges' in district_info:
                ag_challenges = [c for c in district_info['challenges'] 
                               if any(k in c['type'].lower() 
                                    for k in ['agriculture', 'farming', 'crop', 'soil'])
                               and c['severity'] in ['High', 'Critical']]
                if ag_challenges:
                    challenges = [f"{c['type']} ({c['severity']})" for c in ag_challenges]
                    response.append(f"Major Challenges: {', '.join(challenges)}")
            
            if not response:
                return f"Detailed agricultural information is not available for {district}."
                
            return " | ".join(response)
            
        except Exception as e:
            logger.error(f"Error getting agricultural information: {str(e)}")
            return f"Unable to retrieve agricultural information for {district}."

    def get_weather_info(self, district: str) -> str:
        """Get real-time weather information for a district using sensor data."""
        try:
            # First, try to get real-time sensor data
            try:
                from sensors.district_sensor_manager import DistrictSensorManager
                sensor_manager = DistrictSensorManager()
                
                # Get real-time temperature and humidity data
                # Handle Karachi divisions - if user asks for "karachi", use "karachi central" as default
                sensor_district = district.lower()
                if sensor_district == 'karachi':
                    sensor_district = 'karachi central'
                
                temp_humidity_data = sensor_manager.get_sensor_data(sensor_district, 'temp_humidity')
                air_quality_data = sensor_manager.get_sensor_data(sensor_district, 'air_quality')
                
                # Check if we have at least temperature/humidity data
                if temp_humidity_data:
                    response = [f"🌤️ <b>Real-Time Weather Data for {district.title()}</b>"]
                    
                    # Current temperature and humidity
                    if 'temperature' in temp_humidity_data:
                        response.append(f"\n<b>Temperature:</b> {temp_humidity_data['temperature']}°C")
                    if 'humidity' in temp_humidity_data:
                        response.append(f"<b>Humidity:</b> {temp_humidity_data['humidity']}%")
                    
                    # Air quality information (only if available)
                    if air_quality_data and 'aqi' in air_quality_data:
                        aqi = air_quality_data['aqi']
                        aqi_status = "Good" if aqi <= 50 else "Moderate" if aqi <= 100 else "Unhealthy for Sensitive Groups" if aqi <= 150 else "Unhealthy"
                        response.append(f"<b>Air Quality:</b> {aqi_status} (AQI: {aqi})")
                    
                    response.append(f"\n<b>Last Updated:</b> {self._format_last_updated(temp_humidity_data.get('timestamp', 'N/A'))}")
                    
                    return "\n".join(response)
                    
            except Exception as e:
                # If sensor data fails, fall back to historical data
                pass
            
            # Fallback to historical weather data
            district_info = self.climate_data.get(district.lower(), {})
            if not district_info:
                return f"Weather data is not available for {district}."
            
            # If we have real-time data, only show that
            if 'current_weather' in district_info:
                current = district_info['current_weather']
                response = []
                if 'temperature' in current:
                    response.append(f"Temperature: {current['temperature']}°C")
                if 'humidity' in current:
                    response.append(f"Humidity: {current['humidity']}%")
                if 'wind_speed' in current:
                    response.append(f"Wind Speed: {current['wind_speed']}")
                if 'conditions' in current:
                    response.append(f"Conditions: {current['conditions']}")
                return " | ".join(response)
            
            # If no real-time data, show typical patterns briefly
            response = []
            if 'temperature' in district_info:
                temp = district_info['temperature']
                if 'average' in temp:
                    response.append(f"Typical Temperature: {temp['average']}°C")
                if 'summer_max' in temp and 'winter_min' in temp:
                    response.append(f"Range: {temp['winter_min']}°C to {temp['summer_max']}°C")
            
            if not response:
                return f"Weather information is not available for {district}."
                
            response.append("Note: This is typical weather data, not real-time information.")
            return " | ".join(response)
            
        except Exception as e:
            logger.error(f"Error getting weather information: {str(e)}")
            return f"Unable to retrieve weather information for {district}."

    def _format_last_updated(self, timestamp: str) -> str:
        """Format the last updated timestamp in a user-friendly way."""
        try:
            if not timestamp or timestamp == 'N/A':
                return 'N/A'
            # Try to parse the timestamp
            dt = dateutil.parser.parse(timestamp)
            # If the timestamp is naive, treat as local time
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=pytz.UTC)
            # Format: August 19, 2025 at 09:45 AM
            formatted = dt.strftime('%B %d, %Y at %I:%M %p')
            return f'🕒 {formatted}'
        except Exception:
            return timestamp

    # =====================
    # Audience-aware helpers (non-intrusive)
    # =====================
    def _infer_audience(self, original_query: str) -> str:
        """Infer audience from the user's original query. Returns one of: default, community, ngo, researcher.
        This is heuristic-only and keeps default behavior when no cues are found."""
        q = original_query.lower()
        NGO_CUES = [
            "ngo", "organization", "org", "donor", "grant", "proposal", "3w", "who what where",
            "beneficiary", "targeting", "distribution", "shelter", "coordination", "cluster", "m&e", "monitoring"
        ]
        RESEARCH_CUES = [
            "research", "dataset", "csv", "api", "download", "method", "methodology", "uncertainty",
            "statistical", "index", "indices", "spi", "spei", "time series", "correlation", "regression"
        ]
        COMMUNITY_CUES = [
            "tips", "advice", "what should i do", "what to do", "what should", "household", "households",
            "family", "families", "people", "locals", "fisher", "help me", "urdu", "sindhi",
            "local people", "community"
        ]
        if any(k in q for k in NGO_CUES):
            return "ngo"
        if any(k in q for k in RESEARCH_CUES):
            return "researcher"
        if any(k in q for k in COMMUNITY_CUES):
            return "community"
        return "default"

    def _format_for_audience(self, base_text: str, audience: str, district: Optional[str] = None) -> str:
        """Return base_text unchanged for default; otherwise add a concise role-suited tail section.
        Keeps original content intact to avoid changing current behavior."""
        if audience == "default":
            return base_text
        suffix_lines = self._localized_suffix(audience)
        try:
            return base_text + "\n" + "\n".join(suffix_lines)
        except Exception:
            return base_text

    def get_role_aware_response(self, query: str) -> str:
        """Wrapper that preserves existing responses but adds role-suited guidance when the query clearly indicates an audience."""
        try:
            # Keep original text for decision-making
            original_query = query
            # Audience & hazard detection first (for action queries)
            selected = self._get_selected_audience()
            inferred = self._infer_audience(original_query)
            audience = selected or inferred
            hazard = self._hazard_from_query(original_query)
            if audience in ("community", "ngo") and hazard and self._has_action_intent(original_query):
                district = None
                try:
                    district = self.find_district(original_query.lower())
                except Exception:
                    pass
                if audience == "ngo":
                    base = self._ngo_hazard_guidance(district or "your area", hazard)
                else:
                    base = self._community_hazard_guidance(district or "your area", hazard)
                return base
            # Researcher extremes: short, focused output without unrelated water stats
            if audience == "researcher":
                ql = original_query.lower()
                if ("extreme" in ql or "r95" in ql or "heavy rain" in ql or "rainfall extremes" in ql):
                    district = None
                    try:
                        district = self.find_district(original_query.lower())
                    except Exception:
                        pass
                    snippet = self._researcher_extremes_snippet(district or "")
                    if snippet:
                        return (f"Rainfall extremes context for {district.replace('_',' ').title() if district else 'district'}:" + snippet)
            # Generate base response using existing logic
            base = self.get_response(query)
            # Try to infer a district only for potential future use
            district = None
            try:
                district = self.find_district(original_query.lower())
            except Exception:
                pass
            audience = audience or self._infer_audience(original_query)
            # Researcher: add rainfall extremes/methods snippet if asked
            if audience == "researcher":
                ql = original_query.lower()
                if district and ("extreme" in ql or "r95" in ql or "heavy rain" in ql or "rainfall extremes" in ql):
                    base = base + self._researcher_extremes_snippet(district)
            if audience == "ngo" and district:
                try:
                    brief = self.get_ngo_district_brief(district)
                    if brief:
                        base = brief + "\n\n" + base
                except Exception:
                    pass
            return self._format_for_audience(base, audience, district)
        except Exception:
            # Fallback to original behavior
            return self.get_response(query)

    def _get_selected_audience(self) -> Optional[str]:
        """Map UI role selection to internal audience labels; returns None for General."""
        try:
            label = st.session_state.get("chat_role_label")
            if not label or label == "General":
                return None
            mapping = {
                "Local people": "community",
                "Researchers": "researcher",
                "NGOs": "ngo",
            }
            return mapping.get(label, None)
        except Exception:
            return None

    def _get_language(self) -> str:
        """Return current UI language id from session_state if available."""
        try:
            sel = self._get_selected_audience()
            # Local people explicit chat language (Urdu/Sindhi)
            if sel == "community" and st.session_state.get("chat_local_lang") in ("urdu", "sindhi"):
                return st.session_state.get("chat_local_lang")
            # Otherwise, use global language as-is (Researchers remain default language)
            return st.session_state.get("language", "english")
        except Exception:
            return "english"

    def _get_ngo_language(self) -> str:
        """NGOs default to Urdu unless global language is explicitly Sindhi."""
        try:
            lang = st.session_state.get("language", "english").lower()
            return "sindhi" if lang == "sindhi" else "urdu"
        except Exception:
            return "urdu"

    def get_ngo_district_brief(self, district: Optional[str]) -> str:
        """Return a concise NGO operational brief for the district using role-specific data, if available."""
        try:
            if not district:
                return ""
            # Normalize to display form
            dname = district.replace('_', ' ').title()
            brief = _get_ngo_brief(dname, "english")
            return brief or ""
        except Exception:
            return ""

    def _localized_suffix(self, audience: str) -> List[str]:
        """Return audience tail lines localized to Urdu when selected; default English otherwise."""
        lang = self._get_language()
        if lang == "sindhi":
            if audience == "community":
                return [
                    "\n\nمقامي ماڻهن لاءِ:",
                    "- محفوظ پاڻي پيئو، ڏهين کان ڇوڏن تائين سج کان بچو، بزرگن/ٻارن جو خيال رکو",
                    "- سيلاب ۾: ويجهي پناهگاه ڄاڻي وٺو؛ قيمتي شيون مٿي رکو؛ دستاويز سڪي ۽ محفوظ رکو",
                    "- هارين لاءِ: صبح/شام آبپاشي، ملچ، آفتن جي خبردارين تي نظر"
                ]
            if audience == "ngo":
                return [
                    "\n\nاين جي اوز لاءِ:",
                    "- يو سي هٽ اسپاٽن/نابالغ آبادي جي ميپنگ ۽ ترجيح",
                    "- PDMA/صحت/مقامي حڪومت سان رابطن جي هم آهنگي (3W)",
                    "- پاڻي/ORS، هائجين، ٽارپ/رسی، ٽارچ/پاور بينڪ اڳواٽ رکڻ",
                    "- پناهگاهن/رسائي روٽن جي تصديق؛ شڪايت/شموليت اشارن تي عمل"
                ]
            if audience == "researcher":
                return [
                    "\n\nمحققن لاءِ:",
                    "- ڊيٽا سيٽ/طريقا حوالا؛ غير يقيني رپورٽ؛ ورجائتي مرحلا",
                    "- SPI/SPEI، هيٽ انڊيڪس، ۽ R95p جهڙا اشارا استعمال ڪريو",
                    "- جتي ممڪن CSV/API مهيا ڪريو"
                ]
        if lang == "urdu":
            if audience == "community":
                return [
                    "\n\nمقامی لوگوں کے لیے:",
                    "- صاف پانی پیئیں، دوپہر کی دھوپ سے بچیں، بزرگوں/بچوں کا خیال رکھیں",
                    "- سیلاب کی صورت میں: قریبی پناہ گاہ معلوم کریں؛ قیمتی اشیاء اونچی جگہ رکھیں؛ دستاویزات محفوظ کریں",
                    "- کاشتکاروں کے لیے: پانی صبح/شام دیں؛ ملچ کریں؛ کیڑوں کی وارننگ دیکھیں",
                ]
            if audience == "ngo":
                return [
                    "\n\nاین جی اوز کے لیے:",
                    "- حساس علاقوں کو ترجیح دیں؛ PDMA/صحت/سڑکوں سے رابطہ کریں",
                    "- پانی/ORS اور سایہ کٹس پہلے سے رکھیں؛ پناہ گاہیں اور رسائی راستے تصدیق کریں",
                    "- سادہ اشاریے ٹریک کریں (رسائی، شمولیت)؛ 3W اپڈیٹس شیئر کریں",
                ]
            if audience == "researcher":
                return [
                    "\n\nمحققین کے لیے:",
                    "- ڈیٹاسیٹس/طریقۂ کار حوالہ دیں؛ غیر یقینیّت رپورٹ کریں؛ قابلِ تکرار مراحل دیں",
                    "- SPI/SPEI، ہیٹ انڈیکس، اور R95p جیسے اشارئیے استعمال کریں",
                    "- جہاں ممکن ہو CSV/API شیئر کریں",
                ]
        # Default English
        if audience == "community":
            return [
                "\n\nFor local people:",
                "- Drink safe water, avoid noon sun, check elderly/children",
                "- For floods: know nearest shelter; move valuables up; keep documents dry",
                "- For farmers: irrigate early/late; mulch; watch pest alerts",
            ]
        if audience == "ngo":
            return [
                "\n\nFor NGOs:",
                "- Target hotspots by vulnerability; coordinate via PDMA/health/roads",
                "- Preposition water/ORS, shade kits; confirm shelters & access routes",
                "- Track simple KPIs (reach, inclusivity); share 3W updates",
            ]
        if audience == "researcher":
            return [
                "\n\nFor researchers:",
                "- Cite datasets/methods; report uncertainty; provide reproducible steps",
                "- Consider SPI/SPEI, heat indices, extremes (R95p) over district time series",
                "- Share data/plots (CSV/API) where available",
            ]
        return []

    def _researcher_extremes_snippet(self, district: str) -> str:
        """Assemble a short, data-backed snippet for rainfall extremes context and methods."""
        try:
            # Pull what we can from the comprehensive climate data
            info = self._get_historical_climate_data(district)
            # Also try direct structure if available
            c = self.climate_data.get(district.lower(), {}) or self.climate_data.get(district.replace(' ', '_').lower(), {})
            annual_total = None
            rainy_days = None
            thunder_freq = None
            if isinstance(c, dict) and isinstance(c.get('climate_profile'), dict):
                cp = c['climate_profile']
                precip = cp.get('precipitation', {})
                if precip:
                    annual_total = precip.get('annual_total')
                    rainfall = precip.get('rainfall', {})
                    rainy_days = rainfall.get('rainy_days')
                storms = cp.get('storms_extreme_weather', {})
                if storms and isinstance(storms.get('thunderstorms'), dict):
                    thunder_freq = storms['thunderstorms'].get('frequency')
            lang = self._get_language()
            if lang == "sindhi":
                lines = ["\n\nتحقيقي ماپ (مينهن جون انتهائون):"]
                if annual_total:
                    lines.append(f"- ساليانو مينهن: {annual_total}")
                if rainy_days:
                    lines.append(f"- مينهن وارا ڏينهن: {rainy_days}")
                if thunder_freq:
                    lines.append(f"- گج گوڏن جا ڏينهن: {thunder_freq}")
                lines.append("- طريقو: روزاني مينهن مان R95p ۽ R20mm ڳڻيو؛ بنيادي دور 1981–2010؛")
                lines.append("  غايب ڏينهن سنڀاليو؛ رجحان لاءِ Mann–Kendall ۽ Sen's slope استعمال ڪريو.")
            elif lang == "urdu":
                lines = ["\n\nتحقیقی میٹرکس (شدید بارش):"]
                if annual_total:
                    lines.append(f"- سالانہ بارش: {annual_total}")
                if rainy_days:
                    lines.append(f"- بارش والے دن: {rainy_days}")
                if thunder_freq:
                    lines.append(f"- گرج چمک کے واقعات: {thunder_freq}")
                lines.append("- طریقۂ کار: روزانہ بارش سے R95p اور R20mm نکالیں؛ 1981–2010 بیس پیریڈ؛")
                lines.append("  گمشدہ دن ہینڈل کریں؛ رجحان کے لیے Mann–Kendall/Sen's slope ٹیسٹ کریں۔")
            else:
                lines = ["\n\nResearch metrics (rainfall extremes):"]
                if annual_total:
                    lines.append(f"- Annual rainfall: {annual_total}")
                if rainy_days:
                    lines.append(f"- Rainy days: {rainy_days}")
                if thunder_freq:
                    lines.append(f"- Thunderstorms frequency: {thunder_freq}")
                lines.append("- Methods: compute R95p and R20mm from daily rain; base period 1981–2010;")
                lines.append("  handle missing days; trend-test with Mann–Kendall and Sen's slope.")
            return "\n" + "\n".join(lines)
        except Exception:
            return ""

    def _has_action_intent(self, q: str) -> bool:
        ql = (q or "").lower()
        return any(kw in ql for kw in ["what should", "what to do", "how to prepare", "prepare", "checklist", "steps", "do now", "during"])

    def _hazard_from_query(self, q: str) -> Optional[str]:
        ql = (q or "").lower()
        if any(k in ql for k in ["flood", "flooding", "urban flooding", "inundation"]):
            return "flood"
        if any(k in ql for k in ["cyclone", "storm surge", "gale", "hurricane"]):
            return "cyclone"
        if any(k in ql for k in ["heatwave", "heat wave", "extreme heat", "hot weather"]):
            return "heat"
        if any(k in ql for k in ["drought", "dry spell"]):
            return "drought"
        if any(k in ql for k in ["dust storm", "sandstorm", "blowing dust"]):
            return "dust"
        return None

    def _community_hazard_guidance(self, district: str, hazard: str) -> str:
        lang = self._get_language()
        dname = district.title() if district else "Your Area"
        if lang == "urdu":
            if hazard == "flood":
                return (
                    f"خاندان کے لیے شہری سیلاب تیاری ({dname}):\n"
                    "- قریبی پناہ گاہ/محفوظ جگہ پہلے سے معلوم کریں؛ خاندان کا رابطہ نقطہ طے کریں\n"
                    "- اہم دستاویزات/ادویات/نقدی واٹر پروف بیگ میں رکھیں؛ برقی آلات اوپر رکھیں\n"
                    "- نالیاں/گٹر صاف رکھیں؛ گھریلو کچرا بیگ میں باندھیں؛ گاڑی اونچی جگہ کھڑی کریں\n"
                    "- پینے کا پانی محفوظ کریں؛ بنیادی کٹ: ٹارچ، پاور بینک، ORS، فرسٹ ایڈ، خشک خوراک\n"
                    "- سیلاب کے دوران: پانی میں نہ اتریں؛ بجلی کے بکس/تاروں سے دور رہیں؛ مقامی انتباہات پر عمل کریں"
                )
            if hazard == "heat":
                return (
                    f"خاندان کے لیے گرمی کی لہر کے دوران احتیاط ({dname}):\n"
                    "- 11am–4pm میں دھوپ سے بچیں؛ ہلکے رنگ کے ڈھیلے کپڑے پہنیں\n"
                    "- پانی اور ORS پیئیں؛ بزرگوں/بچوں/مزدوروں کی نگرانی کریں\n"
                    "- کمرہ ٹھنڈا رکھیں: ہوا، سایہ، گیلا کپڑا؛ گاڑی بند میں بچوں/بزرگوں کو نہ چھوڑیں\n"
                    "- گرمی کی علامات (چکر، متلی) پر فوراً آرام/پانی دیں اور ضرورت پر طبی امداد لیں"
                )
            if hazard == "cyclone":
                return (
                    f"طوفان/سمندری طغیانی تیاری ({dname}):\n"
                    "- چھت/کھڑکی/دروازے مضبوط کریں؛ ढِلے سامان باندھ دیں\n"
                    "- انخلا راستہ اور قریبی پناہ گاہ معلوم کریں؛ ایندھن/نقدی/خوراک/پانی ذخیرہ کریں\n"
                    "- ماہی گیروں کو سمندر سے دور رہنے کی ہدایت کریں؛ انتباہات پر عمل کریں"
                )
            if hazard == "drought":
                return (
                    f"خشک سالی کے دوران گھریلو اقدامات ({dname}):\n"
                    "- پانی کی بچت: لیک درست کریں، کم بہاؤ نل لگائیں، غسل/لان کو محدود کریں\n"
                    "- پینے کے پانی کی حفاظت: ابالیں/فلٹر کریں؛ ذخیرہ سایہ میں رکھیں\n"
                    "- کسان: صبح/شام آبپاشی، ملچ، کم پانی والی فصلیں اختیار کریں"
                )
            if hazard == "dust":
                return (
                    f"گرد آلود آندھی کے دوران ({dname}):\n"
                    "- گھر کے اندر رہیں؛ N95/ماسک پہنیں؛ آنکھوں کے لیے چشمہ\n"
                    "- گاڑی آہستہ چلائیں؛ کم視یت میں ہیڈلائٹس آن رکھیں\n"
                    "- سانس کی بیماری والے افراد اضافی احتیاط کریں"
                )
        # Default English
        if hazard == "flood":
            return (
                f"Family checklist for urban flooding in {dname}:\n"
                "- Know nearest shelter and a family contact point; keep phones charged\n"
                "- Bag essentials: IDs/meds/cash in waterproof pouch; move appliances/valuables up\n"
                "- Clear drains; bag household waste; park vehicle on higher ground\n"
                "- Store safe drinking water; kit: flashlight, power bank, ORS, first aid, dry food\n"
                "- During flood: avoid walking/driving in water; stay away from power boxes/wires; follow local alerts"
            )
        if hazard == "heat":
            return (
                f"Family checklist for heatwave in {dname}:\n"
                "- Avoid 11am–4pm sun; wear light/loose clothing\n"
                "- Drink water/ORS frequently; check elderly/children/workers\n"
                "- Cool room with shade/airflow/wet cloth; never leave kids/elderly in parked cars\n"
                "- If symptoms (dizziness, nausea), rest, hydrate, seek medical help if needed"
            )
        if hazard == "cyclone":
            return (
                f"Family checklist for cyclone/storm in {dname}:\n"
                "- Secure roof/windows/doors; tie down loose items\n"
                "- Know evacuation route and nearest shelter; stock fuel/cash/food/water\n"
                "- Keep radios/phones for alerts; fishers stay off sea\n"
            )
        if hazard == "drought":
            return (
                f"Family checklist for drought in {dname}:\n"
                "- Save water: fix leaks, low-flow taps, reduce baths/lawn use\n"
                "- Keep drinking water safe: boil/filter; store in shade\n"
                "- Farmers: irrigate early/late, mulch, shift to low-water crops"
            )
        if hazard == "dust":
            return (
                f"Family checklist for dust storms in {dname}:\n"
                "- Stay indoors; wear mask (N95) and eye protection\n"
                "- Drive slowly; headlights on in low visibility\n"
                "- Extra caution for people with respiratory disease"
            )
        return f"Safety checklist for {dname}."

    def _ngo_hazard_guidance(self, district: str, hazard: str) -> str:
        dname = district.title() if district else "Your Area"
        if hazard == "flood":
            return (
                f"NGO Flood Preparedness — {dname}:\n\n"
                "Immediate (48–72h):\n"
                "- Map UC hotspots and verify which evacuation centres and routes are usable. Send simple alert messages and name the centres people should use.\n\n"
                "Coordination:\n"
                "- Assign focal points and check in daily with PDMA, Local Government, Health and Rescue so coverage and gaps are clear in a short 3W.\n\n"
                "Logistics/Kits:\n"
                "- Preposition safe water/ORS, hygiene, basic medical kits, tarps and rope, lights and power banks at hubs close to at‑risk UCs. Arrange boats and trucks with fuel and drivers on standby.\n\n"
                "Inclusion & Protection:\n"
                "- Prioritize children, persons with disabilities and pregnant women. Ensure shelters have separate, well‑lit WASH areas and safe access.\n\n"
                "Reporting:\n"
                "- Publish a short daily sitrep with reach, inclusion and complaints so partners can adjust support quickly."
            )
        if hazard == "cyclone":
            return (
                f"NGO Cyclone Readiness — {dname}:\n\n"
                "Immediate (48–72h):\n"
                "- Open and staff evacuation centres; verify road and boat access. Push alerts (SMS/WhatsApp and loudspeakers) telling coastal hamlets when to move, what to bring and which centres to use.\n\n"
                "Coordination:\n"
                "- Set named focal points with PDMA, Local Government, Health and Roads and share a one‑page 3W showing UC coverage and gaps.\n\n"
                "Logistics/Kits:\n"
                "- Stage water/food/medical kits, tarps and rope; prepare boats and trucks; secure fuel and PPE (rain gear, life jackets, gloves) for teams.\n\n"
                "Inclusion & Protection:\n"
                "- Build a quick registry of vulnerable households and contact them first. Make shelters accessible, lit and safe for women and children.\n\n"
                "Post‑storm:\n"
                "- Start WASH (chlorination, latrine cleaning), do urgent shelter repairs and clear debris; collect complaints and issue a daily sitrep."
            )
        if hazard == "heat":
            return (
                f"NGO Heatwave Response — {dname}:\n\n"
                "Immediate:\n"
                "- Set up cooling spaces, shade and water points, and distribute ORS with simple heat‑health messaging.\n\n"
                "Coordination:\n"
                "- Coordinate with Health and Labour to align alerts and adjust outdoor work schedules to avoid peak heat.\n\n"
                "Protection:\n"
                "- Register elderly, pregnant women and persons with disabilities for proactive checks; ensure rest breaks and shaded areas at worksites."
            )
        if hazard == "drought":
            return (
                f"NGO Drought Actions — {dname}:\n\n"
                "Water supply:\n"
                "- Support the safest mix of water trucking, chlorination and household filters based on tests; protect priority communal sources.\n\n"
                "Livelihoods & Health:\n"
                "- Provide fodder or feed where animals are critical; run dehydration awareness and ORS points at clinics and markets.\n\n"
                "Infrastructure:\n"
                "- Repair handpumps and storage tanks; add shaded storage and basic rainwater harvesting where feasible.\n\n"
                "Targeting & Monitoring:\n"
                "- Target villages with the highest water stress and report weekly on water access, WASH quality and complaints."
            )
        if hazard == "dust":
            return (
                f"NGO Dust‑Storm Response — {dname}:\n\n"
                "Immediate:\n"
                "- Advise people to stay indoors during peak hours; distribute masks where possible and protect those with asthma or COPD first.\n\n"
                "Facilities & Water:\n"
                "- Keep shelters and clinics sealed as much as possible; provide safe water and promote wet cleaning to reduce indoor dust.\n\n"
                "Health & Messaging:\n"
                "- Share short messages on eye and breathing protection and where to seek care; monitor respiratory cases at clinics."
            )
        return f"Preparedness checklist for {dname}."

# Create a global chatbot instance
chatbot = ChatBot() 

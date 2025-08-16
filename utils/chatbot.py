"""
GreenAI Climate Chatbot - Core Implementation
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

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ChatBot:
    """Climate data chatbot core functionality."""
    
    def __init__(self, data_dir: str = 'data/chatbot'):
        self.data_dir = Path(data_dir)
        self.districts = {
            'karachi', 'hyderabad', 'sukkur', 'larkana', 'mirpurkhas', 'nawabshah',
            'thatta', 'badin', 'tharparkar', 'dadu', 'jacobabad', 'kashmore',
            'ghotki', 'khairpur', 'naushahro feroze', 'shaheed benazirabad',
            'sanghar', 'tando allahyar', 'tando muhammad khan', 'matiari'
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
        
    def _initialize_data(self):
        """Initialize all district and climate data including Karachi divisions."""
        try:
            # Import climate data from Python modules
            import data.district_climate_data as climate_data
            import data.district_data as district_data
            
            self.district_data = district_data.district_data
            self.climate_data = climate_data.district_climate_data
            
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
        """Get information about GreenAI."""
        return """GreenAI is an advanced climate information system designed specifically for Sindh, Pakistan. Here's what makes it special:

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

GreenAI aims to empower Sindh's communities with the knowledge they need to address climate challenges and build a sustainable future."""

    def get_team_info(self) -> str:
        """Get information about the project team."""
        return """The GreenAI project is developed by a dedicated team from the Department of Computer Science at University of Sufism and Modern Sciences, Bhitshah:

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
        return """GreenAI primarily addresses SDG 13 - Climate Action, while contributing to several other SDGs:

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
        return """GreenAI's future development plans include:

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
        return """GreenAI Technical Capabilities:

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
        """Check if query is asking about GreenAI."""
        query = query.lower().strip()
        
        # About question patterns
        about_patterns = [
            'what is', 'what does', 'who is', 'tell me about', 'explain',
            'describe', 'how does', 'purpose of', 'goal of', 'objective of'
        ]
        
        # Project references
        project_refs = [
            'greenai', 'green ai', 'the system', 'this system',
            'this assistant', 'this project', 'the project'
        ]
        
        # Check for exact about patterns
        has_about = any(pattern in query for pattern in about_patterns)
        has_project = any(ref in query for ref in project_refs)
        
        # Special case for direct "what is greenai" type questions
        if query.startswith('what') and any(ref in query for ref in ['greenai', 'green ai']):
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
        has_project_ref = any(ref in query for ref in ['greenai', 'green ai', 'project', 'this', 'the'])
        
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

    def find_district(self, query: str) -> Optional[str]:
        """Find district name in query."""
        query = query.lower().strip()
        
        # First check for Karachi divisions with different word orders
        for division in self.karachi_divisions:
            patterns = [
                f"karachi {division}",  # e.g. "karachi central"
                f"{division} karachi",  # e.g. "central karachi"
                division  # e.g. "central" (when context is clearly about Karachi)
            ]
            if any(pattern in query for pattern in patterns):
                return f"karachi {division}"  # Always return in "karachi division" format
        
        # Then check for general districts
        for district in self.districts:
            if district in query:
                # Get the district key from climate data that matches case-insensitively
                district_key = next((k for k in self.climate_data.keys() 
                                   if k.lower() == district.lower()), district)
                return district_key
                
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
        """Format climate profile data into a readable response."""
        try:
            response = []
            
            # Temperature information
            temp = climate_profile.get('temperature', {})
            if temp:
                response.append("Temperature:")
                response.append(f"• Annual average: {temp.get('annual_average', 'N/A')}")
                response.append(f"• Summer maximum: {temp.get('summer_max', 'N/A')}")
                response.append(f"• Winter minimum: {temp.get('winter_min', 'N/A')}")
                if temp.get('trend'):
                    response.append(f"• Trend: {temp['trend']}")
            
            # Rainfall information
            rain = climate_profile.get('rainfall', {})
            if rain:
                response.append("\nRainfall:")
                response.append(f"• Annual average: {rain.get('annual_average', 'N/A')}")
                response.append(f"• Monsoon contribution: {rain.get('monsoon_contribution', 'N/A')}")
                response.append(f"• Rainy days: {rain.get('rainy_days', 'N/A')}")
                if rain.get('trend'):
                    response.append(f"• Trend: {rain['trend']}")
            
            # Humidity information
            humidity = climate_profile.get('humidity', {})
            if humidity:
                response.append("\nHumidity:")
                response.append(f"• Annual average: {humidity.get('annual_average', 'N/A')}")
                response.append(f"• Summer: {humidity.get('summer', 'N/A')}")
                response.append(f"• Winter: {humidity.get('winter', 'N/A')}")
                if humidity.get('trend'):
                    response.append(f"• Trend: {humidity['trend']}")
            
            # Wind information
            wind = climate_profile.get('wind', {})
            if wind:
                response.append("\nWind:")
                response.append(f"• Average speed: {wind.get('average_speed', 'N/A')}")
                if wind.get('prevailing_direction'):
                    response.append(f"• Prevailing direction: {wind['prevailing_direction']}")
            
            return "\n".join(response)
        except Exception as e:
            logger.error(f"Error formatting climate profile: {str(e)}")
            return "Sorry, I had trouble formatting the climate information. Please try asking about specific aspects like temperature or rainfall."

    def get_welcome_message(self) -> str:
        """Get welcome message for new chat sessions."""
        return """Welcome to GreenAI Climate Assistant! 👋

I can help you with:
• Information about the GreenAI project and team
• Climate data for all districts in Sindh
• Environmental issues and adaptation measures
• Research findings and technical details
• SDG goals and future plans

Try asking:
• "What is GreenAI?"
• "Tell me about the team"
• "What's happening in Thatta?"
• "How can we adapt to climate change?"
• "What are the future plans?"

Just ask your question and I'll help you find the information you need!"""

    def get_default_response(self) -> str:
        """Get default response for empty or unrecognized queries."""
        return """I can help you with various topics:

• Project Information: Ask about GreenAI, the team, or SDG goals
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
            elif self.is_research_query(query):
                return self.get_research_info()
            elif self.is_adaptation_query(query):
                return self.get_adaptation_info()
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

            # Handle basic queries
            if any(word in query for word in ["hi", "hello", "hey", "السلام علیکم", "سلام"]):
                return "Hello! How can I help you today?"

            # For unrecognized queries, prompt for specific information
            return "Please ask a specific question about:\n" + \
                   "• A district in Sindh (e.g., 'How is the weather in Karachi?')\n" + \
                   "• Climate data or water resources\n" + \
                   "• Agricultural conditions\n" + \
                   "• Project information"

        except Exception as e:
            logger.error(f"Error generating response: {str(e)}")
            return "I apologize, but I encountered an error. Please try asking your question differently."

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
            
            # Water resources
            if district in WATER_AVAILABILITY:
                water_status = WATER_AVAILABILITY[district]
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
            if district not in WATER_AVAILABILITY:
                return f"I don't have water resources data for {district}."
            
            water_status = WATER_AVAILABILITY[district]
            stress_category = get_water_stress_category(water_status)
            sources = WATER_SOURCES.get(district, {})
            quality = WATER_QUALITY_ISSUES.get(district, {})
            projection = WATER_PROJECTIONS.get(district, 0)
            
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

    def get_climate_info(self, district: str) -> str:
        """Get detailed climate information for a district."""
        try:
            climate_info = self.climate_data.get(district.lower(), {})
            if not climate_info:
                return f"I don't have climate data for {district}."
            
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
        """Get weather information for a district."""
        try:
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

# Create a global chatbot instance
chatbot = ChatBot() 
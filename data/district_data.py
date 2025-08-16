"""
Comprehensive district data for Sindh province.
Includes climate, historical, administrative, and development information.
"""

# Regional classifications with complete district coverage
sindh_regions = {
    "northern_sindh": [
        "sukkur",
        "khairpur",
        "ghotki",
        "kashmore",
        "jacobabad",
        "shikarpur",
        "larkana"
    ],
    "central_sindh": [
        "hyderabad",
        "matiari",
        "dadu",
        "jamshoro",
        "shaheed benazirabad",
        "naushahro feroze",
        "sanghar",
        "tando allahyar",
        "tando muhammad khan"
    ],
    "southern_sindh": [
        "karachi central",
        "karachi east",
        "karachi west",
        "karachi south",
        "karachi malir",
        "karachi korangi",
        "karachi keamari",
        "thatta",
        "sujawal",
        "badin",
        "tharparkar",
        "umerkot",
        "mirpurkhas"
    ]
}

# Regional climate challenges with specific impacts
regional_challenges = {
    "northern_sindh": [
        "Extreme heat waves with temperatures exceeding 50°C",
        "Severe water scarcity affecting agriculture",
        "Progressive desertification and soil degradation",
        "Agricultural stress due to temperature extremes",
        "Frequent dust storms affecting air quality",
        "Groundwater depletion in agricultural areas",
        "River water management challenges"
    ],
    "central_sindh": [
        "Irregular rainfall patterns affecting crop cycles",
        "Complex water management issues",
        "High agricultural vulnerability to climate change",
        "Increasing urban heat island effect",
        "Industrial pollution impacting air and water quality",
        "Soil salinity in agricultural areas",
        "Groundwater contamination from industrial sources"
    ],
    "southern_sindh": [
        "Accelerating sea level rise threatening coastal areas",
        "Severe coastal erosion affecting communities",
        "Regular urban flooding during monsoons",
        "Increasing saltwater intrusion in aquifers",
        "Critical air pollution in urban centers",
        "Mangrove ecosystem degradation",
        "Urban infrastructure stress from climate impacts"
    ]
}

# District-tehsil relationships with administrative details
district_tehsil_mapping = {
    "karachi_central": {
        "tehsils": ["gulberg", "liaquatabad", "north nazimabad", "new karachi", "north karachi"],
        "admin_level": "District",
        "headquarters": "Gulberg"
    },
    "hyderabad": {
        "tehsils": ["hyderabad city", "hyderabad rural", "latifabad", "qasimabad"],
        "admin_level": "District",
        "headquarters": "Hyderabad City"
    },
    # Add all districts with their tehsils...
}

# Comprehensive district climate information
sindh_district_climate_info = {
    "hyderabad": {
        "region": "central_sindh",
        "climate": "Hot desert climate",
        "temperature": {
            "annual_range": "26-40°C average",
            "summer": {
                "max": "45°C",
                "min": "30°C",
                "average": "38°C"
            },
            "winter": {
                "max": "25°C",
                "min": "10°C",
                "average": "18°C"
            }
        },
        "rainfall": {
            "annual": "175mm",
            "monsoon": "80%",
            "winter": "20%",
            "pattern": "Irregular with monsoon concentration"
        },
        "humidity": {
            "annual_average": "50-70%",
            "summer": "65-75%",
            "winter": "40-50%"
        },
        "challenges": [
            {
                "type": "Urban heat island effect",
                "severity": "High",
                "impacts": ["Public health", "Energy consumption", "Water demand"]
            },
            {
                "type": "Water quality issues",
                "severity": "Critical",
                "impacts": ["Drinking water", "Agriculture", "Public health"]
            },
            {
                "type": "Air pollution",
                "severity": "Moderate to High",
                "impacts": ["Respiratory health", "Visibility", "Quality of life"]
            }
        ],
        "sustainability_initiatives": [
            {
                "name": "Urban forestry program",
                "status": "Ongoing",
                "coverage": "City-wide",
                "impact": "Temperature reduction, Air quality improvement"
            },
            {
                "name": "Industrial waste management",
                "status": "In progress",
                "coverage": "Industrial zones",
                "impact": "Water quality, Public health"
            }
        ],
        "future_projections": {
            "2030": {
                "temperature": "+1.5°C",
                "rainfall": "-10%",
                "extreme_events": "Increased frequency"
            },
            "2050": {
                "temperature": "+2.5°C",
                "rainfall": "-15%",
                "extreme_events": "High probability of severe events"
            }
        }
    },
    # Add similar comprehensive data for all districts
}

# Historical climate evolution with detailed tracking
district_historical_evolution = {
    "hyderabad": {
        "temperature_pattern": {
            "1960-1980": "Moderate with occasional extremes",
            "1981-2000": "Gradual warming trend",
            "2001-2020": "Accelerated warming with frequent extremes"
        },
        "rainfall_pattern": {
            "1960-1980": "Regular monsoon patterns",
            "1981-2000": "Increasing variability",
            "2001-2020": "High variability with extended dry periods"
        },
        "extreme_events": [
            {
                "year": 2015,
                "event": "Heat wave",
                "impact": "Severe",
                "duration": "2 weeks",
                "casualties": "Significant"
            },
            {
                "year": 2020,
                "event": "Urban floods",
                "impact": "Moderate",
                "duration": "1 week",
                "damage": "Infrastructure and property"
            }
        ],
        "environmental_changes": [
            {
                "type": "Urbanization",
                "period": "1990-2020",
                "impact": "Severe",
                "details": "80% increase in built-up area"
            },
            {
                "type": "Industrial growth",
                "period": "2000-2020",
                "impact": "High",
                "details": "200% increase in industrial units"
            }
        ]
    },
    # Add similar historical data for all districts
}

# Complete list of all districts in Sindh
sindh_districts = []
for region_districts in sindh_regions.values():
    sindh_districts.extend(region_districts)
sindh_districts = sorted(list(set(sindh_districts)))  # Remove duplicates and sort alphabetically

# District development indicators
district_development_indicators = {
    "hyderabad": {
        "population_growth": {
            "1998": 2.5,  # million
            "2017": 3.8,  # million
            "annual_growth": "2.8%"
        },
        "urbanization": {
            "urban_population": "75%",
            "growth_rate": "3.2% annually",
            "planned_developments": ["New housing schemes", "Industrial zones"]
        },
        "infrastructure": {
            "roads": "85% coverage",
            "water_supply": "70% coverage",
            "electricity": "95% coverage",
            "healthcare": {
                "hospitals": 12,
                "clinics": 45,
                "beds_per_1000": 1.8
            }
        }
    },
    # Add similar development data for all districts
}

# Future climate projections for Sindh
sindh_future_projections = {
    "2025-2050": {
        "temperature": {
            "increase": "1.5-2.5°C",
            "seasonal_changes": {
                "summer": "+2.0-3.0°C",
                "winter": "+1.0-2.0°C",
                "spring": "+1.5-2.5°C",
                "autumn": "+1.5-2.5°C"
            },
            "impacts": [
                "More frequent and intense heat waves",
                "Extended summer seasons",
                "Higher night temperatures",
                "Increased urban heat island effect",
                "Greater cooling energy demand"
            ]
        },
        "rainfall": {
            "pattern": "More erratic",
            "annual_change": "-5% to -15%",
            "seasonal_changes": {
                "monsoon": "+10% intensity, -20% frequency",
                "winter": "-25% precipitation",
                "pre-monsoon": "+5% intensity"
            },
            "impacts": [
                "Increased monsoon intensity",
                "Higher flood risks in urban areas",
                "Longer dry spells between rainfall events",
                "Reduced winter precipitation",
                "Greater water stress periods"
            ]
        },
        "extreme_events": {
            "frequency": "Increasing by 30-50%",
            "intensity": "Moderate to High increase",
            "types": [
                {
                    "event": "Heat waves",
                    "probability": "Very High",
                    "impact_level": "Severe",
                    "affected_regions": ["All regions", "Urban centers most affected"]
                },
                {
                    "event": "Urban flooding",
                    "probability": "High",
                    "impact_level": "Moderate to Severe",
                    "affected_regions": ["Coastal areas", "Major cities"]
                },
                {
                    "event": "Droughts",
                    "probability": "High",
                    "impact_level": "Severe",
                    "affected_regions": ["Northern Sindh", "Eastern regions"]
                },
                {
                    "event": "Dust storms",
                    "probability": "Moderate",
                    "impact_level": "Moderate",
                    "affected_regions": ["Northern", "Central regions"]
                }
            ]
        },
        "sea_level": {
            "rise": "20-30cm",
            "impacts": [
                "Coastal erosion",
                "Saltwater intrusion",
                "Mangrove ecosystem stress",
                "Coastal infrastructure damage"
            ]
        },
        "agricultural_impacts": {
            "crop_yields": {
                "overall_change": "-10% to -30%",
                "most_affected": ["Cotton", "Wheat", "Rice"],
                "moderately_affected": ["Sugarcane", "Vegetables"]
            },
            "growing_seasons": {
                "changes": "Shifting patterns",
                "impacts": [
                    "Modified planting dates",
                    "Changed crop cycles",
                    "Increased pest pressure"
                ]
            }
        },
        "water_resources": {
            "availability": "-15% to -25%",
            "groundwater": "Significant depletion",
            "quality": "Further deterioration",
            "impacts": [
                "Increased water stress",
                "Groundwater salinization",
                "Reduced irrigation capacity"
            ]
        }
    }
}

# Export all required data structures
__all__ = [
    'sindh_regions',
    'regional_challenges',
    'district_tehsil_mapping',
    'sindh_district_climate_info',
    'district_historical_evolution',
    'sindh_districts',
    'district_development_indicators',
    'sindh_future_projections'
] 
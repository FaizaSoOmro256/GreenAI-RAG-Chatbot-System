"""
Comprehensive climate data for Sindh Province.
Includes historical trends, seasonal patterns, and detailed climate impacts.
"""

# Historical climate trends (1960-2020)
historical_climate_trends = {
    "temperature": {
        "average_increase": "1.5°C since 1960",
        "rate_of_change": "0.25°C per decade",
        "hottest_years": ["2018", "2017", "2016", "2019", "2020"],
        "extreme_events": {
            "heat_waves": "Increased frequency by 300% since 1990",
            "cold_spells": "Decreased frequency by 45% since 1990",
            "duration": "Heat waves lasting 5-7 days longer on average"
        }
    },
    "rainfall": {
        "pattern_change": "More erratic since 1990",
        "annual_average": "Decreased by 20% since 1960",
        "monsoon_shift": "Delayed onset by 10-15 days compared to 1960s",
        "extreme_events": {
            "heavy_rainfall": "50% increase in intensity",
            "dry_spells": "Duration increased by 60%",
            "flash_floods": "Frequency doubled since 2000"
        }
    },
    "sea_level": {
        "total_rise": "1.1mm per year since 1960",
        "acceleration": "Rate increased to 3.1mm per year since 2000",
        "coastal_erosion": "2.5km inland intrusion since 1960",
        "mangrove_impact": "30% reduction in mangrove cover"
    }
}

# Seasonal climate patterns
seasonal_patterns = {
    "winter": {
        "duration": "December to February",
        "temperature_range": "7-25°C",
        "rainfall": "25-50mm total",
        "characteristics": [
            "Cold waves in northern districts",
            "Fog in central regions",
            "Mild temperatures in coastal areas"
        ],
        "agricultural_impact": "Wheat and vegetable growing season"
    },
    "spring": {
        "duration": "March to April",
        "temperature_range": "15-35°C",
        "rainfall": "10-30mm total",
        "characteristics": [
            "Rapid temperature increase",
            "Dust storms in desert regions",
            "Variable wind patterns"
        ],
        "agricultural_impact": "Harvest of winter crops, preparation for summer"
    },
    "summer": {
        "duration": "May to September",
        "temperature_range": "30-50°C",
        "rainfall": "100-300mm (monsoon dependent)",
        "characteristics": [
            "Extreme heat waves",
            "Monsoon rains (July-September)",
            "High humidity in coastal areas"
        ],
        "agricultural_impact": "Rice planting, stress on crops"
    },
    "autumn": {
        "duration": "October to November",
        "temperature_range": "20-35°C",
        "rainfall": "5-25mm total",
        "characteristics": [
            "Temperature moderation",
            "Post-monsoon dryness",
            "Variable wind conditions"
        ],
        "agricultural_impact": "Second cropping season begins"
    }
}

# Regional climate variations
regional_climate_patterns = {
    "Coastal": {
        "characteristics": [
            "High humidity (60-85%)",
            "Moderate temperature range",
            "Sea breeze influence",
            "Cyclone vulnerability"
        ],
        "unique_features": {
            "sea_breeze": "Daily temperature moderation",
            "coastal_fog": "Winter morning phenomenon",
            "monsoon_impact": "First to receive monsoon rains"
        },
        "adaptation_needs": [
            "Sea level rise protection",
            "Mangrove conservation",
            "Urban heat management"
        ]
    },
    "Central Sindh": {
        "characteristics": [
            "Hot summers, mild winters",
            "Moderate humidity",
            "River flood plains",
            "Agricultural heartland"
        ],
        "unique_features": {
            "river_effect": "Indus River moderates local climate",
            "soil_moisture": "Affects local temperature patterns",
            "wind_patterns": "North-south wind corridor"
        },
        "adaptation_needs": [
            "Flood management",
            "Agricultural water efficiency",
            "Heat-resistant infrastructure"
        ]
    },
    "Northern Sindh": {
        "characteristics": [
            "Extreme temperature range",
            "Low humidity",
            "Dust storms",
            "Limited rainfall"
        ],
        "unique_features": {
            "heat_island": "Some of Asia's highest temperatures",
            "dust_patterns": "Regular dust storms in summer",
            "thermal_belts": "Night temperature variations"
        },
        "adaptation_needs": [
            "Extreme heat management",
            "Water conservation",
            "Dust storm protection"
        ]
    },
    "Eastern Sindh": {
        "characteristics": [
            "Desert climate",
            "High temperature variation",
            "Sand dunes",
            "Variable rainfall"
        ],
        "unique_features": {
            "desert_effect": "Rapid heating and cooling",
            "rainfall_pattern": "Highly localized storms",
            "wind_erosion": "Continuous landscape change"
        },
        "adaptation_needs": [
            "Drought management",
            "Sand dune stabilization",
            "Alternative livelihoods"
        ]
    }
}

# Climate change impacts
climate_impacts = {
    "agriculture": {
        "crop_yields": {
            "wheat": "15-30% decline projected by 2050",
            "rice": "20-40% decline projected by 2050",
            "cotton": "25-35% decline projected by 2050",
            "sugarcane": "10-20% decline projected by 2050"
        },
        "growing_seasons": {
            "shifts": "10-30 day changes in planting dates",
            "duration": "5-15 day reduction in growing period",
            "pests": "New pest patterns and invasive species"
        },
        "adaptation_strategies": [
            "Drought-resistant crop varieties",
            "Modified planting calendars",
            "Efficient irrigation systems",
            "Crop diversification"
        ]
    },
    "water_resources": {
        "river_flow": {
            "annual_change": "20-30% reduction projected by 2050",
            "seasonal_variation": "More extreme high and low flows",
            "glacial_impact": "Increased early summer flows, reduced late summer flows"
        },
        "groundwater": {
            "depletion_rate": "1-3 meters per year",
            "quality_issues": "Increasing salinity and contamination",
            "recharge": "Reduced by 15-25% due to rainfall changes"
        },
        "adaptation_strategies": [
            "Water storage enhancement",
            "Groundwater recharge projects",
            "Water-efficient technologies",
            "Rainwater harvesting"
        ]
    },
    "health": {
        "heat_related": {
            "mortality": "Projected 50% increase in heat-related deaths by 2050",
            "morbidity": "Heat stress, cardiovascular issues, respiratory problems",
            "vulnerable_groups": "Elderly, children, outdoor workers"
        },
        "disease_patterns": {
            "vector_borne": "Expanded range of dengue, malaria",
            "water_borne": "Increased cholera, typhoid risk",
            "air_quality": "Respiratory issues from dust and pollution"
        },
        "adaptation_strategies": [
            "Heat warning systems",
            "Public cooling centers",
            "Healthcare capacity building",
            "Disease surveillance"
        ]
    },
    "biodiversity": {
        "ecosystems": {
            "mangroves": "50% at risk by 2050",
            "wetlands": "30-40% degradation projected",
            "desert": "Increased desertification"
        },
        "species": {
            "migration": "Shifting patterns and timing",
            "extinction_risk": "15-20% of local species at risk",
            "invasive_species": "Increased threat to native ecosystems"
        },
        "adaptation_strategies": [
            "Protected area expansion",
            "Ecosystem restoration",
            "Species monitoring",
            "Habitat connectivity"
        ]
    }
}

# Sustainability initiatives
sustainability_programs = {
    "renewable_energy": {
        "solar": {
            "current_capacity": "500 MW",
            "planned_expansion": "2000 MW by 2025",
            "focus_areas": ["Desert solar farms", "Urban rooftop solar", "Agricultural solar pumps"]
        },
        "wind": {
            "current_capacity": "785 MW",
            "planned_expansion": "1500 MW by 2025",
            "focus_areas": ["Coastal wind corridor", "Hybrid wind-solar projects"]
        }
    },
    "water_management": {
        "conservation": {
            "programs": ["Canal lining", "Drip irrigation", "Water recycling"],
            "targets": "20% reduction in agricultural water use by 2030"
        },
        "quality": {
            "initiatives": ["Urban water treatment", "Industrial effluent control"],
            "goals": "Clean drinking water access for 90% population by 2030"
        }
    },
    "agriculture": {
        "sustainable_practices": {
            "programs": ["Climate-smart agriculture", "Organic farming", "Precision irrigation"],
            "targets": "30% farms using sustainable practices by 2030"
        },
        "research": {
            "focus_areas": ["Drought-resistant crops", "Saline agriculture", "Water efficiency"],
            "collaborations": ["International research centers", "Local universities"]
        }
    }
} 
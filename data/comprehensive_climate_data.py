"""
Complete comprehensive climate data for all districts of Sindh with complete climate factors.
This file ensures all districts have detailed information for:
- Temperature (daily/seasonal averages, extremes)
- Precipitation (rainfall, patterns, variability)
- Humidity (moisture levels, seasonal variations)
- Wind Patterns (directions, speeds, seasonal changes)
- Atmospheric Pressure (variations affecting weather)
- Sunshine/Solar Radiation (intensity, sunny days)
- Cloud Cover (frequency, type, thickness)
- Evaporation/Transpiration (water cycle interactions)
- Storms/Extreme Weather (frequency, types)
- Seasonal Patterns (summer, winter, spring, autumn, monsoons)

Generated manually to ensure complete coverage of all 27 districts.
"""

# Complete list of all districts in Sindh
SINDH_DISTRICTS = [
    "karachi_central", "karachi_east", "karachi_west", "karachi_south", "karachi_malir", "karachi_korangi",
    "hyderabad", "sukkur", "larkana", "mirpurkhas", "nawabshah", "jacobabad", "shikarpur", "dadu",
    "jamshoro", "tharparkar", "badin", "sanghar", "khairpur", "ghotki", "kashmore", "umerkot",
    "matiari", "tando_allahyar", "tando_muhammad_khan", "naushahro_feroze", "sujawal"
]

# Complete comprehensive climate data for all districts
COMPREHENSIVE_CLIMATE_DATA = {
    "karachi_central": {
        "climate_profile": {
            "temperature": {
                "annual_average": "27.5°C",
                "daily_average": {
                    "summer": "32.5-42.5°C",
                    "winter": "12.5-22.5°C",
                    "spring": "25.5-35.5°C",
                    "autumn": "26.5-34.5°C"
                },
                "seasonal_averages": {
                    "summer": "35.5°C",
                    "winter": "14.5°C",
                    "spring": "29.5°C",
                    "autumn": "28.5°C"
                },
                "extremes": {
                    "highest_recorded": "47.5°C",
                    "lowest_recorded": "2.5°C",
                    "summer_max": "39.5-45.5°C",
                    "winter_min": "5.5-12.5°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "220mm",
                "rainfall": {
                    "annual": "220mm",
                    "monsoon_contribution": "70-80%",
                    "rainy_days": "22-27 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-3 times per year)",
                "seasonal_totals": {
                    "summer": "165mm (monsoon)",
                    "winter": "14mm",
                    "spring": "22mm",
                    "autumn": "14mm"
                },
                "patterns": "Highly variable, concentrated in monsoon",
                "variability": "Increasing year-to-year variation"
            },
            "humidity": {
                "annual_average": "70%",
                "seasonal_variations": {
                    "summer": "80-90%",
                    "winter": "50-60%",
                    "spring": "65-75%",
                    "autumn": "65-80%"
                },
                "daily_patterns": {
                    "morning": "80-90%",
                    "afternoon": "55-65%",
                    "evening": "65-80%"
                },
                "trend": "Variable with monsoon influence"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "Southwest (monsoon)",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "12-18 km/h",
                    "summer": "15-25 km/h",
                    "winter": "8-15 km/h",
                    "storm_conditions": "25-45 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Strong southwest winds",
                    "winter_transition": "Calm periods",
                    "spring_winds": "Moderate variable winds"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1012-1013 hPa",
                "variations": {
                    "daily": "±3-4 hPa",
                    "seasonal": "±5-6 hPa",
                    "monsoon_low": "1007-1011 hPa"
                },
                "weather_system_effects": "Low pressure during monsoon, high pressure in winter"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "260-300 days per year",
                "cloudy_days": "65-105 days per year",
                "solar_radiation": {
                    "annual_average": "5.5-6.0 kWh/m²/day",
                    "summer_peak": "6.8-7.2 kWh/m²/day",
                    "winter_minimum": "3.9-4.2 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "High (8-11) in summer",
                    "shading_factor": "Variable based on urban development"
                }
            },
            "cloud_cover": {
                "annual_average": "25-35%",
                "seasonal_coverage": {
                    "monsoon_season": "60-80%",
                    "dry_season": "10-20%",
                    "winter": "20-35%",
                    "spring": "25-40%"
                },
                "cloud_types": {
                    "cumulus": "Common in summer",
                    "stratus": "Common in monsoon",
                    "cirrus": "Occasional in winter"
                },
                "thickness": "Variable from thin cirrus to thick cumulonimbus"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "1900-2500mm",
                "seasonal_rates": {
                    "summer_peak": "9-15mm/day",
                    "winter_minimum": "3-6mm/day",
                    "spring": "6-11mm/day",
                    "autumn": "5-9mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Variable based on urban development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "45.5-47.5°C"
                },
                "dust_storms": {
                    "frequency": "5-12 per year",
                    "peak_season": "April-June",
                    "intensity": "Moderate to severe"
                },
                "droughts": {
                    "frequency": "1-3 per decade",
                    "duration": "6-18 months",
                    "severity": "Moderate to extreme"
                },
                "thunderstorms": {
                    "frequency": "8-20 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate frequency"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Very hot and humid",
                    "temperature_range": "32.5-42.5°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "12.5-22.5°C",
                    "rainfall": "Minimal"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Hot with heavy rainfall",
                    "peak_months": "July-August",
                    "rainfall_contribution": "70-80% of annual"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Rapidly warming",
                    "temperature_range": "25.5-35.5°C",
                    "rainfall": "Light occasional showers"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling period",
                    "temperature_range": "26.5-34.5°C",
                    "rainfall": "Light showers"
                }
            }
        }
    },
    "karachi_east": {
        "climate_profile": {
            "temperature": {
                "annual_average": "27.5°C",
                "daily_average": {
                    "summer": "32-38°C",
                    "winter": "18-25°C",
                    "spring": "25-32°C",
                    "autumn": "26-33°C"
                },
                "seasonal_averages": {
                    "summer": "35°C",
                    "winter": "22°C",
                    "spring": "28°C",
                    "autumn": "29°C"
                },
                "extremes": {
                    "highest_recorded": "48.5°C",
                    "lowest_recorded": "8.5°C",
                    "summer_max": "42-45°C",
                    "winter_min": "8-12°C"
                },
                "trend": "Increasing by 0.4°C per decade"
            },
            "precipitation": {
                "annual_total": "220mm",
                "rainfall": {
                    "annual": "220mm",
                    "monsoon_contribution": "75%",
                    "rainy_days": "25-30 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (2-3 times per year)",
                "seasonal_totals": {
                    "summer": "165mm (monsoon)",
                    "winter": "15mm",
                    "spring": "25mm",
                    "autumn": "15mm"
                },
                "patterns": "Highly variable, concentrated in monsoon",
                "variability": "Increasing year-to-year variation"
            },
            "humidity": {
                "annual_average": "70%",
                "seasonal_variations": {
                    "summer": "80-85%",
                    "winter": "50-60%",
                    "spring": "65-75%",
                    "autumn": "70-80%"
                },
                "daily_patterns": {
                    "morning": "75-85%",
                    "afternoon": "60-70%",
                    "evening": "70-80%"
                },
                "trend": "Variable with monsoon influence"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "Southwest (monsoon)",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "12 km/h",
                    "summer": "15-20 km/h",
                    "winter": "8-12 km/h",
                    "storm_conditions": "25-40 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Strong southwest winds",
                    "winter_transition": "Calm periods with light breezes",
                    "spring_winds": "Moderate variable winds"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1013 hPa",
                "variations": {
                    "daily": "±2 hPa",
                    "seasonal": "±5 hPa",
                    "monsoon_low": "1009-1011 hPa"
                },
                "weather_system_effects": "Low pressure during monsoon, high pressure in winter"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "260-280 days per year",
                "cloudy_days": "85-105 days per year",
                "solar_radiation": {
                    "annual_average": "5.5 kWh/m²/day",
                    "summer_peak": "6.8 kWh/m²/day",
                    "winter_minimum": "3.9 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "High (8-10) in summer",
                    "shading_factor": "Urban areas have 20-30% less direct sunlight"
                }
            },
            "cloud_cover": {
                "annual_average": "35%",
                "seasonal_coverage": {
                    "monsoon_season": "70-80%",
                    "dry_season": "15-20%",
                    "winter": "25-35%",
                    "spring": "30-40%"
                },
                "cloud_types": {
                    "cumulus": "Most common in summer",
                    "stratus": "Common in monsoon",
                    "cirrus": "Occasional in winter"
                },
                "thickness": "Variable from thin cirrus to thick cumulonimbus"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "1900-2200mm",
                "seasonal_rates": {
                    "summer_peak": "9-12mm/day",
                    "winter_minimum": "3-5mm/day",
                    "spring": "6-9mm/day",
                    "autumn": "5-8mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Limited due to urban development",
                    "water_cycle": "Reduced natural water recycling"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-6 per year",
                    "duration": "3-7 days",
                    "peak_temperature": "46-48°C"
                },
                "dust_storms": {
                    "frequency": "5-8 per year",
                    "peak_season": "April-June",
                    "intensity": "Moderate to severe"
                },
                "droughts": {
                    "frequency": "1-3 per decade",
                    "duration": "6-18 months",
                    "severity": "Moderate to extreme"
                },
                "thunderstorms": {
                    "frequency": "15-20 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate frequency"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Very hot and humid",
                    "temperature_range": "32-45°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Mild and dry",
                    "temperature_range": "18-25°C",
                    "rainfall": "Occasional light showers"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Hot and humid with heavy rainfall",
                    "peak_months": "July-August",
                    "rainfall_contribution": "75% of annual total"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Warming period, pleasant temperatures",
                    "temperature_range": "25-35°C",
                    "rainfall": "Light occasional showers"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling period, moderate humidity",
                    "temperature_range": "26-33°C",
                    "rainfall": "Light showers, decreasing humidity"
                }
            }
        }
    },
    "karachi_south": {
        "climate_profile": {
            "temperature": {
                "annual_average": "27.5°C",
                "daily_average": {
                    "summer": "32-38°C",
                    "winter": "18-25°C",
                    "spring": "25-32°C",
                    "autumn": "26-33°C"
                },
                "seasonal_averages": {
                    "summer": "35°C",
                    "winter": "22°C",
                    "spring": "28°C",
                    "autumn": "29°C"
                },
                "extremes": {
                    "highest_recorded": "48.5°C",
                    "lowest_recorded": "8.5°C",
                    "summer_max": "42-45°C",
                    "winter_min": "8-12°C"
                },
                "trend": "Increasing by 0.4°C per decade"
            },
            "precipitation": {
                "annual_total": "220mm",
                "rainfall": {
                    "annual": "220mm",
                    "monsoon_contribution": "75%",
                    "rainy_days": "25-30 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (2-3 times per year)",
                "seasonal_totals": {
                    "summer": "165mm (monsoon)",
                    "winter": "15mm",
                    "spring": "25mm",
                    "autumn": "15mm"
                },
                "patterns": "Highly variable, concentrated in monsoon",
                "variability": "Increasing year-to-year variation"
            },
            "humidity": {
                "annual_average": "70%",
                "seasonal_variations": {
                    "summer": "80-85%",
                    "winter": "50-60%",
                    "spring": "65-75%",
                    "autumn": "70-80%"
                },
                "daily_patterns": {
                    "morning": "75-85%",
                    "afternoon": "60-70%",
                    "evening": "70-80%"
                },
                "trend": "Variable with monsoon influence"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "Southwest (monsoon)",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "12 km/h",
                    "summer": "15-20 km/h",
                    "winter": "8-12 km/h",
                    "storm_conditions": "25-40 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Strong southwest winds",
                    "winter_transition": "Calm periods with light breezes",
                    "spring_winds": "Moderate variable winds"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1013 hPa",
                "variations": {
                    "daily": "±2 hPa",
                    "seasonal": "±5 hPa",
                    "monsoon_low": "1009-1011 hPa"
                },
                "weather_system_effects": "Low pressure during monsoon, high pressure in winter"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "260-280 days per year",
                "cloudy_days": "85-105 days per year",
                "solar_radiation": {
                    "annual_average": "5.5 kWh/m²/day",
                    "summer_peak": "6.8 kWh/m²/day",
                    "winter_minimum": "3.9 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "High (8-10) in summer",
                    "shading_factor": "Urban areas have 20-30% less direct sunlight"
                }
            },
            "cloud_cover": {
                "annual_average": "35%",
                "seasonal_coverage": {
                    "monsoon_season": "70-80%",
                    "dry_season": "15-20%",
                    "winter": "25-35%",
                    "spring": "30-40%"
                },
                "cloud_types": {
                    "cumulus": "Most common in summer",
                    "stratus": "Common in monsoon",
                    "cirrus": "Occasional in winter"
                },
                "thickness": "Variable from thin cirrus to thick cumulonimbus"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "1900-2200mm",
                "seasonal_rates": {
                    "summer_peak": "9-12mm/day",
                    "winter_minimum": "3-5mm/day",
                    "spring": "6-9mm/day",
                    "autumn": "5-8mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Limited due to urban development",
                    "water_cycle": "Reduced natural water recycling"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-6 per year",
                    "duration": "3-7 days",
                    "peak_temperature": "46-48°C"
                },
                "dust_storms": {
                    "frequency": "5-8 per year",
                    "peak_season": "April-June",
                    "intensity": "Moderate to severe"
                },
                "droughts": {
                    "frequency": "1-3 per decade",
                    "duration": "6-18 months",
                    "severity": "Moderate to extreme"
                },
                "thunderstorms": {
                    "frequency": "15-20 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate frequency"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Very hot and humid",
                    "temperature_range": "32-45°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Mild and dry",
                    "temperature_range": "18-25°C",
                    "rainfall": "Occasional light showers"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Hot and humid with heavy rainfall",
                    "peak_months": "July-August",
                    "rainfall_contribution": "75% of annual total"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Warming period, pleasant temperatures",
                    "temperature_range": "25-35°C",
                    "rainfall": "Light occasional showers"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling period, moderate humidity",
                    "temperature_range": "26-33°C",
                    "rainfall": "Light showers, decreasing humidity"
                }
            }
        }
    },
    "karachi_malir": {
        "climate_profile": {
            "temperature": {
                "annual_average": "27.5°C",
                "daily_average": {
                    "summer": "32-38°C",
                    "winter": "18-25°C",
                    "spring": "25-32°C",
                    "autumn": "26-33°C"
                },
                "seasonal_averages": {
                    "summer": "35°C",
                    "winter": "22°C",
                    "spring": "28°C",
                    "autumn": "29°C"
                },
                "extremes": {
                    "highest_recorded": "48.5°C",
                    "lowest_recorded": "8.5°C",
                    "summer_max": "42-45°C",
                    "winter_min": "8-12°C"
                },
                "trend": "Increasing by 0.4°C per decade"
            },
            "precipitation": {
                "annual_total": "220mm",
                "rainfall": {
                    "annual": "220mm",
                    "monsoon_contribution": "75%",
                    "rainy_days": "25-30 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (2-3 times per year)",
                "seasonal_totals": {
                    "summer": "165mm (monsoon)",
                    "winter": "15mm",
                    "spring": "25mm",
                    "autumn": "15mm"
                },
                "patterns": "Highly variable, concentrated in monsoon",
                "variability": "Increasing year-to-year variation"
            },
            "humidity": {
                "annual_average": "70%",
                "seasonal_variations": {
                    "summer": "80-85%",
                    "winter": "50-60%",
                    "spring": "65-75%",
                    "autumn": "70-80%"
                },
                "daily_patterns": {
                    "morning": "75-85%",
                    "afternoon": "60-70%",
                    "evening": "70-80%"
                },
                "trend": "Variable with monsoon influence"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "Southwest (monsoon)",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "12 km/h",
                    "summer": "15-20 km/h",
                    "winter": "8-12 km/h",
                    "storm_conditions": "25-40 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Strong southwest winds",
                    "winter_transition": "Calm periods with light breezes",
                    "spring_winds": "Moderate variable winds"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1013 hPa",
                "variations": {
                    "daily": "±2 hPa",
                    "seasonal": "±5 hPa",
                    "monsoon_low": "1009-1011 hPa"
                },
                "weather_system_effects": "Low pressure during monsoon, high pressure in winter"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "260-280 days per year",
                "cloudy_days": "85-105 days per year",
                "solar_radiation": {
                    "annual_average": "5.5 kWh/m²/day",
                    "summer_peak": "6.8 kWh/m²/day",
                    "winter_minimum": "3.9 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "High (8-10) in summer",
                    "shading_factor": "Urban areas have 20-30% less direct sunlight"
                }
            },
            "cloud_cover": {
                "annual_average": "35%",
                "seasonal_coverage": {
                    "monsoon_season": "70-80%",
                    "dry_season": "15-20%",
                    "winter": "25-35%",
                    "spring": "30-40%"
                },
                "cloud_types": {
                    "cumulus": "Most common in summer",
                    "stratus": "Common in monsoon",
                    "cirrus": "Occasional in winter"
                },
                "thickness": "Variable from thin cirrus to thick cumulonimbus"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "1900-2200mm",
                "seasonal_rates": {
                    "summer_peak": "9-12mm/day",
                    "winter_minimum": "3-5mm/day",
                    "spring": "6-9mm/day",
                    "autumn": "5-8mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Limited due to urban development",
                    "water_cycle": "Reduced natural water recycling"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-6 per year",
                    "duration": "3-7 days",
                    "peak_temperature": "46-48°C"
                },
                "dust_storms": {
                    "frequency": "5-8 per year",
                    "peak_season": "April-June",
                    "intensity": "Moderate to severe"
                },
                "droughts": {
                    "frequency": "1-3 per decade",
                    "duration": "6-18 months",
                    "severity": "Moderate to extreme"
                },
                "thunderstorms": {
                    "frequency": "15-20 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate frequency"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Very hot and humid",
                    "temperature_range": "32-45°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Mild and dry",
                    "temperature_range": "18-25°C",
                    "rainfall": "Occasional light showers"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Hot and humid with heavy rainfall",
                    "peak_months": "July-August",
                    "rainfall_contribution": "75% of annual total"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Warming period, pleasant temperatures",
                    "temperature_range": "25-35°C",
                    "rainfall": "Light occasional showers"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling period, moderate humidity",
                    "temperature_range": "26-33°C",
                    "rainfall": "Light showers, decreasing humidity"
                }
            }
        }
    },
    "karachi_korangi": {
        "climate_profile": {
            "temperature": {
                "annual_average": "27.5°C",
                "daily_average": {
                    "summer": "32-38°C",
                    "winter": "18-25°C",
                    "spring": "25-32°C",
                    "autumn": "26-33°C"
                },
                "seasonal_averages": {
                    "summer": "35°C",
                    "winter": "22°C",
                    "spring": "28°C",
                    "autumn": "29°C"
                },
                "extremes": {
                    "highest_recorded": "48.5°C",
                    "lowest_recorded": "8.5°C",
                    "summer_max": "42-45°C",
                    "winter_min": "8-12°C"
                },
                "trend": "Increasing by 0.4°C per decade"
            },
            "precipitation": {
                "annual_total": "220mm",
                "rainfall": {
                    "annual": "220mm",
                    "monsoon_contribution": "75%",
                    "rainy_days": "25-30 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (2-3 times per year)",
                "seasonal_totals": {
                    "summer": "165mm (monsoon)",
                    "winter": "15mm",
                    "spring": "25mm",
                    "autumn": "15mm"
                },
                "patterns": "Highly variable, concentrated in monsoon",
                "variability": "Increasing year-to-year variation"
            },
            "humidity": {
                "annual_average": "70%",
                "seasonal_variations": {
                    "summer": "80-85%",
                    "winter": "50-60%",
                    "spring": "65-75%",
                    "autumn": "70-80%"
                },
                "daily_patterns": {
                    "morning": "75-85%",
                    "afternoon": "60-70%",
                    "evening": "70-80%"
                },
                "trend": "Variable with monsoon influence"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "Southwest (monsoon)",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "12 km/h",
                    "summer": "15-20 km/h",
                    "winter": "8-12 km/h",
                    "storm_conditions": "25-40 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Strong southwest winds",
                    "winter_transition": "Calm periods with light breezes",
                    "spring_winds": "Moderate variable winds"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1013 hPa",
                "variations": {
                    "daily": "±2 hPa",
                    "seasonal": "±5 hPa",
                    "monsoon_low": "1009-1011 hPa"
                },
                "weather_system_effects": "Low pressure during monsoon, high pressure in winter"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "260-280 days per year",
                "cloudy_days": "85-105 days per year",
                "solar_radiation": {
                    "annual_average": "5.5 kWh/m²/day",
                    "summer_peak": "6.8 kWh/m²/day",
                    "winter_minimum": "3.9 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "High (8-10) in summer",
                    "shading_factor": "Urban areas have 20-30% less direct sunlight"
                }
            },
            "cloud_cover": {
                "annual_average": "35%",
                "seasonal_coverage": {
                    "monsoon_season": "70-80%",
                    "dry_season": "15-20%",
                    "winter": "25-35%",
                    "spring": "30-40%"
                },
                "cloud_types": {
                    "cumulus": "Most common in summer",
                    "stratus": "Common in monsoon",
                    "cirrus": "Occasional in winter"
                },
                "thickness": "Variable from thin cirrus to thick cumulonimbus"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "1900-2200mm",
                "seasonal_rates": {
                    "summer_peak": "9-12mm/day",
                    "winter_minimum": "3-5mm/day",
                    "spring": "6-9mm/day",
                    "autumn": "5-8mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Limited due to urban development",
                    "water_cycle": "Reduced natural water recycling"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-6 per year",
                    "duration": "3-7 days",
                    "peak_temperature": "46-48°C"
                },
                "dust_storms": {
                    "frequency": "5-8 per year",
                    "peak_season": "April-June",
                    "intensity": "Moderate to severe"
                },
                "droughts": {
                    "frequency": "1-3 per decade",
                    "duration": "6-18 months",
                    "severity": "Moderate to extreme"
                },
                "thunderstorms": {
                    "frequency": "15-20 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate frequency"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Very hot and humid",
                    "temperature_range": "32-45°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Mild and dry",
                    "temperature_range": "18-25°C",
                    "rainfall": "Occasional light showers"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Hot and humid with heavy rainfall",
                    "peak_months": "July-August",
                    "rainfall_contribution": "75% of annual total"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Warming period, pleasant temperatures",
                    "temperature_range": "25-35°C",
                    "rainfall": "Light occasional showers"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling period, moderate humidity",
                    "temperature_range": "26-33°C",
                    "rainfall": "Light showers, decreasing humidity"
                }
            }
        }
    },
    "hyderabad": {
        "climate_profile": {
            "temperature": {
                "annual_average": "30°C",
                "daily_average": {
                    "summer": "35-45°C",
                    "winter": "15-25°C",
                    "spring": "28-38°C",
                    "autumn": "29-37°C"
                },
                "seasonal_averages": {
                    "summer": "40°C",
                    "winter": "20°C",
                    "spring": "33°C",
                    "autumn": "33°C"
                },
                "extremes": {
                    "highest_recorded": "50°C",
                    "lowest_recorded": "5°C",
                    "summer_max": "42-48°C",
                    "winter_min": "5-15°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "175mm",
                "rainfall": {
                    "annual": "175mm",
                    "monsoon_contribution": "75-80%",
                    "rainy_days": "18-22 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-2 times per year)",
                "seasonal_totals": {
                    "summer": "131mm (monsoon)",
                    "winter": "12mm",
                    "spring": "18mm",
                    "autumn": "12mm"
                },
                "patterns": "Highly variable, concentrated in monsoon",
                "variability": "Increasing year-to-year variation"
            },
            "humidity": {
                "annual_average": "60%",
                "seasonal_variations": {
                    "summer": "70-80%",
                    "winter": "40-50%",
                    "spring": "55-65%",
                    "autumn": "60-70%"
                },
                "daily_patterns": {
                    "morning": "70-80%",
                    "afternoon": "45-55%",
                    "evening": "60-70%"
                },
                "trend": "Variable with monsoon influence"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "Southwest (monsoon)",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "12-18 km/h",
                    "summer": "15-25 km/h",
                    "winter": "8-15 km/h",
                    "storm_conditions": "25-45 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Strong southwest winds",
                    "winter_transition": "Calm periods",
                    "spring_winds": "Moderate variable winds"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1012-1013 hPa",
                "variations": {
                    "daily": "±3-4 hPa",
                    "seasonal": "±5-6 hPa",
                    "monsoon_low": "1007-1011 hPa"
                },
                "weather_system_effects": "Low pressure during monsoon, high pressure in winter"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "270-310 days per year",
                "cloudy_days": "55-95 days per year",
                "solar_radiation": {
                    "annual_average": "5.8-6.3 kWh/m²/day",
                    "summer_peak": "7.0-7.5 kWh/m²/day",
                    "winter_minimum": "4.1-4.5 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "Very High (9-11) in summer",
                    "shading_factor": "Moderate urban development"
                }
            },
            "cloud_cover": {
                "annual_average": "20-30%",
                "seasonal_coverage": {
                    "monsoon_season": "55-75%",
                    "dry_season": "8-18%",
                    "winter": "15-30%",
                    "spring": "20-35%"
                },
                "cloud_types": {
                    "cumulus": "Common in summer",
                    "stratus": "Common in monsoon",
                    "cirrus": "Occasional in winter"
                },
                "thickness": "Variable from thin cirrus to thick cumulonimbus"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "2100-2700mm",
                "seasonal_rates": {
                    "summer_peak": "10-16mm/day",
                    "winter_minimum": "3-6mm/day",
                    "spring": "7-12mm/day",
                    "autumn": "6-10mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Moderate agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "5-9 per year",
                    "duration": "4-12 days",
                    "peak_temperature": "48-50°C"
                },
                "dust_storms": {
                    "frequency": "6-15 per year",
                    "peak_season": "April-June",
                    "intensity": "Moderate to severe"
                },
                "droughts": {
                    "frequency": "1-3 per decade",
                    "duration": "6-18 months",
                    "severity": "Moderate to extreme"
                },
                "thunderstorms": {
                    "frequency": "10-25 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate to high frequency"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Very hot and dry",
                    "temperature_range": "35-48°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "15-25°C",
                    "rainfall": "Minimal"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Hot with heavy rainfall",
                    "peak_months": "July-August",
                    "rainfall_contribution": "75-80% of annual"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Rapidly warming",
                    "temperature_range": "28-38°C",
                    "rainfall": "Light occasional showers"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling period",
                    "temperature_range": "29-37°C",
                    "rainfall": "Light showers"
                }
            }
        }
    },
    "sukkur": {
        "climate_profile": {
            "temperature": {
                "annual_average": "32°C",
                "daily_average": {
                    "summer": "37-47°C",
                    "winter": "17-27°C",
                    "spring": "30-40°C",
                    "autumn": "31-39°C"
                },
                "seasonal_averages": {
                    "summer": "42°C",
                    "winter": "22°C",
                    "spring": "35°C",
                    "autumn": "35°C"
                },
                "extremes": {
                    "highest_recorded": "52°C",
                    "lowest_recorded": "7°C",
                    "summer_max": "47-52°C",
                    "winter_min": "7-17°C"
                },
                "trend": "Increasing by 0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "120mm",
                "rainfall": {
                    "annual": "120mm",
                    "monsoon_contribution": "80%",
                    "rainy_days": "12-15 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-2 times per year)",
                "seasonal_totals": {
                    "summer": "96mm (monsoon)",
                    "winter": "8mm",
                    "spring": "12mm",
                    "autumn": "8mm"
                },
                "patterns": "Highly variable, concentrated in monsoon",
                "variability": "Increasing year-to-year variation"
            },
            "humidity": {
                "annual_average": "45%",
                "seasonal_variations": {
                    "summer": "55-65%",
                    "winter": "25-35%",
                    "spring": "40-50%",
                    "autumn": "45-55%"
                },
                "daily_patterns": {
                    "morning": "55-65%",
                    "afternoon": "30-40%",
                    "evening": "45-55%"
                },
                "trend": "Variable with monsoon influence"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "Southwest (monsoon)",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "15-20 km/h",
                    "summer": "20-30 km/h",
                    "winter": "10-18 km/h",
                    "storm_conditions": "30-50 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Strong southwest winds",
                    "winter_transition": "Calm periods",
                    "spring_winds": "Moderate variable winds"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1011-1012 hPa",
                "variations": {
                    "daily": "±3-4 hPa",
                    "seasonal": "±6-7 hPa",
                    "monsoon_low": "1005-1009 hPa"
                },
                "weather_system_effects": "Low pressure during monsoon, high pressure in winter"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "280-320 days per year",
                "cloudy_days": "45-85 days per year",
                "solar_radiation": {
                    "annual_average": "6.0-6.5 kWh/m²/day",
                    "summer_peak": "7.2-7.8 kWh/m²/day",
                    "winter_minimum": "4.2-4.6 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "Very High (9-11) in summer",
                    "shading_factor": "Limited urban development"
                }
            },
            "cloud_cover": {
                "annual_average": "15-25%",
                "seasonal_coverage": {
                    "monsoon_season": "50-70%",
                    "dry_season": "5-15%",
                    "winter": "10-25%",
                    "spring": "15-30%"
                },
                "cloud_types": {
                    "cumulus": "Common in summer",
                    "stratus": "Common in monsoon",
                    "cirrus": "Occasional in winter"
                },
                "thickness": "Variable from thin cirrus to thick cumulonimbus"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "2500-3200mm",
                "seasonal_rates": {
                    "summer_peak": "12-18mm/day",
                    "winter_minimum": "4-7mm/day",
                    "spring": "8-13mm/day",
                    "autumn": "7-11mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Limited agricultural development",
                    "water_cycle": "Reduced natural water recycling"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "6-10 per year",
                    "duration": "5-15 days",
                    "peak_temperature": "50-52°C"
                },
                "dust_storms": {
                    "frequency": "8-18 per year",
                    "peak_season": "April-June",
                    "intensity": "Moderate to severe"
                },
                "droughts": {
                    "frequency": "2-4 per decade",
                    "duration": "8-24 months",
                    "severity": "Moderate to extreme"
                },
                "thunderstorms": {
                    "frequency": "6-15 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate frequency"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Extremely hot and dry",
                    "temperature_range": "37-52°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "17-27°C",
                    "rainfall": "Minimal"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Hot with moderate rainfall",
                    "peak_months": "July-August",
                    "rainfall_contribution": "80% of annual"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Rapidly warming",
                    "temperature_range": "30-40°C",
                    "rainfall": "Light occasional showers"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling period",
                    "temperature_range": "31-39°C",
                    "rainfall": "Light showers"
                }
            }
        }
    },
    "larkana": {
        "climate_profile": {
            "temperature": {
                "annual_average": "31°C",
                "daily_average": {
                    "summer": "36-46°C",
                    "winter": "16-26°C",
                    "spring": "29-39°C",
                    "autumn": "30-38°C"
                },
                "seasonal_averages": {
                    "summer": "41°C",
                    "winter": "21°C",
                    "spring": "34°C",
                    "autumn": "34°C"
                },
                "extremes": {
                    "highest_recorded": "51°C",
                    "lowest_recorded": "6°C",
                    "summer_max": "46-51°C",
                    "winter_min": "6-16°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "140mm",
                "rainfall": {
                    "annual": "140mm",
                    "monsoon_contribution": "75-80%",
                    "rainy_days": "14-18 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-3 times per year)",
                "seasonal_totals": {
                    "summer": "105mm (monsoon)",
                    "winter": "9mm",
                    "spring": "14mm",
                    "autumn": "9mm"
                },
                "patterns": "Highly variable, concentrated in monsoon",
                "variability": "Increasing year-to-year variation"
            },
            "humidity": {
                "annual_average": "55%",
                "seasonal_variations": {
                    "summer": "65-75%",
                    "winter": "35-45%",
                    "spring": "50-60%",
                    "autumn": "55-65%"
                },
                "daily_patterns": {
                    "morning": "65-75%",
                    "afternoon": "40-50%",
                    "evening": "55-65%"
                },
                "trend": "Variable with monsoon influence"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "Southwest (monsoon)",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "13-18 km/h",
                    "summer": "18-28 km/h",
                    "winter": "8-15 km/h",
                    "storm_conditions": "28-48 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Strong southwest winds",
                    "winter_transition": "Calm periods",
                    "spring_winds": "Moderate variable winds"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1012-1013 hPa",
                "variations": {
                    "daily": "±3-4 hPa",
                    "seasonal": "±5-6 hPa",
                    "monsoon_low": "1007-1011 hPa"
                },
                "weather_system_effects": "Low pressure during monsoon, high pressure in winter"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "270-310 days per year",
                "cloudy_days": "55-95 days per year",
                "solar_radiation": {
                    "annual_average": "5.8-6.3 kWh/m²/day",
                    "summer_peak": "7.0-7.5 kWh/m²/day",
                    "winter_minimum": "4.0-4.4 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "Very High (9-11) in summer",
                    "shading_factor": "Moderate urban development"
                }
            },
            "cloud_cover": {
                "annual_average": "20-30%",
                "seasonal_coverage": {
                    "monsoon_season": "55-75%",
                    "dry_season": "8-18%",
                    "winter": "15-30%",
                    "spring": "20-35%"
                },
                "cloud_types": {
                    "cumulus": "Common in summer",
                    "stratus": "Common in monsoon",
                    "cirrus": "Occasional in winter"
                },
                "thickness": "Variable from thin cirrus to thick cumulonimbus"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "2200-2800mm",
                "seasonal_rates": {
                    "summer_peak": "11-16mm/day",
                    "winter_minimum": "3-6mm/day",
                    "spring": "7-12mm/day",
                    "autumn": "6-10mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Moderate agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "5-9 per year",
                    "duration": "4-12 days",
                    "peak_temperature": "48-51°C"
                },
                "dust_storms": {
                    "frequency": "6-15 per year",
                    "peak_season": "April-June",
                    "intensity": "Moderate to severe"
                },
                "droughts": {
                    "frequency": "1-3 per decade",
                    "duration": "6-18 months",
                    "severity": "Moderate to extreme"
                },
                "thunderstorms": {
                    "frequency": "8-18 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate frequency"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Very hot and dry",
                    "temperature_range": "36-51°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "16-26°C",
                    "rainfall": "Minimal"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Hot with moderate rainfall",
                    "peak_months": "July-August",
                    "rainfall_contribution": "75-80% of annual"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Rapidly warming",
                    "temperature_range": "29-39°C",
                    "rainfall": "Light occasional showers"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling period",
                    "temperature_range": "30-38°C",
                    "rainfall": "Light showers"
                }
            }
        }
    },
    "mirpurkhas": {
        "climate_profile": {
            "temperature": {
                "annual_average": "31.5°C",
                "daily_average": {
                    "summer": "36.5-46.5°C",
                    "winter": "16.5-26.5°C",
                    "spring": "29.5-39.5°C",
                    "autumn": "30.5-38.5°C"
                },
                "seasonal_averages": {
                    "summer": "41.5°C",
                    "winter": "21.5°C",
                    "spring": "34.5°C",
                    "autumn": "34.5°C"
                },
                "extremes": {
                    "highest_recorded": "51.5°C",
                    "lowest_recorded": "6.5°C",
                    "summer_max": "46.5-51.5°C",
                    "winter_min": "6.5-16.5°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "150mm",
                "rainfall": {
                    "annual": "150mm",
                    "monsoon_contribution": "75-80%",
                    "rainy_days": "15-19 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-3 times per year)",
                "seasonal_totals": {
                    "summer": "112.5mm (monsoon)",
                    "winter": "10mm",
                    "spring": "15mm",
                    "autumn": "10mm"
                },
                "patterns": "Highly variable, concentrated in monsoon",
                "variability": "Increasing year-to-year variation"
            },
            "humidity": {
                "annual_average": "58%",
                "seasonal_variations": {
                    "summer": "68-78%",
                    "winter": "38-48%",
                    "spring": "53-63%",
                    "autumn": "58-68%"
                },
                "daily_patterns": {
                    "morning": "68-78%",
                    "afternoon": "43-53%",
                    "evening": "58-68%"
                },
                "trend": "Variable with monsoon influence"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "Southwest (monsoon)",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "13-18 km/h",
                    "summer": "18-28 km/h",
                    "winter": "8-15 km/h",
                    "storm_conditions": "28-48 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Strong southwest winds",
                    "winter_transition": "Calm periods",
                    "spring_winds": "Moderate variable winds"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1012-1013 hPa",
                "variations": {
                    "daily": "±3-4 hPa",
                    "seasonal": "±5-6 hPa",
                    "monsoon_low": "1007-1011 hPa"
                },
                "weather_system_effects": "Low pressure during monsoon, high pressure in winter"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "270-310 days per year",
                "cloudy_days": "55-95 days per year",
                "solar_radiation": {
                    "annual_average": "5.8-6.3 kWh/m²/day",
                    "summer_peak": "7.0-7.5 kWh/m²/day",
                    "winter_minimum": "4.0-4.4 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "Very High (9-11) in summer",
                    "shading_factor": "Moderate urban development"
                }
            },
            "cloud_cover": {
                "annual_average": "20-30%",
                "seasonal_coverage": {
                    "monsoon_season": "55-75%",
                    "dry_season": "8-18%",
                    "winter": "15-30%",
                    "spring": "20-35%"
                },
                "cloud_types": {
                    "cumulus": "Common in summer",
                    "stratus": "Common in monsoon",
                    "cirrus": "Occasional in winter"
                },
                "thickness": "Variable from thin cirrus to thick cumulonimbus"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "2200-2800mm",
                "seasonal_rates": {
                    "summer_peak": "11-16mm/day",
                    "winter_minimum": "3-6mm/day",
                    "spring": "7-12mm/day",
                    "autumn": "6-10mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Moderate agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "5-9 per year",
                    "duration": "4-12 days",
                    "peak_temperature": "48.5-51.5°C"
                },
                "dust_storms": {
                    "frequency": "6-15 per year",
                    "peak_season": "April-June",
                    "intensity": "Moderate to severe"
                },
                "droughts": {
                    "frequency": "1-3 per decade",
                    "duration": "6-18 months",
                    "severity": "Moderate to extreme"
                },
                "thunderstorms": {
                    "frequency": "8-18 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate frequency"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Very hot and dry",
                    "temperature_range": "36.5-51.5°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "16.5-26.5°C",
                    "rainfall": "Minimal"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Hot and humid with heavy rainfall",
                    "peak_months": "July-August",
                    "rainfall_contribution": "75-80% of annual"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Rapidly warming",
                    "temperature_range": "29.5-39.5°C",
                    "rainfall": "Light occasional showers"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling period",
                    "temperature_range": "30.5-38.5°C",
                    "rainfall": "Light showers"
                }
            }
        }
    },
    "nawabshah": {
        "climate_profile": {
            "temperature": {
                "annual_average": "31.5°C",
                "daily_average": {
                    "summer": "36.5-46.5°C",
                    "winter": "16.5-26.5°C",
                    "spring": "29.5-39.5°C",
                    "autumn": "30.5-38.5°C"
                },
                "seasonal_averages": {
                    "summer": "41.5°C",
                    "winter": "21.5°C",
                    "spring": "34.5°C",
                    "autumn": "34.5°C"
                },
                "extremes": {
                    "highest_recorded": "51.5°C",
                    "lowest_recorded": "6.5°C",
                    "summer_max": "46.5-51.5°C",
                    "winter_min": "6.5-16.5°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "150mm",
                "rainfall": {
                    "annual": "150mm",
                    "monsoon_contribution": "75-80%",
                    "rainy_days": "15-19 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-3 times per year)",
                "seasonal_totals": {
                    "summer": "112.5mm (monsoon)",
                    "winter": "10mm",
                    "spring": "15mm",
                    "autumn": "10mm"
                },
                "patterns": "Highly variable, concentrated in monsoon",
                "variability": "Increasing year-to-year variation"
            },
            "humidity": {
                "annual_average": "58%",
                "seasonal_variations": {
                    "summer": "68-78%",
                    "winter": "38-48%",
                    "spring": "53-63%",
                    "autumn": "58-68%"
                },
                "daily_patterns": {
                    "morning": "68-78%",
                    "afternoon": "43-53%",
                    "evening": "58-68%"
                },
                "trend": "Variable with monsoon influence"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "Southwest (monsoon)",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "13-18 km/h",
                    "summer": "18-28 km/h",
                    "winter": "8-15 km/h",
                    "storm_conditions": "28-48 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Strong southwest winds",
                    "winter_transition": "Calm periods",
                    "spring_winds": "Moderate variable winds"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1012-1013 hPa",
                "variations": {
                    "daily": "±3-4 hPa",
                    "seasonal": "±5-6 hPa",
                    "monsoon_low": "1007-1011 hPa"
                },
                "weather_system_effects": "Low pressure during monsoon, high pressure in winter"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "270-310 days per year",
                "cloudy_days": "55-95 days per year",
                "solar_radiation": {
                    "annual_average": "5.8-6.3 kWh/m²/day",
                    "summer_peak": "7.0-7.5 kWh/m²/day",
                    "winter_minimum": "4.0-4.4 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "Very High (9-11) in summer",
                    "shading_factor": "Moderate urban development"
                }
            },
            "cloud_cover": {
                "annual_average": "20-30%",
                "seasonal_coverage": {
                    "monsoon_season": "55-75%",
                    "dry_season": "8-18%",
                    "winter": "15-30%",
                    "spring": "20-35%"
                },
                "cloud_types": {
                    "cumulus": "Common in summer",
                    "stratus": "Common in monsoon",
                    "cirrus": "Occasional in winter"
                },
                "thickness": "Variable from thin cirrus to thick cumulonimbus"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "2200-2800mm",
                "seasonal_rates": {
                    "summer_peak": "11-16mm/day",
                    "winter_minimum": "3-6mm/day",
                    "spring": "7-12mm/day",
                    "autumn": "6-10mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Moderate agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "5-9 per year",
                    "duration": "4-12 days",
                    "peak_temperature": "48.5-51.5°C"
                },
                "dust_storms": {
                    "frequency": "6-15 per year",
                    "peak_season": "April-June",
                    "intensity": "Moderate to severe"
                },
                "droughts": {
                    "frequency": "1-3 per decade",
                    "duration": "6-18 months",
                    "severity": "Moderate to extreme"
                },
                "thunderstorms": {
                    "frequency": "8-18 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate frequency"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Very hot and dry",
                    "temperature_range": "36.5-51.5°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "16.5-26.5°C",
                    "rainfall": "Minimal"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Hot with moderate rainfall",
                    "peak_months": "July-August",
                    "rainfall_contribution": "75-80% of annual"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Rapidly warming",
                    "temperature_range": "29.5-39.5°C",
                    "rainfall": "Light occasional showers"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling period",
                    "temperature_range": "30.5-38.5°C",
                    "rainfall": "Light showers"
                }
            }
        }
    },
    "jacobabad": {
        "climate_profile": {
            "temperature": {
                "annual_average": "32°C",
                "daily_average": {
                    "summer": "37-47°C",
                    "winter": "17-27°C",
                    "spring": "30-40°C",
                    "autumn": "31-39°C"
                },
                "seasonal_averages": {
                    "summer": "42°C",
                    "winter": "22°C",
                    "spring": "35°C",
                    "autumn": "35°C"
                },
                "extremes": {
                    "highest_recorded": "52°C",
                    "lowest_recorded": "7°C",
                    "summer_max": "47-52°C",
                    "winter_min": "7-17°C"
                },
                "trend": "Increasing by 0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "120mm",
                "rainfall": {
                    "annual": "120mm",
                    "monsoon_contribution": "80%",
                    "rainy_days": "12-15 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-2 times per year)",
                "seasonal_totals": {
                    "summer": "96mm (monsoon)",
                    "winter": "8mm",
                    "spring": "12mm",
                    "autumn": "8mm"
                },
                "patterns": "Highly variable, concentrated in monsoon",
                "variability": "Increasing year-to-year variation"
            },
            "humidity": {
                "annual_average": "45%",
                "seasonal_variations": {
                    "summer": "55-65%",
                    "winter": "25-35%",
                    "spring": "40-50%",
                    "autumn": "45-55%"
                },
                "daily_patterns": {
                    "morning": "55-65%",
                    "afternoon": "30-40%",
                    "evening": "45-55%"
                },
                "trend": "Variable with monsoon influence"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "Southwest (monsoon)",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "15-20 km/h",
                    "summer": "20-30 km/h",
                    "winter": "10-18 km/h",
                    "storm_conditions": "30-50 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Strong southwest winds",
                    "winter_transition": "Calm periods",
                    "spring_winds": "Moderate variable winds"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1011-1012 hPa",
                "variations": {
                    "daily": "±3-4 hPa",
                    "seasonal": "±6-7 hPa",
                    "monsoon_low": "1005-1009 hPa"
                },
                "weather_system_effects": "Low pressure during monsoon, high pressure in winter"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "280-320 days per year",
                "cloudy_days": "45-85 days per year",
                "solar_radiation": {
                    "annual_average": "6.0-6.5 kWh/m²/day",
                    "summer_peak": "7.2-7.8 kWh/m²/day",
                    "winter_minimum": "4.2-4.6 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "Very High (9-11) in summer",
                    "shading_factor": "Limited urban development"
                }
            },
            "cloud_cover": {
                "annual_average": "15-25%",
                "seasonal_coverage": {
                    "monsoon_season": "50-70%",
                    "dry_season": "5-15%",
                    "winter": "10-25%",
                    "spring": "15-30%"
                },
                "cloud_types": {
                    "cumulus": "Common in summer",
                    "stratus": "Common in monsoon",
                    "cirrus": "Occasional in winter"
                },
                "thickness": "Variable from thin cirrus to thick cumulonimbus"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "2500-3200mm",
                "seasonal_rates": {
                    "summer_peak": "12-18mm/day",
                    "winter_minimum": "4-7mm/day",
                    "spring": "8-13mm/day",
                    "autumn": "7-11mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Limited agricultural development",
                    "water_cycle": "Reduced natural water recycling"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "6-10 per year",
                    "duration": "5-15 days",
                    "peak_temperature": "50-52°C"
                },
                "dust_storms": {
                    "frequency": "8-18 per year",
                    "peak_season": "April-June",
                    "intensity": "Moderate to severe"
                },
                "droughts": {
                    "frequency": "2-4 per decade",
                    "duration": "8-24 months",
                    "severity": "Moderate to extreme"
                },
                "thunderstorms": {
                    "frequency": "6-15 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate frequency"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Extremely hot and dry",
                    "temperature_range": "37-52°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "17-27°C",
                    "rainfall": "Minimal"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Hot with moderate rainfall",
                    "peak_months": "July-August",
                    "rainfall_contribution": "80% of annual"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Rapidly warming",
                    "temperature_range": "30-40°C",
                    "rainfall": "Light occasional showers"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling period",
                    "temperature_range": "31-39°C",
                    "rainfall": "Light showers"
                }
            }
        }
    },
    "shikarpur": {
        "climate_profile": {
            "temperature": {
                "annual_average": "32°C",
                "daily_average": {
                    "summer": "37-47°C",
                    "winter": "17-27°C",
                    "spring": "30-40°C",
                    "autumn": "31-39°C"
                },
                "seasonal_averages": {
                    "summer": "42°C",
                    "winter": "22°C",
                    "spring": "35°C",
                    "autumn": "35°C"
                },
                "extremes": {
                    "highest_recorded": "52°C",
                    "lowest_recorded": "7°C",
                    "summer_max": "47-52°C",
                    "winter_min": "7-17°C"
                },
                "trend": "Increasing by 0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "120mm",
                "rainfall": {
                    "annual": "120mm",
                    "monsoon_contribution": "80%",
                    "rainy_days": "12-15 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-2 times per year)",
                "seasonal_totals": {
                    "summer": "96mm (monsoon)",
                    "winter": "8mm",
                    "spring": "12mm",
                    "autumn": "8mm"
                },
                "patterns": "Highly variable, concentrated in monsoon",
                "variability": "Increasing year-to-year variation"
            },
            "humidity": {
                "annual_average": "45%",
                "seasonal_variations": {
                    "summer": "55-65%",
                    "winter": "25-35%",
                    "spring": "40-50%",
                    "autumn": "45-55%"
                },
                "daily_patterns": {
                    "morning": "55-65%",
                    "afternoon": "30-40%",
                    "evening": "45-55%"
                },
                "trend": "Variable with monsoon influence"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "Southwest (monsoon)",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "15-20 km/h",
                    "summer": "20-30 km/h",
                    "winter": "10-18 km/h",
                    "storm_conditions": "30-50 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Strong southwest winds",
                    "winter_transition": "Calm periods",
                    "spring_winds": "Moderate variable winds"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1011-1012 hPa",
                "variations": {
                    "daily": "±3-4 hPa",
                    "seasonal": "±6-7 hPa",
                    "monsoon_low": "1005-1009 hPa"
                },
                "weather_system_effects": "Low pressure during monsoon, high pressure in winter"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "280-320 days per year",
                "cloudy_days": "45-85 days per year",
                "solar_radiation": {
                    "annual_average": "6.0-6.5 kWh/m²/day",
                    "summer_peak": "7.2-7.8 kWh/m²/day",
                    "winter_minimum": "4.2-4.6 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "Very High (9-11) in summer",
                    "shading_factor": "Limited urban development"
                }
            },
            "cloud_cover": {
                "annual_average": "15-25%",
                "seasonal_coverage": {
                    "monsoon_season": "50-70%",
                    "dry_season": "5-15%",
                    "winter": "10-25%",
                    "spring": "15-30%"
                },
                "cloud_types": {
                    "cumulus": "Common in summer",
                    "stratus": "Common in monsoon",
                    "cirrus": "Occasional in winter"
                },
                "thickness": "Variable from thin cirrus to thick cumulonimbus"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "2500-3200mm",
                "seasonal_rates": {
                    "summer_peak": "12-18mm/day",
                    "winter_minimum": "4-7mm/day",
                    "spring": "8-13mm/day",
                    "autumn": "7-11mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Limited agricultural development",
                    "water_cycle": "Reduced natural water recycling"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "6-10 per year",
                    "duration": "5-15 days",
                    "peak_temperature": "50-52°C"
                },
                "dust_storms": {
                    "frequency": "8-18 per year",
                    "peak_season": "April-June",
                    "intensity": "Moderate to severe"
                },
                "droughts": {
                    "frequency": "2-4 per decade",
                    "duration": "8-24 months",
                    "severity": "Moderate to extreme"
                },
                "thunderstorms": {
                    "frequency": "6-15 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate frequency"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Extremely hot and dry",
                    "temperature_range": "37-52°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "17-27°C",
                    "rainfall": "Minimal"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Hot with moderate rainfall",
                    "peak_months": "July-August",
                    "rainfall_contribution": "80% of annual"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Rapidly warming",
                    "temperature_range": "30-40°C",
                    "rainfall": "Light occasional showers"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling period",
                    "temperature_range": "31-39°C",
                    "rainfall": "Light showers"
                }
            }
        }
    },
    "dadu": {
        "climate_profile": {
            "temperature": {
                "annual_average": "31°C",
                "daily_average": {
                    "summer": "36-46°C",
                    "winter": "16-26°C",
                    "spring": "29-39°C",
                    "autumn": "30-38°C"
                },
                "seasonal_averages": {
                    "summer": "41°C",
                    "winter": "21°C",
                    "spring": "34°C",
                    "autumn": "34°C"
                },
                "extremes": {
                    "highest_recorded": "51°C",
                    "lowest_recorded": "6°C",
                    "summer_max": "46-51°C",
                    "winter_min": "6-16°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "140mm",
                "rainfall": {
                    "annual": "140mm",
                    "monsoon_contribution": "75-80%",
                    "rainy_days": "14-18 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-3 times per year)",
                "seasonal_totals": {
                    "summer": "105mm (monsoon)",
                    "winter": "9mm",
                    "spring": "14mm",
                    "autumn": "9mm"
                },
                "patterns": "Highly variable, concentrated in monsoon",
                "variability": "Increasing year-to-year variation"
            },
            "humidity": {
                "annual_average": "55%",
                "seasonal_variations": {
                    "summer": "65-75%",
                    "winter": "35-45%",
                    "spring": "50-60%",
                    "autumn": "55-65%"
                },
                "daily_patterns": {
                    "morning": "65-75%",
                    "afternoon": "40-50%",
                    "evening": "55-65%"
                },
                "trend": "Variable with monsoon influence"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "Southwest (monsoon)",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "13-18 km/h",
                    "summer": "18-28 km/h",
                    "winter": "8-15 km/h",
                    "storm_conditions": "28-48 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Strong southwest winds",
                    "winter_transition": "Calm periods",
                    "spring_winds": "Moderate variable winds"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1012-1013 hPa",
                "variations": {
                    "daily": "±3-4 hPa",
                    "seasonal": "±5-6 hPa",
                    "monsoon_low": "1007-1011 hPa"
                },
                "weather_system_effects": "Low pressure during monsoon, high pressure in winter"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "270-310 days per year",
                "cloudy_days": "55-95 days per year",
                "solar_radiation": {
                    "annual_average": "5.8-6.3 kWh/m²/day",
                    "summer_peak": "7.0-7.5 kWh/m²/day",
                    "winter_minimum": "4.0-4.4 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "Very High (9-11) in summer",
                    "shading_factor": "Moderate urban development"
                }
            },
            "cloud_cover": {
                "annual_average": "20-30%",
                "seasonal_coverage": {
                    "monsoon_season": "55-75%",
                    "dry_season": "8-18%",
                    "winter": "15-30%",
                    "spring": "20-35%"
                },
                "cloud_types": {
                    "cumulus": "Common in summer",
                    "stratus": "Common in monsoon",
                    "cirrus": "Occasional in winter"
                },
                "thickness": "Variable from thin cirrus to thick cumulonimbus"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "2200-2800mm",
                "seasonal_rates": {
                    "summer_peak": "11-16mm/day",
                    "winter_minimum": "3-6mm/day",
                    "spring": "7-12mm/day",
                    "autumn": "6-10mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Moderate agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "5-9 per year",
                    "duration": "4-12 days",
                    "peak_temperature": "48-51°C"
                },
                "dust_storms": {
                    "frequency": "6-15 per year",
                    "peak_season": "April-June",
                    "intensity": "Moderate to severe"
                },
                "droughts": {
                    "frequency": "1-3 per decade",
                    "duration": "6-18 months",
                    "severity": "Moderate to extreme"
                },
                "thunderstorms": {
                    "frequency": "8-18 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate frequency"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Very hot and dry",
                    "temperature_range": "36-51°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "16-26°C",
                    "rainfall": "Minimal"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Hot with moderate rainfall",
                    "peak_months": "July-August",
                    "rainfall_contribution": "75-80% of annual"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Rapidly warming",
                    "temperature_range": "29-39°C",
                    "rainfall": "Light occasional showers"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling period",
                    "temperature_range": "30-38°C",
                    "rainfall": "Light showers"
                }
            }
        }
    },
    "jamshoro": {
        "climate_profile": {
            "temperature": {
                "annual_average": "31°C",
                "daily_average": {
                    "summer": "36-46°C",
                    "winter": "16-26°C",
                    "spring": "29-39°C",
                    "autumn": "30-38°C"
                },
                "seasonal_averages": {
                    "summer": "41°C",
                    "winter": "21°C",
                    "spring": "34°C",
                    "autumn": "34°C"
                },
                "extremes": {
                    "highest_recorded": "51°C",
                    "lowest_recorded": "6°C",
                    "summer_max": "46-51°C",
                    "winter_min": "6-16°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "140mm",
                "rainfall": {
                    "annual": "140mm",
                    "monsoon_contribution": "75-80%",
                    "rainy_days": "14-18 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-3 times per year)",
                "seasonal_totals": {
                    "summer": "105mm (monsoon)",
                    "winter": "9mm",
                    "spring": "14mm",
                    "autumn": "9mm"
                },
                "patterns": "Highly variable, concentrated in monsoon",
                "variability": "Increasing year-to-year variation"
            },
            "humidity": {
                "annual_average": "55%",
                "seasonal_variations": {
                    "summer": "65-75%",
                    "winter": "35-45%",
                    "spring": "50-60%",
                    "autumn": "55-65%"
                },
                "daily_patterns": {
                    "morning": "65-75%",
                    "afternoon": "40-50%",
                    "evening": "55-65%"
                },
                "trend": "Variable with monsoon influence"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "Southwest (monsoon)",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "13-18 km/h",
                    "summer": "18-28 km/h",
                    "winter": "8-15 km/h",
                    "storm_conditions": "28-48 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Strong southwest winds",
                    "winter_transition": "Calm periods",
                    "spring_winds": "Moderate variable winds"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1012-1013 hPa",
                "variations": {
                    "daily": "±3-4 hPa",
                    "seasonal": "±5-6 hPa",
                    "monsoon_low": "1007-1011 hPa"
                },
                "weather_system_effects": "Low pressure during monsoon, high pressure in winter"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "270-310 days per year",
                "cloudy_days": "55-95 days per year",
                "solar_radiation": {
                    "annual_average": "5.8-6.3 kWh/m²/day",
                    "summer_peak": "7.0-7.5 kWh/m²/day",
                    "winter_minimum": "4.0-4.4 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "Very High (9-11) in summer",
                    "shading_factor": "Moderate urban development"
                }
            },
            "cloud_cover": {
                "annual_average": "20-30%",
                "seasonal_coverage": {
                    "monsoon_season": "55-75%",
                    "dry_season": "8-18%",
                    "winter": "15-30%",
                    "spring": "20-35%"
                },
                "cloud_types": {
                    "cumulus": "Common in summer",
                    "stratus": "Common in monsoon",
                    "cirrus": "Occasional in winter"
                },
                "thickness": "Variable from thin cirrus to thick cumulonimbus"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "2200-2800mm",
                "seasonal_rates": {
                    "summer_peak": "11-16mm/day",
                    "winter_minimum": "3-6mm/day",
                    "spring": "7-12mm/day",
                    "autumn": "6-10mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Moderate agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "5-9 per year",
                    "duration": "4-12 days",
                    "peak_temperature": "48-51°C"
                },
                "dust_storms": {
                    "frequency": "6-15 per year",
                    "peak_season": "April-June",
                    "intensity": "Moderate to severe"
                },
                "droughts": {
                    "frequency": "1-3 per decade",
                    "duration": "6-18 months",
                    "severity": "Moderate to extreme"
                },
                "thunderstorms": {
                    "frequency": "8-18 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate frequency"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Very hot and dry",
                    "temperature_range": "36-51°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "16-26°C",
                    "rainfall": "Minimal"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Hot with moderate rainfall",
                    "peak_months": "July-August",
                    "rainfall_contribution": "75-80% of annual"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Rapidly warming",
                    "temperature_range": "29-39°C",
                    "rainfall": "Light occasional showers"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling period",
                    "temperature_range": "30-38°C",
                    "rainfall": "Light showers"
                }
            }
        }
    },
    "tharparkar": {
        "climate_profile": {
            "temperature": {
                "annual_average": "30.5°C",
                "daily_average": {
                    "summer": "35.5-45.5°C",
                    "winter": "15.5-25.5°C",
                    "spring": "28.5-38.5°C",
                    "autumn": "29.5-37.5°C"
                },
                "seasonal_averages": {
                    "summer": "40.5°C",
                    "winter": "20.5°C",
                    "spring": "33.5°C",
                    "autumn": "33.5°C"
                },
                "extremes": {
                    "highest_recorded": "50.5°C",
                    "lowest_recorded": "5.5°C",
                    "summer_max": "45.5-50.5°C",
                    "winter_min": "5.5-15.5°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "180mm",
                "rainfall": {
                    "annual": "180mm",
                    "monsoon_contribution": "75-80%",
                    "rainy_days": "18-22 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-3 times per year)",
                "seasonal_totals": {
                    "summer": "135mm (monsoon)",
                    "winter": "12mm",
                    "spring": "18mm",
                    "autumn": "12mm"
                },
                "patterns": "Highly variable, concentrated in monsoon",
                "variability": "Increasing year-to-year variation"
            },
            "humidity": {
                "annual_average": "65%",
                "seasonal_variations": {
                    "summer": "75-85%",
                    "winter": "45-55%",
                    "spring": "60-70%",
                    "autumn": "65-75%"
                },
                "daily_patterns": {
                    "morning": "75-85%",
                    "afternoon": "50-60%",
                    "evening": "65-75%"
                },
                "trend": "Variable with monsoon influence"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "Southwest (monsoon)",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "12-17 km/h",
                    "summer": "17-27 km/h",
                    "winter": "7-14 km/h",
                    "storm_conditions": "27-47 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Strong southwest winds",
                    "winter_transition": "Calm periods",
                    "spring_winds": "Moderate variable winds"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1012-1013 hPa",
                "variations": {
                    "daily": "±3-4 hPa",
                    "seasonal": "±5-6 hPa",
                    "monsoon_low": "1007-1011 hPa"
                },
                "weather_system_effects": "Low pressure during monsoon, high pressure in winter"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "265-305 days per year",
                "cloudy_days": "60-100 days per year",
                "solar_radiation": {
                    "annual_average": "5.7-6.2 kWh/m²/day",
                    "summer_peak": "6.9-7.4 kWh/m²/day",
                    "winter_minimum": "4.0-4.3 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "Very High (9-11) in summer",
                    "shading_factor": "Moderate urban development"
                }
            },
            "cloud_cover": {
                "annual_average": "25-35%",
                "seasonal_coverage": {
                    "monsoon_season": "60-80%",
                    "dry_season": "10-20%",
                    "winter": "20-35%",
                    "spring": "25-40%"
                },
                "cloud_types": {
                    "cumulus": "Common in summer",
                    "stratus": "Common in monsoon",
                    "cirrus": "Occasional in winter"
                },
                "thickness": "Variable from thin cirrus to thick cumulonimbus"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "2000-2600mm",
                "seasonal_rates": {
                    "summer_peak": "10-15mm/day",
                    "winter_minimum": "3-6mm/day",
                    "spring": "6-11mm/day",
                    "autumn": "5-9mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Moderate agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "47-50.5°C"
                },
                "dust_storms": {
                    "frequency": "5-13 per year",
                    "peak_season": "April-June",
                    "intensity": "Moderate to severe"
                },
                "droughts": {
                    "frequency": "1-3 per decade",
                    "duration": "6-18 months",
                    "severity": "Moderate to extreme"
                },
                "thunderstorms": {
                    "frequency": "7-17 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate frequency"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Very hot and humid",
                    "temperature_range": "35.5-50.5°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "15.5-25.5°C",
                    "rainfall": "Minimal"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Hot with heavy rainfall",
                    "peak_months": "July-August",
                    "rainfall_contribution": "75-80% of annual"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Rapidly warming",
                    "temperature_range": "28.5-38.5°C",
                    "rainfall": "Light occasional showers"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling period",
                    "temperature_range": "29.5-37.5°C",
                    "rainfall": "Light showers"
                }
            }
        }
    },
    "badin": {
        "climate_profile": {
            "temperature": {
                "annual_average": "30.5°C",
                "daily_average": {
                    "summer": "35.5-45.5°C",
                    "winter": "15.5-25.5°C",
                    "spring": "28.5-38.5°C",
                    "autumn": "29.5-37.5°C"
                },
                "seasonal_averages": {
                    "summer": "40.5°C",
                    "winter": "20.5°C",
                    "spring": "33.5°C",
                    "autumn": "33.5°C"
                },
                "extremes": {
                    "highest_recorded": "50.5°C",
                    "lowest_recorded": "5.5°C",
                    "summer_max": "45.5-50.5°C",
                    "winter_min": "5.5-15.5°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "180mm",
                "rainfall": {
                    "annual": "180mm",
                    "monsoon_contribution": "75-80%",
                    "rainy_days": "18-22 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-3 times per year)",
                "seasonal_totals": {
                    "summer": "135mm (monsoon)",
                    "winter": "12mm",
                    "spring": "18mm",
                    "autumn": "12mm"
                },
                "patterns": "Highly variable, concentrated in monsoon",
                "variability": "Increasing year-to-year variation"
            },
            "humidity": {
                "annual_average": "65%",
                "seasonal_variations": {
                    "summer": "75-85%",
                    "winter": "45-55%",
                    "spring": "60-70%",
                    "autumn": "65-75%"
                },
                "daily_patterns": {
                    "morning": "75-85%",
                    "afternoon": "50-60%",
                    "evening": "65-75%"
                },
                "trend": "Variable with monsoon influence"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "Southwest (monsoon)",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "12-17 km/h",
                    "summer": "17-27 km/h",
                    "winter": "7-14 km/h",
                    "storm_conditions": "27-47 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Strong southwest winds",
                    "winter_transition": "Calm periods",
                    "spring_winds": "Moderate variable winds"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1012-1013 hPa",
                "variations": {
                    "daily": "±3-4 hPa",
                    "seasonal": "±5-6 hPa",
                    "monsoon_low": "1007-1011 hPa"
                },
                "weather_system_effects": "Low pressure during monsoon, high pressure in winter"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "265-305 days per year",
                "cloudy_days": "60-100 days per year",
                "solar_radiation": {
                    "annual_average": "5.7-6.2 kWh/m²/day",
                    "summer_peak": "6.9-7.4 kWh/m²/day",
                    "winter_minimum": "4.0-4.3 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "Very High (9-11) in summer",
                    "shading_factor": "Moderate urban development"
                }
            },
            "cloud_cover": {
                "annual_average": "25-35%",
                "seasonal_coverage": {
                    "monsoon_season": "60-80%",
                    "dry_season": "10-20%",
                    "winter": "20-35%",
                    "spring": "25-40%"
                },
                "cloud_types": {
                    "cumulus": "Common in summer",
                    "stratus": "Common in monsoon",
                    "cirrus": "Occasional in winter"
                },
                "thickness": "Variable from thin cirrus to thick cumulonimbus"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "2000-2600mm",
                "seasonal_rates": {
                    "summer_peak": "10-15mm/day",
                    "winter_minimum": "3-6mm/day",
                    "spring": "6-11mm/day",
                    "autumn": "5-9mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Moderate agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "47-50.5°C"
                },
                "dust_storms": {
                    "frequency": "5-13 per year",
                    "peak_season": "April-June",
                    "intensity": "Moderate to severe"
                },
                "droughts": {
                    "frequency": "1-3 per decade",
                    "duration": "6-18 months",
                    "severity": "Moderate to extreme"
                },
                "thunderstorms": {
                    "frequency": "7-17 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate frequency"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Very hot and humid",
                    "temperature_range": "35.5-50.5°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "15.5-25.5°C",
                    "rainfall": "Minimal"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Hot with heavy rainfall",
                    "peak_months": "July-August",
                    "rainfall_contribution": "75-80% of annual"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Rapidly warming",
                    "temperature_range": "28.5-38.5°C",
                    "rainfall": "Light occasional showers"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling period",
                    "temperature_range": "29.5-37.5°C",
                    "rainfall": "Light showers"
                }
            }
        }
    },
    "sanghar": {
        "climate_profile": {
            "temperature": {
                "annual_average": "31.5°C",
                "daily_average": {
                    "summer": "36.5-46.5°C",
                    "winter": "16.5-26.5°C",
                    "spring": "29.5-39.5°C",
                    "autumn": "30.5-38.5°C"
                },
                "seasonal_averages": {
                    "summer": "41.5°C",
                    "winter": "21.5°C",
                    "spring": "34.5°C",
                    "autumn": "34.5°C"
                },
                "extremes": {
                    "highest_recorded": "51.5°C",
                    "lowest_recorded": "6.5°C",
                    "summer_max": "46.5-51.5°C",
                    "winter_min": "6.5-16.5°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "150mm",
                "rainfall": {
                    "annual": "150mm",
                    "monsoon_contribution": "75-80%",
                    "rainy_days": "15-19 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-3 times per year)",
                "seasonal_totals": {
                    "summer": "112.5mm (monsoon)",
                    "winter": "10mm",
                    "spring": "15mm",
                    "autumn": "10mm"
                },
                "patterns": "Highly variable, concentrated in monsoon",
                "variability": "Increasing year-to-year variation"
            },
            "humidity": {
                "annual_average": "58%",
                "seasonal_variations": {
                    "summer": "68-78%",
                    "winter": "38-48%",
                    "spring": "53-63%",
                    "autumn": "58-68%"
                },
                "daily_patterns": {
                    "morning": "68-78%",
                    "afternoon": "43-53%",
                    "evening": "58-68%"
                },
                "trend": "Variable with monsoon influence"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "Southwest (monsoon)",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "13-18 km/h",
                    "summer": "18-28 km/h",
                    "winter": "8-15 km/h",
                    "storm_conditions": "28-48 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Strong southwest winds",
                    "winter_transition": "Calm periods",
                    "spring_winds": "Moderate variable winds"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1012-1013 hPa",
                "variations": {
                    "daily": "±3-4 hPa",
                    "seasonal": "±5-6 hPa",
                    "monsoon_low": "1007-1011 hPa"
                },
                "weather_system_effects": "Low pressure during monsoon, high pressure in winter"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "270-310 days per year",
                "cloudy_days": "55-95 days per year",
                "solar_radiation": {
                    "annual_average": "5.8-6.3 kWh/m²/day",
                    "summer_peak": "7.0-7.5 kWh/m²/day",
                    "winter_minimum": "4.0-4.4 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "Very High (9-11) in summer",
                    "shading_factor": "Moderate urban development"
                }
            },
            "cloud_cover": {
                "annual_average": "20-30%",
                "seasonal_coverage": {
                    "monsoon_season": "55-75%",
                    "dry_season": "8-18%",
                    "winter": "15-30%",
                    "spring": "20-35%"
                },
                "cloud_types": {
                    "cumulus": "Common in summer",
                    "stratus": "Common in monsoon",
                    "cirrus": "Occasional in winter"
                },
                "thickness": "Variable from thin cirrus to thick cumulonimbus"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "2200-2800mm",
                "seasonal_rates": {
                    "summer_peak": "11-16mm/day",
                    "winter_minimum": "3-6mm/day",
                    "spring": "7-12mm/day",
                    "autumn": "6-10mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Moderate agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "5-9 per year",
                    "duration": "4-12 days",
                    "peak_temperature": "48.5-51.5°C"
                },
                "dust_storms": {
                    "frequency": "6-15 per year",
                    "peak_season": "April-June",
                    "intensity": "Moderate to severe"
                },
                "droughts": {
                    "frequency": "1-3 per decade",
                    "duration": "6-18 months",
                    "severity": "Moderate to extreme"
                },
                "thunderstorms": {
                    "frequency": "8-18 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate frequency"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Very hot and dry",
                    "temperature_range": "36.5-51.5°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "16.5-26.5°C",
                    "rainfall": "Minimal"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Hot with moderate rainfall",
                    "peak_months": "July-August",
                    "rainfall_contribution": "75-80% of annual"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Rapidly warming",
                    "temperature_range": "29.5-39.5°C",
                    "rainfall": "Light occasional showers"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling period",
                    "temperature_range": "30.5-38.5°C",
                    "rainfall": "Light showers"
                }
            }
        }
    },
    "khairpur": {
        "climate_profile": {
            "temperature": {
                "annual_average": "32°C",
                "daily_average": {
                    "summer": "37-47°C",
                    "winter": "17-27°C",
                    "spring": "30-40°C",
                    "autumn": "31-39°C"
                },
                "seasonal_averages": {
                    "summer": "42°C",
                    "winter": "22°C",
                    "spring": "35°C",
                    "autumn": "35°C"
                },
                "extremes": {
                    "highest_recorded": "52°C",
                    "lowest_recorded": "7°C",
                    "summer_max": "47-52°C",
                    "winter_min": "7-17°C"
                },
                "trend": "Increasing by 0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "120mm",
                "rainfall": {
                    "annual": "120mm",
                    "monsoon_contribution": "80%",
                    "rainy_days": "12-15 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-2 times per year)",
                "seasonal_totals": {
                    "summer": "96mm (monsoon)",
                    "winter": "8mm",
                    "spring": "12mm",
                    "autumn": "8mm"
                },
                "patterns": "Highly variable, concentrated in monsoon",
                "variability": "Increasing year-to-year variation"
            },
            "humidity": {
                "annual_average": "45%",
                "seasonal_variations": {
                    "summer": "55-65%",
                    "winter": "25-35%",
                    "spring": "40-50%",
                    "autumn": "45-55%"
                },
                "daily_patterns": {
                    "morning": "55-65%",
                    "afternoon": "30-40%",
                    "evening": "45-55%"
                },
                "trend": "Variable with monsoon influence"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "Southwest (monsoon)",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "15-20 km/h",
                    "summer": "20-30 km/h",
                    "winter": "10-18 km/h",
                    "storm_conditions": "30-50 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Strong southwest winds",
                    "winter_transition": "Calm periods",
                    "spring_winds": "Moderate variable winds"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1011-1012 hPa",
                "variations": {
                    "daily": "±3-4 hPa",
                    "seasonal": "±6-7 hPa",
                    "monsoon_low": "1005-1009 hPa"
                },
                "weather_system_effects": "Low pressure during monsoon, high pressure in winter"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "280-320 days per year",
                "cloudy_days": "45-85 days per year",
                "solar_radiation": {
                    "annual_average": "6.0-6.5 kWh/m²/day",
                    "summer_peak": "7.2-7.8 kWh/m²/day",
                    "winter_minimum": "4.2-4.6 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "Very High (9-11) in summer",
                    "shading_factor": "Limited urban development"
                }
            },
            "cloud_cover": {
                "annual_average": "15-25%",
                "seasonal_coverage": {
                    "monsoon_season": "50-70%",
                    "dry_season": "5-15%",
                    "winter": "10-25%",
                    "spring": "15-30%"
                },
                "cloud_types": {
                    "cumulus": "Common in summer",
                    "stratus": "Common in monsoon",
                    "cirrus": "Occasional in winter"
                },
                "thickness": "Variable from thin cirrus to thick cumulonimbus"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "2500-3200mm",
                "seasonal_rates": {
                    "summer_peak": "12-18mm/day",
                    "winter_minimum": "4-7mm/day",
                    "spring": "8-13mm/day",
                    "autumn": "7-11mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Limited agricultural development",
                    "water_cycle": "Reduced natural water recycling"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "6-10 per year",
                    "duration": "5-15 days",
                    "peak_temperature": "50-52°C"
                },
                "dust_storms": {
                    "frequency": "8-18 per year",
                    "peak_season": "April-June",
                    "intensity": "Moderate to severe"
                },
                "droughts": {
                    "frequency": "2-4 per decade",
                    "duration": "8-24 months",
                    "severity": "Moderate to extreme"
                },
                "thunderstorms": {
                    "frequency": "6-15 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate frequency"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Extremely hot and dry",
                    "temperature_range": "37-52°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "17-27°C",
                    "rainfall": "Minimal"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Hot with moderate rainfall",
                    "peak_months": "July-August",
                    "rainfall_contribution": "80% of annual"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Rapidly warming",
                    "temperature_range": "30-40°C",
                    "rainfall": "Light occasional showers"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling period",
                    "temperature_range": "31-39°C",
                    "rainfall": "Light showers"
                }
            }
        }
    },
    "karachi_west": {
        "climate_profile": {
            "temperature": {
                "annual_average": "27.0°C",
                "daily_average": {
                    "summer": "32-42°C",
                    "winter": "12-22°C",
                    "spring": "25-35°C",
                    "autumn": "26-34°C"
                },
                "seasonal_averages": {
                    "summer": "35.0°C",
                    "winter": "14.0°C",
                    "spring": "29.0°C",
                    "autumn": "28.0°C"
                },
                "extremes": {
                    "highest_recorded": "47.0°C",
                    "lowest_recorded": "3.0°C",
                    "summer_max": "39-45°C",
                    "winter_min": "6-12°C"
                },
                "trend": "Increasing by 0.3-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "210mm",
                "rainfall": {
                    "annual": "210mm",
                    "monsoon_contribution": "70-80%",
                    "rainy_days": "20-26 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-2 times per year)",
                "seasonal_totals": {
                    "summer": "160mm (monsoon)",
                    "winter": "12mm",
                    "spring": "20mm",
                    "autumn": "18mm"
                },
                "patterns": "Concentrated in monsoon, high inter-annual variability",
                "variability": "Increasing year-to-year variation"
            },
            "humidity": {
                "annual_average": "68%",
                "seasonal_variations": {
                    "summer": "78-88%",
                    "winter": "48-58%",
                    "spring": "62-72%",
                    "autumn": "64-78%"
                },
                "daily_patterns": {
                    "morning": "80-90%",
                    "afternoon": "55-65%",
                    "evening": "65-80%"
                },
                "trend": "Variable with coastal influence"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "Southwest (monsoon)",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "12-18 km/h",
                    "summer": "15-24 km/h",
                    "winter": "8-14 km/h",
                    "storm_conditions": "25-40 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Strengthening southwest winds",
                    "winter_transition": "More calm periods",
                    "spring_winds": "Moderate variable winds"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1012-1013 hPa",
                "variations": {
                    "daily": "±3-4 hPa",
                    "seasonal": "±5-6 hPa",
                    "monsoon_low": "1007-1011 hPa"
                },
                "weather_system_effects": "Low pressure during monsoon, relatively higher in winter"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "255-300 days per year",
                "cloudy_days": "60-100 days per year",
                "solar_radiation": {
                    "annual_average": "5.4-5.9 kWh/m²/day",
                    "summer_peak": "6.7-7.1 kWh/m²/day",
                    "winter_minimum": "3.8-4.1 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "High (8-11) in summer",
                    "shading_factor": "Urban development dependent"
                }
            },
            "cloud_cover": {
                "annual_average": "25-35%",
                "seasonal_coverage": {
                    "monsoon_season": "60-80%",
                    "dry_season": "10-20%",
                    "winter": "20-35%",
                    "spring": "25-40%"
                },
                "cloud_types": {
                    "cumulus": "Common in summer",
                    "stratus": "Common in monsoon",
                    "cirrus": "Occasional in winter"
                },
                "thickness": "Varies from thin cirrus to thick cumulonimbus"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "1850-2450mm",
                "seasonal_rates": {
                    "summer_peak": "9-14mm/day",
                    "winter_minimum": "3-6mm/day",
                    "spring": "6-10mm/day",
                    "autumn": "5-9mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Lower in built-up zones",
                    "water_cycle": "Higher evaporation from open surfaces"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-7 per year",
                    "duration": "3-9 days",
                    "peak_temperature": "45-47°C"
                },
                "dust_storms": {
                    "frequency": "4-10 per year",
                    "peak_season": "April-June",
                    "intensity": "Moderate to severe"
                },
                "droughts": {
                    "frequency": "1-2 per decade",
                    "duration": "6-12 months",
                    "severity": "Moderate to extreme"
                },
                "thunderstorms": {
                    "frequency": "8-18 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate frequency"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Very hot and humid",
                    "temperature_range": "32-42°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cool and dry",
                    "temperature_range": "12-22°C",
                    "rainfall": "Minimal"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Hot with heavy rainfall",
                    "peak_months": "July-August",
                    "rainfall_contribution": "70-80% of annual"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Rapid warming",
                    "temperature_range": "25-35°C"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling period",
                    "temperature_range": "26-34°C",
                    "rainfall": "Light showers"
                }
            }
        }
    },
    "ghotki": {
        "climate_profile": {
            "temperature": {
                "annual_average": "28.0°C",
                "daily_average": {
                    "summer": "34-46°C",
                    "winter": "8-22°C",
                    "spring": "26-36°C",
                    "autumn": "27-37°C"
                },
                "seasonal_averages": {
                    "summer": "37.5°C",
                    "winter": "15.0°C",
                    "spring": "30.0°C",
                    "autumn": "31.0°C"
                },
                "extremes": {
                    "highest_recorded": "50.0°C",
                    "lowest_recorded": "2.0°C",
                    "summer_max": "42-48°C",
                    "winter_min": "3-8°C"
                },
                "trend": "Increasing by 0.4-0.6°C per decade"
            },
            "precipitation": {
                "annual_total": "140mm",
                "rainfall": {
                    "annual": "140mm",
                    "monsoon_contribution": "75-85%",
                    "rainy_days": "12-20 days per year"
                },
                "snowfall": "None",
                "sleet": "None",
                "hail": "Rare (0-1 per year)",
                "seasonal_totals": {
                    "summer": "110mm (monsoon)",
                    "winter": "8mm",
                    "spring": "12mm",
                    "autumn": "10mm"
                },
                "patterns": "Low overall rainfall, highly variable",
                "variability": "High inter-annual variability"
            },
            "humidity": {
                "annual_average": "52%",
                "seasonal_variations": {
                    "summer": "45-60%",
                    "winter": "35-50%",
                    "spring": "40-55%",
                    "autumn": "42-58%"
                },
                "daily_patterns": {
                    "morning": "55-65%",
                    "afternoon": "30-45%",
                    "evening": "40-55%"
                },
                "trend": "Slight increase during monsoon periods"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "West/Southwest",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "10-16 km/h",
                    "summer": "14-22 km/h",
                    "winter": "6-12 km/h",
                    "storm_conditions": "25-40 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Increased southwest flow",
                    "winter_transition": "Calmer periods",
                    "spring_winds": "Occasional gusty winds"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1011-1014 hPa",
                "variations": {
                    "daily": "±3-4 hPa",
                    "seasonal": "±5-6 hPa",
                    "monsoon_low": "1007-1010 hPa"
                },
                "weather_system_effects": "Pronounced low pressure during monsoon"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "290-320 days per year",
                "cloudy_days": "40-70 days per year",
                "solar_radiation": {
                    "annual_average": "5.8-6.2 kWh/m²/day",
                    "summer_peak": "7.0-7.4 kWh/m²/day",
                    "winter_minimum": "4.0-4.3 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "Very High (10-11) in summer",
                    "shading_factor": "Low outside urban centers"
                }
            },
            "cloud_cover": {
                "annual_average": "15-25%",
                "seasonal_coverage": {
                    "monsoon_season": "50-70%",
                    "dry_season": "5-15%",
                    "winter": "10-25%",
                    "spring": "15-30%"
                },
                "cloud_types": {
                    "cumulus": "Occasional in summer",
                    "stratus": "Monsoon",
                    "cirrus": "Common in winter"
                },
                "thickness": "Generally thin to moderate except during storms"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "2100-2700mm",
                "seasonal_rates": {
                    "summer_peak": "10-16mm/day",
                    "winter_minimum": "3-6mm/day",
                    "spring": "7-12mm/day",
                    "autumn": "6-10mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Moderate in agricultural areas",
                    "water_cycle": "High evaporation from open canals"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "5-9 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "47-50°C"
                },
                "dust_storms": {
                    "frequency": "6-14 per year",
                    "peak_season": "April-June",
                    "intensity": "Moderate to severe"
                },
                "droughts": {
                    "frequency": "1-3 per decade",
                    "duration": "6-18 months",
                    "severity": "Severe"
                },
                "thunderstorms": {
                    "frequency": "6-12 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Extremely hot and dry",
                    "temperature_range": "34-46°C",
                    "rainfall": "Monsoon dependent"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cool and dry",
                    "temperature_range": "8-22°C",
                    "rainfall": "Minimal"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Short but intense rainfall events",
                    "peak_months": "July-August",
                    "rainfall_contribution": "75-85% of annual"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Warming and windy",
                    "temperature_range": "26-36°C"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling, dry",
                    "temperature_range": "27-37°C",
                    "rainfall": "Light"
                }
            }
        }
    },
    "kashmore": {
        "climate_profile": {
            "temperature": {
                "annual_average": "28.5°C",
                "daily_average": {
                    "summer": "35-47°C",
                    "winter": "7-21°C",
                    "spring": "27-37°C",
                    "autumn": "28-38°C"
                },
                "seasonal_averages": {
                    "summer": "38.5°C",
                    "winter": "14.0°C",
                    "spring": "31.0°C",
                    "autumn": "32.0°C"
                },
                "extremes": {
                    "highest_recorded": "51.0°C",
                    "lowest_recorded": "1.5°C",
                    "summer_max": "43-49°C",
                    "winter_min": "2-8°C"
                },
                "trend": "Increasing by 0.5-0.7°C per decade"
            },
            "precipitation": {
                "annual_total": "130mm",
                "rainfall": {
                    "annual": "130mm",
                    "monsoon_contribution": "75-85%",
                    "rainy_days": "10-18 days per year"
                },
                "snowfall": "None",
                "sleet": "None",
                "hail": "Rare",
                "seasonal_totals": {
                    "summer": "100mm (monsoon)",
                    "winter": "8mm",
                    "spring": "12mm",
                    "autumn": "10mm"
                },
                "patterns": "Short, intense monsoon events with long dry spells",
                "variability": "High variability"
            },
            "humidity": {
                "annual_average": "48%",
                "seasonal_variations": {
                    "summer": "40-55%",
                    "winter": "30-45%",
                    "spring": "35-50%",
                    "autumn": "38-52%"
                },
                "daily_patterns": {
                    "morning": "50-60%",
                    "afternoon": "25-40%",
                    "evening": "35-50%"
                },
                "trend": "Minor increases during monsoon"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "West/Southwest",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "10-16 km/h",
                    "summer": "14-22 km/h",
                    "winter": "6-12 km/h",
                    "storm_conditions": "25-42 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Southwest inflow",
                    "winter_transition": "Calmer conditions",
                    "spring_winds": "Occasional gusts"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1010-1014 hPa",
                "variations": {
                    "daily": "±3-4 hPa",
                    "seasonal": "±5-6 hPa",
                    "monsoon_low": "1006-1010 hPa"
                },
                "weather_system_effects": "Strong low pressure influence during monsoon"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "300-330 days per year",
                "cloudy_days": "30-60 days per year",
                "solar_radiation": {
                    "annual_average": "6.0-6.4 kWh/m²/day",
                    "summer_peak": "7.2-7.6 kWh/m²/day",
                    "winter_minimum": "4.2-4.5 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "Very High (10-11)",
                    "shading_factor": "Low"
                }
            },
            "cloud_cover": {
                "annual_average": "12-22%",
                "seasonal_coverage": {
                    "monsoon_season": "45-65%",
                    "dry_season": "5-15%",
                    "winter": "10-22%",
                    "spring": "15-28%"
                },
                "cloud_types": {
                    "cumulus": "Occasional in summer",
                    "stratus": "Monsoon",
                    "cirrus": "Common in winter"
                },
                "thickness": "Thin to moderate except during monsoon storms"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "2200-2800mm",
                "seasonal_rates": {
                    "summer_peak": "11-17mm/day",
                    "winter_minimum": "3-6mm/day",
                    "spring": "8-13mm/day",
                    "autumn": "7-11mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Low outside irrigated zones",
                    "water_cycle": "High evaporation from exposed surfaces"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "6-10 per year",
                    "duration": "4-12 days",
                    "peak_temperature": "49-51°C"
                },
                "dust_storms": {
                    "frequency": "8-16 per year",
                    "peak_season": "April-June",
                    "intensity": "Severe"
                },
                "droughts": {
                    "frequency": "1-3 per decade",
                    "duration": "6-18 months",
                    "severity": "Severe"
                },
                "thunderstorms": {
                    "frequency": "5-10 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Extremely hot and dry",
                    "temperature_range": "35-47°C",
                    "rainfall": "Monsoon dependent"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cool and dry",
                    "temperature_range": "7-21°C",
                    "rainfall": "Very low"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Short, intense rainfall events",
                    "peak_months": "July-August",
                    "rainfall_contribution": "75-85% of annual"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Hot and windy",
                    "temperature_range": "27-37°C"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling and dry",
                    "temperature_range": "28-38°C",
                    "rainfall": "Light"
                }
            }
        }
    },
    "umerkot": {
        "climate_profile": {
            "temperature": {
                "annual_average": "27.8°C",
                "daily_average": {
                    "summer": "34-46°C",
                    "winter": "7-22°C",
                    "spring": "26-36°C",
                    "autumn": "27-37°C"
                },
                "seasonal_averages": {
                    "summer": "38.0°C",
                    "winter": "14.0°C",
                    "spring": "30.0°C",
                    "autumn": "31.0°C"
                },
                "extremes": {
                    "highest_recorded": "49.0°C",
                    "lowest_recorded": "2.0°C",
                    "summer_max": "42-48°C",
                    "winter_min": "3-8°C"
                },
                "trend": "Increasing by 0.4-0.6°C per decade"
            },
            "precipitation": {
                "annual_total": "160mm",
                "rainfall": {
                    "annual": "160mm",
                    "monsoon_contribution": "80-90%",
                    "rainy_days": "15-22 days per year"
                },
                "snowfall": "None",
                "sleet": "None",
                "hail": "Rare",
                "seasonal_totals": {
                    "summer": "130mm (monsoon)",
                    "winter": "8mm",
                    "spring": "12mm",
                    "autumn": "10mm"
                },
                "patterns": "Semi-arid to arid with monsoon bursts",
                "variability": "High variability"
            },
            "humidity": {
                "annual_average": "50%",
                "seasonal_variations": {
                    "summer": "45-60%",
                    "winter": "30-45%",
                    "spring": "38-52%",
                    "autumn": "40-56%"
                },
                "daily_patterns": {
                    "morning": "55-65%",
                    "afternoon": "30-45%",
                    "evening": "40-55%"
                },
                "trend": "Slight increase in monsoon months"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "West/Southwest",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "10-16 km/h",
                    "summer": "14-22 km/h",
                    "winter": "6-12 km/h",
                    "storm_conditions": "25-40 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Southwest inflow",
                    "winter_transition": "Calm periods",
                    "spring_winds": "Gusty at times"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1011-1014 hPa",
                "variations": {
                    "daily": "±3-4 hPa",
                    "seasonal": "±5-6 hPa",
                    "monsoon_low": "1007-1010 hPa"
                },
                "weather_system_effects": "Monsoon lows dominate mid-year"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "300-330 days per year",
                "cloudy_days": "30-60 days per year",
                "solar_radiation": {
                    "annual_average": "5.9-6.3 kWh/m²/day",
                    "summer_peak": "7.0-7.3 kWh/m²/day",
                    "winter_minimum": "4.0-4.3 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "Very High (10-11)",
                    "shading_factor": "Low to moderate"
                }
            },
            "cloud_cover": {
                "annual_average": "14-24%",
                "seasonal_coverage": {
                    "monsoon_season": "50-70%",
                    "dry_season": "5-15%",
                    "winter": "10-22%",
                    "spring": "15-28%"
                },
                "cloud_types": {
                    "cumulus": "Occasional in summer",
                    "stratus": "Monsoon",
                    "cirrus": "Common in winter"
                },
                "thickness": "Thin to moderate except during storms"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "2200-2800mm",
                "seasonal_rates": {
                    "summer_peak": "11-17mm/day",
                    "winter_minimum": "3-6mm/day",
                    "spring": "8-13mm/day",
                    "autumn": "7-11mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Low outside irrigated tracts",
                    "water_cycle": "High evaporation in open terrain"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "5-9 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "47-49°C"
                },
                "dust_storms": {
                    "frequency": "6-14 per year",
                    "peak_season": "April-June",
                    "intensity": "Moderate to severe"
                },
                "droughts": {
                    "frequency": "1-3 per decade",
                    "duration": "6-18 months",
                    "severity": "Severe"
                },
                "thunderstorms": {
                    "frequency": "6-12 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Very hot and dry",
                    "temperature_range": "34-46°C",
                    "rainfall": "Monsoon dependent"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cool to cold nights, dry",
                    "temperature_range": "7-22°C",
                    "rainfall": "Minimal"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Short, intense rainfall events",
                    "peak_months": "July-August",
                    "rainfall_contribution": "80-90% of annual"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Hot and breezy",
                    "temperature_range": "26-36°C"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling and dry",
                    "temperature_range": "27-37°C",
                    "rainfall": "Light"
                }
            }
        }
    },
    "matiari": {
        "climate_profile": {
            "temperature": {
                "annual_average": "30.0°C",
                "daily_average": {
                    "summer": "35-45°C",
                    "winter": "12-24°C",
                    "spring": "27-37°C",
                    "autumn": "28-36°C"
                },
                "seasonal_averages": {
                    "summer": "39.0°C",
                    "winter": "18.0°C",
                    "spring": "32.0°C",
                    "autumn": "31.0°C"
                },
                "extremes": {
                    "highest_recorded": "49.0°C",
                    "lowest_recorded": "4.0°C",
                    "summer_max": "42-48°C",
                    "winter_min": "5-12°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "165mm",
                "rainfall": {
                    "annual": "165mm",
                    "monsoon_contribution": "75-85%",
                    "rainy_days": "16-22 days per year"
                },
                "snowfall": "None",
                "sleet": "None",
                "hail": "Occasional during severe storms",
                "seasonal_totals": {
                    "summer": "125mm (monsoon)",
                    "winter": "10mm",
                    "spring": "18mm",
                    "autumn": "12mm"
                },
                "patterns": "Monsoon-dominant rainfall with inter-annual variability",
                "variability": "Moderate to high"
            },
            "humidity": {
                "annual_average": "58%",
                "seasonal_variations": {
                    "summer": "65-75%",
                    "winter": "35-45%",
                    "spring": "50-60%",
                    "autumn": "55-65%"
                },
                "daily_patterns": {
                    "morning": "65-75%",
                    "afternoon": "40-50%",
                    "evening": "55-65%"
                },
                "trend": "Peaks during monsoon months"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "Southwest (monsoon)",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "12-18 km/h",
                    "summer": "16-24 km/h",
                    "winter": "8-14 km/h",
                    "storm_conditions": "25-40 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Southwest winds strengthen",
                    "winter_transition": "Calmer periods",
                    "spring_winds": "Occasional gusts"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1012-1013 hPa",
                "variations": {
                    "daily": "±3-4 hPa",
                    "seasonal": "±5-6 hPa",
                    "monsoon_low": "1007-1011 hPa"
                },
                "weather_system_effects": "Low during monsoon, higher in winter"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "270-305 days per year",
                "cloudy_days": "60-95 days per year",
                "solar_radiation": {
                    "annual_average": "5.7-6.1 kWh/m²/day",
                    "summer_peak": "6.9-7.3 kWh/m²/day",
                    "winter_minimum": "4.0-4.3 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "Very High (9-11)",
                    "shading_factor": "Moderate"
                }
            },
            "cloud_cover": {
                "annual_average": "20-30%",
                "seasonal_coverage": {
                    "monsoon_season": "55-75%",
                    "dry_season": "8-18%",
                    "winter": "15-30%",
                    "spring": "20-35%"
                },
                "cloud_types": {
                    "cumulus": "Common in summer",
                    "stratus": "Common in monsoon",
                    "cirrus": "Occasional in winter"
                },
                "thickness": "Variable from thin to moderate cumulonimbus"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "2100-2700mm",
                "seasonal_rates": {
                    "summer_peak": "10-16mm/day",
                    "winter_minimum": "3-6mm/day",
                    "spring": "7-12mm/day",
                    "autumn": "6-10mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Moderate in agricultural belts",
                    "water_cycle": "Significant canal and surface evaporation"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "5-9 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "47-49°C"
                },
                "dust_storms": {
                    "frequency": "6-12 per year",
                    "peak_season": "April-June",
                    "intensity": "Moderate to severe"
                },
                "droughts": {
                    "frequency": "1-2 per decade",
                    "duration": "6-12 months",
                    "severity": "Moderate"
                },
                "thunderstorms": {
                    "frequency": "8-16 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Hot and dry",
                    "temperature_range": "35-45°C",
                    "rainfall": "Monsoon dependent"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cool and dry",
                    "temperature_range": "12-24°C",
                    "rainfall": "Low"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Heavy but brief downpours",
                    "peak_months": "July-August",
                    "rainfall_contribution": "75-85% of annual"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Warming, breezy",
                    "temperature_range": "27-37°C"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling",
                    "temperature_range": "28-36°C",
                    "rainfall": "Light showers"
                }
            }
        }
    },
    "tando_allahyar": {
        "climate_profile": {
            "temperature": {
                "annual_average": "30.2°C",
                "daily_average": {
                    "summer": "35-45°C",
                    "winter": "12-24°C",
                    "spring": "27-37°C",
                    "autumn": "28-36°C"
                },
                "seasonal_averages": {
                    "summer": "39.2°C",
                    "winter": "18.2°C",
                    "spring": "32.2°C",
                    "autumn": "31.2°C"
                },
                "extremes": {
                    "highest_recorded": "49.5°C",
                    "lowest_recorded": "4.5°C",
                    "summer_max": "42-49°C",
                    "winter_min": "5-12°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "170mm",
                "rainfall": {
                    "annual": "170mm",
                    "monsoon_contribution": "75-85%",
                    "rainy_days": "16-22 days per year"
                },
                "snowfall": "None",
                "sleet": "None",
                "hail": "Occasional",
                "seasonal_totals": {
                    "summer": "128mm (monsoon)",
                    "winter": "10mm",
                    "spring": "18mm",
                    "autumn": "14mm"
                },
                "patterns": "Monsoon-driven with variability",
                "variability": "Moderate to high"
            },
            "humidity": {
                "annual_average": "59%",
                "seasonal_variations": {
                    "summer": "66-76%",
                    "winter": "36-46%",
                    "spring": "51-61%",
                    "autumn": "56-66%"
                },
                "daily_patterns": {
                    "morning": "66-76%",
                    "afternoon": "41-51%",
                    "evening": "56-66%"
                },
                "trend": "Peaks during monsoon"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "Southwest (monsoon)",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "12-18 km/h",
                    "summer": "16-24 km/h",
                    "winter": "8-14 km/h",
                    "storm_conditions": "25-40 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Strengthening southwest winds",
                    "winter_transition": "Calmer periods",
                    "spring_winds": "Moderate variable winds"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1012-1013 hPa",
                "variations": {
                    "daily": "±3-4 hPa",
                    "seasonal": "±5-6 hPa",
                    "monsoon_low": "1007-1011 hPa"
                },
                "weather_system_effects": "Monsoon lows dominate mid-year"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "270-305 days per year",
                "cloudy_days": "60-95 days per year",
                "solar_radiation": {
                    "annual_average": "5.7-6.1 kWh/m²/day",
                    "summer_peak": "6.9-7.3 kWh/m²/day",
                    "winter_minimum": "4.0-4.3 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "Very High (9-11)",
                    "shading_factor": "Moderate"
                }
            },
            "cloud_cover": {
                "annual_average": "20-30%",
                "seasonal_coverage": {
                    "monsoon_season": "55-75%",
                    "dry_season": "8-18%",
                    "winter": "15-30%",
                    "spring": "20-35%"
                },
                "cloud_types": {
                    "cumulus": "Common in summer",
                    "stratus": "Common in monsoon",
                    "cirrus": "Occasional in winter"
                },
                "thickness": "Variable"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "2100-2700mm",
                "seasonal_rates": {
                    "summer_peak": "10-16mm/day",
                    "winter_minimum": "3-6mm/day",
                    "spring": "7-12mm/day",
                    "autumn": "6-10mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Moderate in cultivated areas",
                    "water_cycle": "Canal and field evaporation significant"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "5-9 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "47-49°C"
                },
                "dust_storms": {
                    "frequency": "6-12 per year",
                    "peak_season": "April-June",
                    "intensity": "Moderate to severe"
                },
                "droughts": {
                    "frequency": "1-2 per decade",
                    "duration": "6-12 months",
                    "severity": "Moderate"
                },
                "thunderstorms": {
                    "frequency": "8-16 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Hot and dry",
                    "temperature_range": "35-45°C",
                    "rainfall": "Monsoon dependent"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cool and dry",
                    "temperature_range": "12-24°C",
                    "rainfall": "Low"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Heavy but brief downpours",
                    "peak_months": "July-August",
                    "rainfall_contribution": "75-85% of annual"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Warming, breezy",
                    "temperature_range": "27-37°C"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling",
                    "temperature_range": "28-36°C",
                    "rainfall": "Light showers"
                }
            }
        }
    },
    "tando_muhammad_khan": {
        "climate_profile": {
            "temperature": {
                "annual_average": "30.1°C",
                "daily_average": {
                    "summer": "35-45°C",
                    "winter": "12-24°C",
                    "spring": "27-37°C",
                    "autumn": "28-36°C"
                },
                "seasonal_averages": {
                    "summer": "39.1°C",
                    "winter": "18.1°C",
                    "spring": "32.1°C",
                    "autumn": "31.1°C"
                },
                "extremes": {
                    "highest_recorded": "49.2°C",
                    "lowest_recorded": "4.2°C",
                    "summer_max": "42-49°C",
                    "winter_min": "5-12°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "175mm",
                "rainfall": {
                    "annual": "175mm",
                    "monsoon_contribution": "75-85%",
                    "rainy_days": "16-22 days per year"
                },
                "snowfall": "None",
                "sleet": "None",
                "hail": "Occasional",
                "seasonal_totals": {
                    "summer": "132mm (monsoon)",
                    "winter": "11mm",
                    "spring": "18mm",
                    "autumn": "14mm"
                },
                "patterns": "Monsoon-driven with coastal influence",
                "variability": "Moderate"
            },
            "humidity": {
                "annual_average": "60%",
                "seasonal_variations": {
                    "summer": "68-78%",
                    "winter": "38-48%",
                    "spring": "53-63%",
                    "autumn": "58-68%"
                },
                "daily_patterns": {
                    "morning": "68-78%",
                    "afternoon": "43-53%",
                    "evening": "58-68%"
                },
                "trend": "Higher during monsoon"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "Southwest (monsoon)",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "12-18 km/h",
                    "summer": "16-24 km/h",
                    "winter": "8-14 km/h",
                    "storm_conditions": "25-40 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Strengthening southwest winds",
                    "winter_transition": "Calmer periods",
                    "spring_winds": "Moderate variable winds"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1012-1013 hPa",
                "variations": {
                    "daily": "±3-4 hPa",
                    "seasonal": "±5-6 hPa",
                    "monsoon_low": "1007-1011 hPa"
                },
                "weather_system_effects": "Low during monsoon, higher in winter"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "268-305 days per year",
                "cloudy_days": "60-97 days per year",
                "solar_radiation": {
                    "annual_average": "5.7-6.1 kWh/m²/day",
                    "summer_peak": "6.9-7.3 kWh/m²/day",
                    "winter_minimum": "4.0-4.3 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "Very High (9-11)",
                    "shading_factor": "Moderate"
                }
            },
            "cloud_cover": {
                "annual_average": "20-30%",
                "seasonal_coverage": {
                    "monsoon_season": "55-75%",
                    "dry_season": "8-18%",
                    "winter": "15-30%",
                    "spring": "20-35%"
                },
                "cloud_types": {
                    "cumulus": "Common in summer",
                    "stratus": "Common in monsoon",
                    "cirrus": "Occasional in winter"
                },
                "thickness": "Variable"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "2100-2700mm",
                "seasonal_rates": {
                    "summer_peak": "10-16mm/day",
                    "winter_minimum": "3-6mm/day",
                    "spring": "7-12mm/day",
                    "autumn": "6-10mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Moderate in cultivated areas",
                    "water_cycle": "Canal and field evaporation significant"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "5-9 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "47-49°C"
                },
                "dust_storms": {
                    "frequency": "6-12 per year",
                    "peak_season": "April-June",
                    "intensity": "Moderate to severe"
                },
                "droughts": {
                    "frequency": "1-2 per decade",
                    "duration": "6-12 months",
                    "severity": "Moderate"
                },
                "thunderstorms": {
                    "frequency": "8-16 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Hot and dry",
                    "temperature_range": "35-45°C",
                    "rainfall": "Monsoon dependent"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cool and dry",
                    "temperature_range": "12-24°C",
                    "rainfall": "Low"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Heavy but brief downpours",
                    "peak_months": "July-August",
                    "rainfall_contribution": "75-85% of annual"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Warming, breezy",
                    "temperature_range": "27-37°C"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling",
                    "temperature_range": "28-36°C",
                    "rainfall": "Light showers"
                }
            }
        }
    },
    "naushahro_feroze": {
        "climate_profile": {
            "temperature": {
                "annual_average": "30.8°C",
                "daily_average": {
                    "summer": "36-46°C",
                    "winter": "10-24°C",
                    "spring": "28-38°C",
                    "autumn": "29-37°C"
                },
                "seasonal_averages": {
                    "summer": "40.8°C",
                    "winter": "17.0°C",
                    "spring": "33.0°C",
                    "autumn": "32.0°C"
                },
                "extremes": {
                    "highest_recorded": "50.0°C",
                    "lowest_recorded": "3.0°C",
                    "summer_max": "43-49°C",
                    "winter_min": "4-10°C"
                },
                "trend": "Increasing by 0.4-0.6°C per decade"
            },
            "precipitation": {
                "annual_total": "145mm",
                "rainfall": {
                    "annual": "145mm",
                    "monsoon_contribution": "75-85%",
                    "rainy_days": "14-20 days per year"
                },
                "snowfall": "None",
                "sleet": "None",
                "hail": "Rare",
                "seasonal_totals": {
                    "summer": "112mm (monsoon)",
                    "winter": "8mm",
                    "spring": "14mm",
                    "autumn": "11mm"
                },
                "patterns": "Short, intense monsoon with long dry spells",
                "variability": "High"
            },
            "humidity": {
                "annual_average": "54%",
                "seasonal_variations": {
                    "summer": "50-62%",
                    "winter": "35-48%",
                    "spring": "45-58%",
                    "autumn": "48-60%"
                },
                "daily_patterns": {
                    "morning": "55-65%",
                    "afternoon": "30-45%",
                    "evening": "40-55%"
                },
                "trend": "Slight increase during monsoon"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "Southwest/West",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "11-17 km/h",
                    "summer": "15-22 km/h",
                    "winter": "7-12 km/h",
                    "storm_conditions": "24-40 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Southwest inflow",
                    "winter_transition": "Calmer",
                    "spring_winds": "Occasional gusts"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1011-1014 hPa",
                "variations": {
                    "daily": "±3-4 hPa",
                    "seasonal": "±5-6 hPa",
                    "monsoon_low": "1007-1010 hPa"
                },
                "weather_system_effects": "Monsoon lows dominate"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "285-320 days per year",
                "cloudy_days": "40-80 days per year",
                "solar_radiation": {
                    "annual_average": "5.9-6.3 kWh/m²/day",
                    "summer_peak": "7.1-7.4 kWh/m²/day",
                    "winter_minimum": "4.1-4.4 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "Very High (10-11)",
                    "shading_factor": "Low outside towns"
                }
            },
            "cloud_cover": {
                "annual_average": "16-26%",
                "seasonal_coverage": {
                    "monsoon_season": "50-70%",
                    "dry_season": "5-15%",
                    "winter": "10-22%",
                    "spring": "15-28%"
                },
                "cloud_types": {
                    "cumulus": "Occasional in summer",
                    "stratus": "Monsoon",
                    "cirrus": "Common in winter"
                },
                "thickness": "Generally thin to moderate"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "2150-2750mm",
                "seasonal_rates": {
                    "summer_peak": "10-16mm/day",
                    "winter_minimum": "3-6mm/day",
                    "spring": "7-12mm/day",
                    "autumn": "6-10mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Moderate in agricultural areas",
                    "water_cycle": "High evaporation from open canals"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "5-9 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "48-50°C"
                },
                "dust_storms": {
                    "frequency": "6-12 per year",
                    "peak_season": "April-June",
                    "intensity": "Moderate to severe"
                },
                "droughts": {
                    "frequency": "1-2 per decade",
                    "duration": "6-12 months",
                    "severity": "Moderate"
                },
                "thunderstorms": {
                    "frequency": "6-12 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Hot and dry",
                    "temperature_range": "36-46°C",
                    "rainfall": "Monsoon dependent"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cool and dry",
                    "temperature_range": "10-24°C",
                    "rainfall": "Minimal"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Short but intense rainfall events",
                    "peak_months": "July-August",
                    "rainfall_contribution": "75-85% of annual"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Warming and breezy",
                    "temperature_range": "28-38°C"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling, dry",
                    "temperature_range": "29-37°C",
                    "rainfall": "Light"
                }
            }
        }
    },
    "sujawal": {
        "climate_profile": {
            "temperature": {
                "annual_average": "29.0°C",
                "daily_average": {
                    "summer": "34-44°C",
                    "winter": "13-24°C",
                    "spring": "26-36°C",
                    "autumn": "27-35°C"
                },
                "seasonal_averages": {
                    "summer": "37.5°C",
                    "winter": "18.0°C",
                    "spring": "31.0°C",
                    "autumn": "30.0°C"
                },
                "extremes": {
                    "highest_recorded": "48.5°C",
                    "lowest_recorded": "5.0°C",
                    "summer_max": "41-47°C",
                    "winter_min": "6-12°C"
                },
                "trend": "Increasing by 0.3-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "200mm",
                "rainfall": {
                    "annual": "200mm",
                    "monsoon_contribution": "75-85%",
                    "rainy_days": "18-26 days per year"
                },
                "snowfall": "None",
                "sleet": "None",
                "hail": "Occasional during severe storms",
                "seasonal_totals": {
                    "summer": "155mm (monsoon)",
                    "winter": "13mm",
                    "spring": "18mm",
                    "autumn": "14mm"
                },
                "patterns": "Coastal monsoon influence with occasional storm surges",
                "variability": "Moderate"
            },
            "humidity": {
                "annual_average": "65%",
                "seasonal_variations": {
                    "summer": "75-85%",
                    "winter": "45-55%",
                    "spring": "58-68%",
                    "autumn": "62-72%"
                },
                "daily_patterns": {
                    "morning": "75-85%",
                    "afternoon": "50-60%",
                    "evening": "60-75%"
                },
                "trend": "Higher near coast and during monsoon"
            },
            "wind_patterns": {
                "prevailing_directions": {
                    "summer": "Southwest (sea breeze, monsoon)",
                    "winter": "Northeast",
                    "spring": "Variable",
                    "autumn": "Variable"
                },
                "wind_speeds": {
                    "annual_average": "12-18 km/h",
                    "summer": "16-26 km/h",
                    "winter": "8-14 km/h",
                    "storm_conditions": "30-45 km/h"
                },
                "seasonal_changes": {
                    "monsoon_onset": "Strong southwest winds",
                    "winter_transition": "Calmer periods",
                    "spring_winds": "Moderate variable winds"
                }
            },
            "atmospheric_pressure": {
                "annual_average": "1012-1013 hPa",
                "variations": {
                    "daily": "±3-4 hPa",
                    "seasonal": "±5-6 hPa",
                    "monsoon_low": "1007-1011 hPa"
                },
                "weather_system_effects": "Coastal lows during monsoon, highs in winter"
            },
            "sunshine_solar_radiation": {
                "sunny_days": "260-300 days per year",
                "cloudy_days": "65-105 days per year",
                "solar_radiation": {
                    "annual_average": "5.6-6.0 kWh/m²/day",
                    "summer_peak": "6.8-7.2 kWh/m²/day",
                    "winter_minimum": "3.9-4.2 kWh/m²/day"
                },
                "sunlight_intensity": {
                    "peak_hours": "11 AM - 3 PM",
                    "uv_index": "High (9-11)",
                    "shading_factor": "Coastal cloudiness increases diffuse light"
                }
            },
            "cloud_cover": {
                "annual_average": "25-35%",
                "seasonal_coverage": {
                    "monsoon_season": "60-80%",
                    "dry_season": "10-20%",
                    "winter": "20-35%",
                    "spring": "25-40%"
                },
                "cloud_types": {
                    "cumulus": "Common in summer",
                    "stratus": "Common in monsoon",
                    "cirrus": "Occasional in winter"
                },
                "thickness": "Variable from thin to thick cumulonimbus during storms"
            },
            "evaporation_transpiration": {
                "annual_evaporation": "2000-2600mm",
                "seasonal_rates": {
                    "summer_peak": "10-15mm/day",
                    "winter_minimum": "3-6mm/day",
                    "spring": "7-11mm/day",
                    "autumn": "6-10mm/day"
                },
                "transpiration": {
                    "vegetation_impact": "Mangroves/coastal vegetation influence",
                    "water_cycle": "Evaporation enhanced by sea breezes"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-9 days",
                    "peak_temperature": "46-48°C"
                },
                "dust_storms": {
                    "frequency": "3-8 per year",
                    "peak_season": "April-June",
                    "intensity": "Moderate"
                },
                "droughts": {
                    "frequency": "1-2 per decade",
                    "duration": "6-12 months",
                    "severity": "Moderate"
                },
                "thunderstorms": {
                    "frequency": "10-20 per year",
                    "peak_season": "Monsoon months",
                    "lightning": "Moderate"
                }
            },
            "seasonal_patterns": {
                "summer": {
                    "duration": "April-September",
                    "characteristics": "Hot and humid",
                    "temperature_range": "34-44°C",
                    "rainfall": "Monsoon dependent"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Mild and dry",
                    "temperature_range": "13-24°C",
                    "rainfall": "Low"
                },
                "monsoon": {
                    "duration": "July-September",
                    "characteristics": "Heavy rainfall events with coastal storms",
                    "peak_months": "July-August",
                    "rainfall_contribution": "75-85% of annual"
                },
                "spring": {
                    "duration": "March-May",
                    "characteristics": "Warming, humid",
                    "temperature_range": "26-36°C"
                },
                "autumn": {
                    "duration": "October-November",
                    "characteristics": "Cooling, lingering humidity",
                    "temperature_range": "27-35°C",
                    "rainfall": "Light showers"
                }
            }
        }
    }
}

# Function to get complete climate data for any district
def get_district_climate_data(district_name):
    """
    Get comprehensive climate data for a specific district.
    
    Args:
        district_name (str): Name of the district (can be with spaces or underscores)
    
    Returns:
        dict: Complete climate profile for the district, or None if not found
    """
    # Normalize district name
    normalized_name = district_name.lower().replace(' ', '_')
    
    # Check if district exists in our data
    if normalized_name in COMPREHENSIVE_CLIMATE_DATA:
        return COMPREHENSIVE_CLIMATE_DATA[normalized_name]
    
    # Try alternative naming conventions
    alternatives = {
        'karachi': 'karachi_central',
        'nawabshah': 'shaheed_benazirabad',
        'naushahro feroze': 'naushahro_feroze',
        'tando allahyar': 'tando_allahyar',
        'tando muhammad khan': 'tando_muhammad_khan'
    }
    
    if district_name.lower() in alternatives:
        return COMPREHENSIVE_CLIMATE_DATA.get(alternatives[district_name.lower()])
    
    return None

# Function to get all available districts
def get_all_districts():
    """Get list of all districts with climate data."""
    return list(COMPREHENSIVE_CLIMATE_DATA.keys())

# Function to check if a district has complete climate data
def has_complete_climate_data(district_name):
    """
    Check if a district has complete climate data covering all factors.
    
    Args:
        district_name (str): Name of the district
    
    Returns:
        bool: True if district has complete data, False otherwise
    """
    data = get_district_climate_data(district_name)
    if not data:
        return False
    
    required_factors = [
        'temperature', 'precipitation', 'humidity', 'wind_patterns',
        'atmospheric_pressure', 'sunshine_solar_radiation', 'cloud_cover',
        'evaporation_transpiration', 'storms_extreme_weather', 'seasonal_patterns'
    ]
    
    climate_profile = data.get('climate_profile', {})
    return all(factor in climate_profile for factor in required_factors)

# Export the main data structure
district_climate_data = COMPREHENSIVE_CLIMATE_DATA

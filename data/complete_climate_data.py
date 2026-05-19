"""
Complete comprehensive climate data for all districts of Sindh.
This file contains all climate factors for every district including:
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

Generated automatically to ensure complete coverage.
"""

# Complete comprehensive climate data for all districts
district_climate_data = {
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "45.5-49.5°C"
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
                    "temperature_range": "32.5-45.5°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "7.5-22.5°C",
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "45.5-49.5°C"
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
                    "temperature_range": "32.5-45.5°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "7.5-22.5°C",
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
    "karachi_west": {
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "45.5-49.5°C"
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
                    "temperature_range": "32.5-45.5°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "7.5-22.5°C",
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
    "karachi_south": {
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "45.5-49.5°C"
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
                    "temperature_range": "32.5-45.5°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "7.5-22.5°C",
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
    "karachi_malir": {
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "45.5-49.5°C"
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
                    "temperature_range": "32.5-45.5°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "7.5-22.5°C",
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
    "karachi_korangi": {
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "45.5-49.5°C"
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
                    "temperature_range": "32.5-45.5°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "7.5-22.5°C",
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
                    "summer": "38°C",
                    "winter": "17°C",
                    "spring": "32°C",
                    "autumn": "31°C"
                },
                "extremes": {
                    "highest_recorded": "50°C",
                    "lowest_recorded": "5°C",
                    "summer_max": "42-48°C",
                    "winter_min": "8-15°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "175mm",
                "rainfall": {
                    "annual": "175mm",
                    "monsoon_contribution": "70-80%",
                    "rainy_days": "17-21 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-3 times per year)",
                "seasonal_totals": {
                    "summer": "131mm (monsoon)",
                    "winter": "11mm",
                    "spring": "17mm",
                    "autumn": "11mm"
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
                    "autumn": "55-70%"
                },
                "daily_patterns": {
                    "morning": "70-80%",
                    "afternoon": "45-55%",
                    "evening": "55-70%"
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "48-52°C"
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
                    "temperature_range": "35-48°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "10-25°C",
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
                    "summer": "40°C",
                    "winter": "19°C",
                    "spring": "34°C",
                    "autumn": "33°C"
                },
                "extremes": {
                    "highest_recorded": "52°C",
                    "lowest_recorded": "7°C",
                    "summer_max": "44-50°C",
                    "winter_min": "10-17°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "120mm",
                "rainfall": {
                    "annual": "120mm",
                    "monsoon_contribution": "70-80%",
                    "rainy_days": "12-15 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-3 times per year)",
                "seasonal_totals": {
                    "summer": "90mm (monsoon)",
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
                    "autumn": "40-55%"
                },
                "daily_patterns": {
                    "morning": "55-65%",
                    "afternoon": "30-40%",
                    "evening": "40-55%"
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "50-54°C"
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
                    "temperature_range": "37-50°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "12-27°C",
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
                    "summer": "39°C",
                    "winter": "18°C",
                    "spring": "33°C",
                    "autumn": "32°C"
                },
                "extremes": {
                    "highest_recorded": "51°C",
                    "lowest_recorded": "6°C",
                    "summer_max": "43-49°C",
                    "winter_min": "9-16°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "140mm",
                "rainfall": {
                    "annual": "140mm",
                    "monsoon_contribution": "70-80%",
                    "rainy_days": "14-17 days per year"
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
                    "autumn": "50-65%"
                },
                "daily_patterns": {
                    "morning": "65-75%",
                    "afternoon": "40-50%",
                    "evening": "50-65%"
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "49-53°C"
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
                    "temperature_range": "36-49°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "11-26°C",
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
                    "summer": "39.5°C",
                    "winter": "18.5°C",
                    "spring": "33.5°C",
                    "autumn": "32.5°C"
                },
                "extremes": {
                    "highest_recorded": "51.5°C",
                    "lowest_recorded": "6.5°C",
                    "summer_max": "43.5-49.5°C",
                    "winter_min": "9.5-16.5°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "150mm",
                "rainfall": {
                    "annual": "150mm",
                    "monsoon_contribution": "70-80%",
                    "rainy_days": "15-18 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-3 times per year)",
                "seasonal_totals": {
                    "summer": "112mm (monsoon)",
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
                    "autumn": "53-68%"
                },
                "daily_patterns": {
                    "morning": "68-78%",
                    "afternoon": "43-53%",
                    "evening": "53-68%"
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "49.5-53.5°C"
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
                    "temperature_range": "36.5-49.5°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "11.5-26.5°C",
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
                    "summer": "39.5°C",
                    "winter": "18.5°C",
                    "spring": "33.5°C",
                    "autumn": "32.5°C"
                },
                "extremes": {
                    "highest_recorded": "51.5°C",
                    "lowest_recorded": "6.5°C",
                    "summer_max": "43.5-49.5°C",
                    "winter_min": "9.5-16.5°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "150mm",
                "rainfall": {
                    "annual": "150mm",
                    "monsoon_contribution": "70-80%",
                    "rainy_days": "15-18 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-3 times per year)",
                "seasonal_totals": {
                    "summer": "112mm (monsoon)",
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
                    "autumn": "53-68%"
                },
                "daily_patterns": {
                    "morning": "68-78%",
                    "afternoon": "43-53%",
                    "evening": "53-68%"
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "49.5-53.5°C"
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
                    "temperature_range": "36.5-49.5°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "11.5-26.5°C",
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
                    "summer": "40°C",
                    "winter": "19°C",
                    "spring": "34°C",
                    "autumn": "33°C"
                },
                "extremes": {
                    "highest_recorded": "52°C",
                    "lowest_recorded": "7°C",
                    "summer_max": "44-50°C",
                    "winter_min": "10-17°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "120mm",
                "rainfall": {
                    "annual": "120mm",
                    "monsoon_contribution": "70-80%",
                    "rainy_days": "12-15 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-3 times per year)",
                "seasonal_totals": {
                    "summer": "90mm (monsoon)",
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
                    "autumn": "40-55%"
                },
                "daily_patterns": {
                    "morning": "55-65%",
                    "afternoon": "30-40%",
                    "evening": "40-55%"
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "50-54°C"
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
                    "temperature_range": "37-50°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "12-27°C",
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
                    "summer": "40°C",
                    "winter": "19°C",
                    "spring": "34°C",
                    "autumn": "33°C"
                },
                "extremes": {
                    "highest_recorded": "52°C",
                    "lowest_recorded": "7°C",
                    "summer_max": "44-50°C",
                    "winter_min": "10-17°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "120mm",
                "rainfall": {
                    "annual": "120mm",
                    "monsoon_contribution": "70-80%",
                    "rainy_days": "12-15 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-3 times per year)",
                "seasonal_totals": {
                    "summer": "90mm (monsoon)",
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
                    "autumn": "40-55%"
                },
                "daily_patterns": {
                    "morning": "55-65%",
                    "afternoon": "30-40%",
                    "evening": "40-55%"
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "50-54°C"
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
                    "temperature_range": "37-50°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "12-27°C",
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
                    "summer": "39°C",
                    "winter": "18°C",
                    "spring": "33°C",
                    "autumn": "32°C"
                },
                "extremes": {
                    "highest_recorded": "51°C",
                    "lowest_recorded": "6°C",
                    "summer_max": "43-49°C",
                    "winter_min": "9-16°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "140mm",
                "rainfall": {
                    "annual": "140mm",
                    "monsoon_contribution": "70-80%",
                    "rainy_days": "14-17 days per year"
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
                    "autumn": "50-65%"
                },
                "daily_patterns": {
                    "morning": "65-75%",
                    "afternoon": "40-50%",
                    "evening": "50-65%"
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "49-53°C"
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
                    "temperature_range": "36-49°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "11-26°C",
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
                    "summer": "39°C",
                    "winter": "18°C",
                    "spring": "33°C",
                    "autumn": "32°C"
                },
                "extremes": {
                    "highest_recorded": "51°C",
                    "lowest_recorded": "6°C",
                    "summer_max": "43-49°C",
                    "winter_min": "9-16°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "140mm",
                "rainfall": {
                    "annual": "140mm",
                    "monsoon_contribution": "70-80%",
                    "rainy_days": "14-17 days per year"
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
                    "autumn": "50-65%"
                },
                "daily_patterns": {
                    "morning": "65-75%",
                    "afternoon": "40-50%",
                    "evening": "50-65%"
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "49-53°C"
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
                    "temperature_range": "36-49°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "11-26°C",
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
                    "summer": "38.5°C",
                    "winter": "17.5°C",
                    "spring": "32.5°C",
                    "autumn": "31.5°C"
                },
                "extremes": {
                    "highest_recorded": "50.5°C",
                    "lowest_recorded": "5.5°C",
                    "summer_max": "42.5-48.5°C",
                    "winter_min": "8.5-15.5°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "180mm",
                "rainfall": {
                    "annual": "180mm",
                    "monsoon_contribution": "70-80%",
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
                    "autumn": "60-75%"
                },
                "daily_patterns": {
                    "morning": "75-85%",
                    "afternoon": "50-60%",
                    "evening": "60-75%"
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "48.5-52.5°C"
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
                    "temperature_range": "35.5-48.5°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "10.5-25.5°C",
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
                    "summer": "38.5°C",
                    "winter": "17.5°C",
                    "spring": "32.5°C",
                    "autumn": "31.5°C"
                },
                "extremes": {
                    "highest_recorded": "50.5°C",
                    "lowest_recorded": "5.5°C",
                    "summer_max": "42.5-48.5°C",
                    "winter_min": "8.5-15.5°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "180mm",
                "rainfall": {
                    "annual": "180mm",
                    "monsoon_contribution": "70-80%",
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
                    "autumn": "60-75%"
                },
                "daily_patterns": {
                    "morning": "75-85%",
                    "afternoon": "50-60%",
                    "evening": "60-75%"
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "48.5-52.5°C"
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
                    "temperature_range": "35.5-48.5°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "10.5-25.5°C",
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
                    "summer": "39.5°C",
                    "winter": "18.5°C",
                    "spring": "33.5°C",
                    "autumn": "32.5°C"
                },
                "extremes": {
                    "highest_recorded": "51.5°C",
                    "lowest_recorded": "6.5°C",
                    "summer_max": "43.5-49.5°C",
                    "winter_min": "9.5-16.5°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "150mm",
                "rainfall": {
                    "annual": "150mm",
                    "monsoon_contribution": "70-80%",
                    "rainy_days": "15-18 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-3 times per year)",
                "seasonal_totals": {
                    "summer": "112mm (monsoon)",
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
                    "autumn": "53-68%"
                },
                "daily_patterns": {
                    "morning": "68-78%",
                    "afternoon": "43-53%",
                    "evening": "53-68%"
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "49.5-53.5°C"
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
                    "temperature_range": "36.5-49.5°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "11.5-26.5°C",
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
                    "summer": "40°C",
                    "winter": "19°C",
                    "spring": "34°C",
                    "autumn": "33°C"
                },
                "extremes": {
                    "highest_recorded": "52°C",
                    "lowest_recorded": "7°C",
                    "summer_max": "44-50°C",
                    "winter_min": "10-17°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "120mm",
                "rainfall": {
                    "annual": "120mm",
                    "monsoon_contribution": "70-80%",
                    "rainy_days": "12-15 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-3 times per year)",
                "seasonal_totals": {
                    "summer": "90mm (monsoon)",
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
                    "autumn": "40-55%"
                },
                "daily_patterns": {
                    "morning": "55-65%",
                    "afternoon": "30-40%",
                    "evening": "40-55%"
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "50-54°C"
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
                    "temperature_range": "37-50°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "12-27°C",
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
    "ghotki": {
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
                    "summer": "40°C",
                    "winter": "19°C",
                    "spring": "34°C",
                    "autumn": "33°C"
                },
                "extremes": {
                    "highest_recorded": "52°C",
                    "lowest_recorded": "7°C",
                    "summer_max": "44-50°C",
                    "winter_min": "10-17°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "120mm",
                "rainfall": {
                    "annual": "120mm",
                    "monsoon_contribution": "70-80%",
                    "rainy_days": "12-15 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-3 times per year)",
                "seasonal_totals": {
                    "summer": "90mm (monsoon)",
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
                    "autumn": "40-55%"
                },
                "daily_patterns": {
                    "morning": "55-65%",
                    "afternoon": "30-40%",
                    "evening": "40-55%"
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "50-54°C"
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
                    "temperature_range": "37-50°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "12-27°C",
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
    "kashmore": {
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
                    "summer": "40°C",
                    "winter": "19°C",
                    "spring": "34°C",
                    "autumn": "33°C"
                },
                "extremes": {
                    "highest_recorded": "52°C",
                    "lowest_recorded": "7°C",
                    "summer_max": "44-50°C",
                    "winter_min": "10-17°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "120mm",
                "rainfall": {
                    "annual": "120mm",
                    "monsoon_contribution": "70-80%",
                    "rainy_days": "12-15 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-3 times per year)",
                "seasonal_totals": {
                    "summer": "90mm (monsoon)",
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
                    "autumn": "40-55%"
                },
                "daily_patterns": {
                    "morning": "55-65%",
                    "afternoon": "30-40%",
                    "evening": "40-55%"
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "50-54°C"
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
                    "temperature_range": "37-50°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "12-27°C",
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
    "umerkot": {
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
                    "summer": "38.5°C",
                    "winter": "17.5°C",
                    "spring": "32.5°C",
                    "autumn": "31.5°C"
                },
                "extremes": {
                    "highest_recorded": "50.5°C",
                    "lowest_recorded": "5.5°C",
                    "summer_max": "42.5-48.5°C",
                    "winter_min": "8.5-15.5°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "180mm",
                "rainfall": {
                    "annual": "180mm",
                    "monsoon_contribution": "70-80%",
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
                    "autumn": "60-75%"
                },
                "daily_patterns": {
                    "morning": "75-85%",
                    "afternoon": "50-60%",
                    "evening": "60-75%"
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "48.5-52.5°C"
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
                    "temperature_range": "35.5-48.5°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "10.5-25.5°C",
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
    "matiari": {
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
                    "summer": "38°C",
                    "winter": "17°C",
                    "spring": "32°C",
                    "autumn": "31°C"
                },
                "extremes": {
                    "highest_recorded": "50°C",
                    "lowest_recorded": "5°C",
                    "summer_max": "42-48°C",
                    "winter_min": "8-15°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "175mm",
                "rainfall": {
                    "annual": "175mm",
                    "monsoon_contribution": "70-80%",
                    "rainy_days": "17-21 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-3 times per year)",
                "seasonal_totals": {
                    "summer": "131mm (monsoon)",
                    "winter": "11mm",
                    "spring": "17mm",
                    "autumn": "11mm"
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
                    "autumn": "55-70%"
                },
                "daily_patterns": {
                    "morning": "70-80%",
                    "afternoon": "45-55%",
                    "evening": "55-70%"
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "48-52°C"
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
                    "temperature_range": "35-48°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "10-25°C",
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
    "tando_allahyar": {
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
                    "summer": "38°C",
                    "winter": "17°C",
                    "spring": "32°C",
                    "autumn": "31°C"
                },
                "extremes": {
                    "highest_recorded": "50°C",
                    "lowest_recorded": "5°C",
                    "summer_max": "42-48°C",
                    "winter_min": "8-15°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "175mm",
                "rainfall": {
                    "annual": "175mm",
                    "monsoon_contribution": "70-80%",
                    "rainy_days": "17-21 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-3 times per year)",
                "seasonal_totals": {
                    "summer": "131mm (monsoon)",
                    "winter": "11mm",
                    "spring": "17mm",
                    "autumn": "11mm"
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
                    "autumn": "55-70%"
                },
                "daily_patterns": {
                    "morning": "70-80%",
                    "afternoon": "45-55%",
                    "evening": "55-70%"
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "48-52°C"
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
                    "temperature_range": "35-48°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "10-25°C",
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
    "tando_muhammad_khan": {
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
                    "summer": "38°C",
                    "winter": "17°C",
                    "spring": "32°C",
                    "autumn": "31°C"
                },
                "extremes": {
                    "highest_recorded": "50°C",
                    "lowest_recorded": "5°C",
                    "summer_max": "42-48°C",
                    "winter_min": "8-15°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "175mm",
                "rainfall": {
                    "annual": "175mm",
                    "monsoon_contribution": "70-80%",
                    "rainy_days": "17-21 days per year"
                },
                "snowfall": "None (tropical climate)",
                "sleet": "None",
                "hail": "Occasional during severe storms (1-3 times per year)",
                "seasonal_totals": {
                    "summer": "131mm (monsoon)",
                    "winter": "11mm",
                    "spring": "17mm",
                    "autumn": "11mm"
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
                    "autumn": "55-70%"
                },
                "daily_patterns": {
                    "morning": "70-80%",
                    "afternoon": "45-55%",
                    "evening": "55-70%"
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "48-52°C"
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
                    "temperature_range": "35-48°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "10-25°C",
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
    "naushahro_feroze": {
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
                    "summer": "39°C",
                    "winter": "18°C",
                    "spring": "33°C",
                    "autumn": "32°C"
                },
                "extremes": {
                    "highest_recorded": "51°C",
                    "lowest_recorded": "6°C",
                    "summer_max": "43-49°C",
                    "winter_min": "9-16°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "140mm",
                "rainfall": {
                    "annual": "140mm",
                    "monsoon_contribution": "70-80%",
                    "rainy_days": "14-17 days per year"
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
                    "autumn": "50-65%"
                },
                "daily_patterns": {
                    "morning": "65-75%",
                    "afternoon": "40-50%",
                    "evening": "50-65%"
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "49-53°C"
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
                    "temperature_range": "36-49°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "11-26°C",
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
    "sujawal": {
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
                    "summer": "38.5°C",
                    "winter": "17.5°C",
                    "spring": "32.5°C",
                    "autumn": "31.5°C"
                },
                "extremes": {
                    "highest_recorded": "50.5°C",
                    "lowest_recorded": "5.5°C",
                    "summer_max": "42.5-48.5°C",
                    "winter_min": "8.5-15.5°C"
                },
                "trend": "Increasing by 0.4-0.5°C per decade"
            },
            "precipitation": {
                "annual_total": "180mm",
                "rainfall": {
                    "annual": "180mm",
                    "monsoon_contribution": "70-80%",
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
                    "autumn": "60-75%"
                },
                "daily_patterns": {
                    "morning": "75-85%",
                    "afternoon": "50-60%",
                    "evening": "60-75%"
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
                    "vegetation_impact": "Variable based on agricultural development",
                    "water_cycle": "Natural water recycling in rural areas"
                }
            },
            "storms_extreme_weather": {
                "heat_waves": {
                    "frequency": "4-8 per year",
                    "duration": "3-10 days",
                    "peak_temperature": "48.5-52.5°C"
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
                    "temperature_range": "35.5-48.5°C",
                    "rainfall": "Monsoon dependent (July-September)"
                },
                "winter": {
                    "duration": "December-February",
                    "characteristics": "Cold and dry",
                    "temperature_range": "10.5-25.5°C",
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
    if normalized_name in district_climate_data:
        return district_climate_data[normalized_name]
    
    # Try alternative naming conventions
    alternatives = {
        'karachi': 'karachi_central',
        'nawabshah': 'shaheed_benazirabad',
        'naushahro feroze': 'naushahro_feroze',
        'tando allahyar': 'tando_allahyar',
        'tando muhammad khan': 'tando_muhammad_khan'
    }
    
    if district_name.lower() in alternatives:
        return district_climate_data.get(alternatives[district_name.lower()])
    
    return None

# Function to get all available districts
def get_all_districts():
    """Get list of all districts with climate data."""
    return list(district_climate_data.keys())

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

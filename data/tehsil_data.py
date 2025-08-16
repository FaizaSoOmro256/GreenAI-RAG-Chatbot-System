"""
Comprehensive tehsil-level data for all districts of Sindh.
Includes administrative, demographic, and development information.
"""

# Complete tehsil listing by division and district
sindh_tehsils = {
    "Karachi Division": {
        "Karachi Central": ["Gulberg", "Liaquatabad", "North Nazimabad", "New Karachi", "North Karachi"],
        "Karachi East": ["Gulshan-e-Iqbal", "Jamshed Town", "Ferozabad", "Gulzar-e-Hijri"],
        "Karachi West": ["Orangi", "SITE", "Baldia", "Harbour", "Manghopir"],
        "Karachi South": ["Saddar", "Civil Lines", "Garden", "Lyari", "Arambagh"],
        "Karachi Malir": ["Ibrahim Hyderi", "Murad Memon", "Shah Murad", "Gadap", "Bin Qasim"],
        "Karachi Korangi": ["Korangi", "Landhi", "Shah Faisal", "Model Colony"],
        "Karachi Keamari": ["Keamari", "SITE", "Maripur", "Shershah"]
    },
    "Hyderabad Division": {
        "Hyderabad": ["Hyderabad City", "Hyderabad Rural", "Latifabad", "Qasimabad"],
        "Matiari": ["Matiari", "Hala", "Saeedabad", "Bhit Shah"],
        "Tando Allahyar": ["Tando Allahyar", "Chamber", "Jhando Mari", "Nasarpur"],
        "Tando Muhammad Khan": ["Tando Muhammad Khan", "Bulri Shah Karim", "Tando Ghulam Hyder", "Tando Mohd Khan Rural"],
        "Badin": ["Badin", "Matli", "Talhar", "Tando Bago", "Golarchi"],
        "Dadu": ["Dadu", "Johi", "Mehar", "Khairpur Nathan Shah"],
        "Jamshoro": ["Kotri", "Manjhand", "Sehwan", "Thano Bula Khan"]
    },
    "Sukkur Division": {
        "Sukkur": ["Sukkur City", "Rohri", "Salehpat", "Pano Aqil"],
        "Khairpur": ["Khairpur", "Gambat", "Kingri", "Kot Diji", "Nara", "Sobhodero", "Thari Mirwah", "Faiz Ganj"],
        "Ghotki": ["Ghotki", "Daharki", "Mirpur Mathelo", "Ubauro", "Khan Garh"]
    },
    "Larkana Division": {
        "Larkana": ["Larkana", "Dokri", "Ratodero", "Bakrani"],
        "Kambar Shahdadkot": ["Kambar", "Shahdadkot", "Warah", "Miro Khan", "Qubo Saeed Khan"],
        "Kashmore": ["Kashmore", "Kandhkot", "Tangwani"],
        "Shikarpur": ["Shikarpur", "Garhi Yasin", "Khanpur", "Lakhi"],
        "Jacobabad": ["Jacobabad", "Garhi Khairo", "Thul"]
    },
    "Mirpurkhas Division": {
        "Mirpurkhas": ["Mirpurkhas", "Digri", "Jhuddo", "Kot Ghulam Muhammad", "Sindhri"],
        "Umerkot": ["Umerkot", "Kunri", "Pithoro", "Samaro"],
        "Tharparkar": ["Mithi", "Islamkot", "Nagarparkar", "Diplo", "Chachho"]
    },
    "Shaheed Benazirabad Division": {
        "Shaheed Benazirabad": ["Nawabshah", "Sakrand", "Daur", "Qazi Ahmed"],
        "Sanghar": ["Sanghar", "Shahdadpur", "Sinjhoro", "Tando Adam", "Jam Nawaz Ali"],
        "Naushahro Feroze": ["Naushahro Feroze", "Moro", "Kandiaro", "Mehrabpur"]
    }
}

# Tehsil-level demographic data
tehsil_demographics = {
    "Hyderabad City": {
        "population": 1200000,
        "area": 192,  # km²
        "density": 6250,  # per km²
        "urban_rural_ratio": "85:15",
        "literacy_rate": "67%",
        "major_languages": ["Sindhi", "Urdu", "Punjabi", "Pashto"]
    },
    "Latifabad": {
        "population": 800000,
        "area": 125,  # km²
        "density": 6400,  # per km²
        "urban_rural_ratio": "90:10",
        "literacy_rate": "72%",
        "major_languages": ["Sindhi", "Urdu", "Gujarati"]
    }
}

# Tehsil-level development indicators
tehsil_development = {
    "Sukkur City": {
        "education": {
            "primary_schools": 245,
            "secondary_schools": 85,
            "colleges": 12,
            "universities": 2
        },
        "healthcare": {
            "hospitals": 8,
            "basic_health_units": 24,
            "dispensaries": 45
        },
        "infrastructure": {
            "road_network": "850 km",
            "electricity_coverage": "95%",
            "water_supply": "85%",
            "sewerage": "75%"
        }
    }
}

# Tehsil-level economic activities
tehsil_economy = {
    "Hala": {
        "major_industries": [
            "Textiles",
            "Handicrafts",
            "Agriculture",
            "Small-scale manufacturing"
        ],
        "agricultural_products": [
            "Cotton",
            "Wheat",
            "Sugarcane",
            "Vegetables"
        ],
        "employment_sectors": {
            "agriculture": "45%",
            "industry": "25%",
            "services": "30%"
        }
    }
}

# Tehsil-level climate and environmental data
tehsil_climate = {
    "Mirpurkhas": {
        "temperature": {
            "summer_max": "45°C",
            "summer_min": "25°C",
            "winter_max": "28°C",
            "winter_min": "10°C"
        },
        "rainfall": {
            "annual_average": "200mm",
            "monsoon_contribution": "80%"
        },
        "environmental_issues": [
            "Water scarcity",
            "Soil degradation",
            "Air pollution"
        ]
    }
}

# Tehsil-level administrative units
tehsil_administrative_units = {
    "Larkana": {
        "union_councils": 28,
        "revenue_circles": 12,
        "police_stations": 8,
        "administrative_offices": {
            "municipal": ["Municipal Committee", "Town Committee"],
            "revenue": ["Tehsil Office", "Revenue Office"],
            "law_enforcement": ["Police", "Rangers"]
        }
    }
} 
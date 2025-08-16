"""
District data module for GreenAI.
Contains shared data about Sindh districts.
"""

# District coordinates mapping
DISTRICT_COORDINATES = {
    "Matiari": {"lat": 25.5971, "lon": 68.4471},
    "Hyderabad": {"lat": 25.3960, "lon": 68.3578},
    "Sukkur": {"lat": 27.7052, "lon": 68.8570},
    "Karachi": {"lat": 24.8607, "lon": 67.0011},
    "Larkana": {"lat": 27.5598, "lon": 68.2264},
    "Thatta": {"lat": 24.7461, "lon": 67.9243},
    "Nawabshah": {"lat": 26.2442, "lon": 68.4100},
    "Mirpurkhas": {"lat": 25.5276, "lon": 69.0126},
    "Jacobabad": {"lat": 28.2826, "lon": 68.4377},
    "Dadu": {"lat": 26.7319, "lon": 67.7750},
    "Khairpur": {"lat": 27.5295, "lon": 68.7592},
    "Badin": {"lat": 24.6558, "lon": 68.8383},
    "Tharparkar": {"lat": 24.7467, "lon": 70.2399},
    "Sanghar": {"lat": 26.0436, "lon": 68.9481},
    "Ghotki": {"lat": 28.0064, "lon": 69.3151},
    "Naushahro Feroze": {"lat": 26.8401, "lon": 68.1227},
    "Kashmore": {"lat": 28.4498, "lon": 69.5827},
    "Tando Allahyar": {"lat": 25.4667, "lon": 68.7167},
    "Tando Muhammad Khan": {"lat": 25.1239, "lon": 68.5366},
    "Umerkot": {"lat": 25.3549, "lon": 69.7376}
}

# Karachi divisions coordinates
KARACHI_DIVISION_COORDINATES = {
    "karachi central": {"lat": 24.9290, "lon": 67.0297},
    "karachi east": {"lat": 24.8731, "lon": 67.0741},
    "karachi south": {"lat": 24.8608, "lon": 67.0104},
    "karachi west": {"lat": 24.9056, "lon": 66.9653},
    "malir": {"lat": 24.8937, "lon": 67.2163},
    "korangi": {"lat": 24.8426, "lon": 67.1530}
}

# District metadata
DISTRICT_METADATA = {
    "Matiari": {
        "area": 1417.0,  # km²
        "population": 769349,  # 2017 census
        "tehsils": ["Matiari", "Hala", "Saeedabad"]
    },
    "Hyderabad": {
        "area": 5519.0,
        "population": 2199463,
        "tehsils": ["Hyderabad City", "Hyderabad Rural", "Latifabad", "Qasimabad"]
    },
    "Sukkur": {
        "area": 5165.0,
        "population": 1487903,
        "tehsils": ["Sukkur City", "Rohri", "Salehpat", "Pano Aqil"]
    },
    "Karachi": {
        "area": 3780.0,
        "population": 16024894,
        "divisions": ["Central", "East", "South", "West", "Malir", "Korangi"]
    },
    "Larkana": {
        "area": 7423.0,
        "population": 1524391,
        "tehsils": ["Larkana", "Ratodero", "Dokri", "Bakrani"]
    },
    "Thatta": {
        "area": 17355.0,
        "population": 979817,
        "tehsils": ["Thatta", "Mirpur Sakro", "Ghorabari", "Keti Bunder"]
    }
} 
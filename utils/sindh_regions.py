"""
Sindh regions and their constituent districts.
"""

sindh_regions = {
    'karachi_division': [
        'malir',
        'korangi',
        'central karachi',
        'east karachi',
        'west karachi'
    ],
    'hyderabad_division': [
        'hyderabad',
        'matiari',
        'tando allahyar',
        'tando muhammad khan',
        'badin',
        'dadu',
        'jamshoro',
        'thatta',
        'sujawal'
    ],
    'mirpurkhas_division': [
        'mirpurkhas',
        'tharparkar',
        'umerkot',
        'sanghar'
    ],
    'sukkur_division': [
        'sukkur',
        'khairpur',
        'ghotki'
    ],
    'larkana_division': [
        'larkana',
        'kambar shahdadkot',
        'shikarpur',
        'jacobabad',
        'kashmore'
    ],
    'shaheed_benazirabad_division': [
        'nawabshah',
        'naushahro feroze',
        'sanghar'
    ]
}

# Flatten the list of districts for easy access
sindh_districts = list(set([
    district.lower()
    for districts in sindh_regions.values()
    for district in districts
])) 
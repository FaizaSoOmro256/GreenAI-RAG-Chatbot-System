"""
Administrative hierarchy under tehsils/talukas in Sindh Province.
This file documents the complete structure of administrative units below the tehsil level.
"""

# Administrative units under tehsils/talukas
administrative_hierarchy = {
    "Union Councils (UCs)": {
        "description": "Basic administrative unit under tehsil/taluka",
        "responsibilities": [
            "Basic service delivery",
            "Local development projects",
            "Community mobilization",
            "Birth/death registration",
            "Local dispute resolution"
        ],
        "typical_composition": [
            "UC Chairman",
            "Vice Chairman",
            "Council members",
            "Administrative staff"
        ]
    },
    "Rural Units": {
        "Dehs": {
            "description": "Revenue villages/units in rural areas",
            "functions": [
                "Land revenue collection",
                "Land records maintenance",
                "Agricultural statistics",
                "Population records"
            ]
        },
        "Villages": {
            "description": "Basic settlement units in rural areas",
            "components": [
                "Village council",
                "Community organizations",
                "Basic health units",
                "Primary schools"
            ]
        },
        "Goths": {
            "description": "Small rural settlements/hamlets",
            "characteristics": [
                "Traditional leadership",
                "Community gatherings",
                "Basic facilities",
                "Agricultural communities"
            ]
        }
    },
    "Urban Units": {
        "Mohallas": {
            "description": "Neighborhood units in urban areas",
            "features": [
                "Neighborhood committees",
                "Community centers",
                "Local facilities",
                "Resident associations"
            ]
        },
        "Blocks/Sectors": {
            "description": "Planned urban subdivisions",
            "components": [
                "Residential areas",
                "Commercial zones",
                "Public spaces",
                "Basic utilities"
            ]
        },
        "Katchi Abadis": {
            "description": "Informal settlements",
            "management": [
                "Community representatives",
                "Basic services provision",
                "Regularization processes",
                "Development committees"
            ]
        }
    },
    "Special Administrative Units": {
        "Industrial Areas": {
            "description": "Designated industrial zones",
            "management": [
                "Industrial committees",
                "Environmental monitoring",
                "Infrastructure maintenance",
                "Security arrangements"
            ]
        },
        "Development Schemes": {
            "description": "Planned development areas",
            "components": [
                "Development authorities",
                "Planning committees",
                "Infrastructure development",
                "Zoning regulations"
            ]
        }
    }
}

# Typical hierarchy flow
administrative_flow = {
    "Tehsil/Taluka": {
        "Union Councils": {
            "Rural Areas": ["Dehs", "Villages", "Goths"],
            "Urban Areas": ["Mohallas", "Blocks/Sectors", "Katchi Abadis"],
            "Special Areas": ["Industrial Areas", "Development Schemes"]
        }
    }
}

# Administrative responsibilities at each level
level_responsibilities = {
    "Union Council": [
        "Local development planning",
        "Basic municipal services",
        "Community welfare",
        "Public health initiatives",
        "Education monitoring",
        "Infrastructure maintenance",
        "Environmental protection",
        "Social welfare programs"
    ],
    "Village/Deh": [
        "Revenue collection",
        "Land records",
        "Agricultural coordination",
        "Local dispute resolution",
        "Community development",
        "Basic health services",
        "Primary education",
        "Water management"
    ],
    "Mohalla/Block": [
        "Neighborhood management",
        "Community organization",
        "Local security",
        "Sanitation services",
        "Public space maintenance",
        "Social activities",
        "Resident welfare",
        "Basic infrastructure"
    ]
} 
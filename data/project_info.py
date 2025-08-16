"""
Project and Team Information for GreenAI Climate Assistant
University of Sufism and Modern Sciences, Bhitshah
"""

project_info = {
    "title": "GreenAI: Climate Action RAG Chatbot for Sindh",
    "type": "Final Year Project",
    "institution": {
        "name": "University of Sufism and Modern Sciences",
        "location": "Bhitshah, Sindh",
        "department": "Computer Science"
    },
    
    "team": {
        "members": [
            {
                "name": "Faiza Soomro",
                "role": "Project Lead & Developer",
                "contributions": [
                    "Project conceptualization",
                    "RAG implementation",
                    "Climate data integration",
                    "Chatbot development",
                    "System architecture"
                ]
            },
            {
                "name": "Damini Lohana",
                "role": "Team Member",
                "contributions": [
                    "Data collection",
                    "Climate analysis",
                    "System testing",
                    "Documentation"
                ]
            },
            {
                "name": "Sahrish Turk",
                "role": "Team Member",
                "contributions": [
                    "UI/UX design",
                    "Data validation",
                    "Testing protocols",
                    "Research support"
                ]
            }
        ],
        "supervisor": {
            "name": "Madam Zojan Memon",
            "role": "Project Supervisor",
            "department": "Computer Science",
            "expertise": [
                "Artificial Intelligence",
                "Climate Informatics",
                "Sustainable Computing"
            ]
        }
    },

    "sdg_focus": {
        "primary_sdg": {
            "number": 13,
            "title": "Climate Action",
            "description": "Take urgent action to combat climate change and its impacts",
            "targets": [
                {
                    "number": "13.1",
                    "description": "Strengthen resilience and adaptive capacity to climate-related hazards"
                },
                {
                    "number": "13.2",
                    "description": "Integrate climate change measures into policies and planning"
                },
                {
                    "number": "13.3",
                    "description": "Improve education, awareness-raising on climate change"
                },
                {
                    "number": "13.A",
                    "description": "Implement the UN Framework Convention on Climate Change"
                },
                {
                    "number": "13.B",
                    "description": "Promote mechanisms for climate change planning and management"
                }
            ],
            "project_contributions": [
                "Real-time climate data access for Sindh districts",
                "Climate change awareness through interactive AI",
                "Local adaptation strategies communication",
                "District-specific climate risk assessment",
                "Support for evidence-based climate action"
            ]
        },
        "related_sdgs": [
            {
                "number": 11,
                "title": "Sustainable Cities and Communities",
                "relevance": "Urban climate resilience and adaptation"
            },
            {
                "number": 15,
                "title": "Life on Land",
                "relevance": "Ecosystem protection and biodiversity"
            },
            {
                "number": 6,
                "title": "Clean Water and Sanitation",
                "relevance": "Water resource management under climate change"
            }
        ]
    },

    "project_objectives": [
        "Provide accurate climate information for Sindh",
        "Enhance climate change awareness",
        "Support local climate action planning",
        "Facilitate evidence-based decision making",
        "Promote sustainable development practices"
    ],

    "impact_areas": {
        "environmental": [
            "Climate change awareness",
            "Environmental protection",
            "Resource conservation"
        ],
        "social": [
            "Community resilience",
            "Public education",
            "Local capacity building"
        ],
        "technological": [
            "AI for sustainability",
            "Climate data accessibility",
            "Digital climate solutions"
        ]
    },

    "future_scope": [
        "Integration with more data sources",
        "Extended regional coverage",
        "Enhanced prediction capabilities",
        "Mobile application development",
        "Community engagement features"
    ]
}

# Access project information
def get_team_info():
    """Return team information"""
    return project_info["team"]

def get_sdg_details():
    """Return SDG information"""
    return project_info["sdg_focus"]

def get_project_overview():
    """Return project overview"""
    return {
        "title": project_info["title"],
        "institution": project_info["institution"],
        "objectives": project_info["project_objectives"]
    } 
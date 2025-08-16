"""
Climate Tips Generator for GreenAI.
Provides personalized climate action recommendations based on user location and preferences.
"""

import streamlit as st
import pandas as pd
import random

# Define regional climate challenges
REGIONAL_CHALLENGES = {
    "Coastal": {
        "challenges": [
            "Sea level rise",
            "Coastal erosion",
            "Saltwater intrusion",
            "Mangrove depletion",
            "Cyclones and storm surges"
        ],
        "tips": [
            "Plant and protect mangrove forests which act as natural barriers against storm surges",
            "Implement rainwater harvesting systems to reduce dependence on groundwater",
            "Use salt-tolerant crop varieties in coastal agricultural areas",
            "Create raised platforms for houses and essential infrastructure",
            "Develop early warning systems for cyclones and flooding",
            "Restore natural coastal ecosystems like dunes and wetlands",
            "Implement sustainable fishing practices to protect marine biodiversity",
            "Build structures on stilts in flood-prone areas",
            "Use permeable pavements to reduce runoff and flooding",
            "Install backflow preventers in drainage systems"
        ]
    },
    "Desert": {
        "challenges": [
            "Extreme heat",
            "Water scarcity",
            "Desertification",
            "Dust storms",
            "Limited agriculture"
        ],
        "tips": [
            "Use drought-resistant native plants for landscaping",
            "Implement drip irrigation systems for efficient water use",
            "Create shade structures with local materials",
            "Install rainwater harvesting systems for occasional rainfall",
            "Use reflective roofing materials to reduce indoor temperatures",
            "Plant trees strategically to create shade and windbreaks",
            "Implement rotational grazing to prevent overgrazing",
            "Use mulch in gardens to retain soil moisture",
            "Install window coverings to block heat during peak hours",
            "Build with thermal mass materials that regulate temperature"
        ]
    },
    "Semi-arid": {
        "challenges": [
            "Irregular rainfall",
            "Soil degradation",
            "Heat waves",
            "Groundwater depletion",
            "Agricultural vulnerabilities"
        ],
        "tips": [
            "Implement contour farming to reduce soil erosion",
            "Practice crop rotation to maintain soil fertility",
            "Use water-efficient appliances and fixtures",
            "Create rainwater storage systems for agricultural use",
            "Plant drought-tolerant native species",
            "Build check dams to slow water flow and increase absorption",
            "Use mulch and cover crops to improve soil health",
            "Implement agroforestry practices to create microclimates",
            "Use precision agriculture techniques to optimize water use",
            "Install shade nets for sensitive crops"
        ]
    }
}

# District to region mapping
DISTRICT_REGIONS = {
    "Karachi": "Coastal",
    "Thatta": "Coastal",
    "Badin": "Coastal",
    "Hyderabad": "Semi-arid",
    "Matiari": "Semi-arid",
    "Tando Allahyar": "Semi-arid",
    "Tando Muhammad Khan": "Semi-arid",
    "Jamshoro": "Semi-arid",
    "Sukkur": "Semi-arid",
    "Khairpur": "Desert",
    "Larkana": "Semi-arid",
    "Jacobabad": "Desert",
    "Shikarpur": "Semi-arid",
    "Dadu": "Semi-arid",
    "Mirpur Khas": "Semi-arid",
    "Sanghar": "Semi-arid",
    "Umerkot": "Desert",
    "Tharparkar": "Desert",
    "Nawabshah": "Desert"
}

# Sector-specific tips regardless of region
SECTOR_TIPS = {
    "Water Conservation": [
        "Install low-flow showerheads and faucets",
        "Fix leaking pipes and taps promptly",
        "Collect and reuse greywater for gardening",
        "Take shorter showers instead of baths",
        "Install dual-flush toilets or place a water displacement device in the tank",
        "Water plants in the early morning or evening to reduce evaporation",
        "Use a broom instead of a hose to clean outdoor areas",
        "Collect rainwater in barrels for outdoor use",
        "Wash only full loads of laundry",
        "Turn off the tap while brushing teeth or shaving"
    ],
    "Energy Efficiency": [
        "Replace incandescent bulbs with LED lighting",
        "Use natural lighting whenever possible",
        "Unplug electronics when not in use to avoid phantom energy use",
        "Use ceiling fans instead of air conditioning when possible",
        "Seal windows and doors to prevent air leakage",
        "Install solar panels for renewable electricity",
        "Use energy-efficient appliances with high ratings",
        "Set water heaters to a lower temperature",
        "Use insulated curtains to keep heat out during summer and in during winter",
        "Cook with lids on pots to conserve energy"
    ],
    "Sustainable Transport": [
        "Use public transportation when available",
        "Consider carpooling for daily commutes",
        "Walk or cycle for short-distance trips",
        "Maintain proper tire pressure for better fuel efficiency",
        "Avoid idling your vehicle unnecessarily",
        "Combine multiple errands into one trip",
        "Consider electric or hybrid vehicles for your next purchase",
        "Use video conferencing instead of traveling for meetings when possible",
        "Support local businesses to reduce transportation of goods",
        "Plan routes efficiently to reduce fuel consumption"
    ],
    "Waste Reduction": [
        "Compost food scraps and yard waste",
        "Use reusable shopping bags, water bottles, and food containers",
        "Reduce single-use plastic consumption",
        "Repurpose items instead of discarding them",
        "Buy products with minimal packaging",
        "Donate usable items instead of throwing them away",
        "Repair items when possible instead of replacing them",
        "Practice sustainable fashion by buying quality clothing that lasts",
        "Buy in bulk to reduce packaging waste",
        "Use cloth napkins and rags instead of paper products"
    ],
    "Sustainable Agriculture": [
        "Grow your own vegetables using kitchen scraps",
        "Create a compost pile for garden waste and food scraps",
        "Use natural pest control methods instead of chemical pesticides",
        "Plant native species that require less water and maintenance",
        "Implement crop rotation to maintain soil health",
        "Use organic fertilizers instead of synthetic ones",
        "Create windbreaks to protect crops and reduce soil erosion",
        "Practice intercropping to improve biodiversity and pest resistance",
        "Maintain vegetation buffer zones near water sources",
        "Support local farmers practicing sustainable agriculture"
    ]
}

def get_region_for_district(district):
    """
    Get the climate region for a district.
    
    Args:
        district (str): The district name
        
    Returns:
        str: The climate region
    """
    return DISTRICT_REGIONS.get(district, "Semi-arid")  # Default to Semi-arid if not found

def generate_personalized_tips(district, sectors, tip_count=5):
    """
    Generate personalized climate action tips based on district and selected sectors.
    
    Args:
        district (str): The user's district
        sectors (list): List of sectors the user is interested in
        tip_count (int): Number of tips to generate
        
    Returns:
        dict: Dictionary with region and personalized tips
    """
    region = get_region_for_district(district)
    
    # Get region-specific tips
    region_tips = REGIONAL_CHALLENGES[region]["tips"]
    
    # Get sector-specific tips
    selected_sector_tips = []
    for sector in sectors:
        if sector in SECTOR_TIPS:
            selected_sector_tips.extend(SECTOR_TIPS[sector])
    
    # Combine and select tips
    all_relevant_tips = region_tips + selected_sector_tips
    
    # If we don't have enough tips, use all of them
    if len(all_relevant_tips) <= tip_count:
        personalized_tips = all_relevant_tips
    else:
        # Randomly select tips
        personalized_tips = random.sample(all_relevant_tips, tip_count)
    
    return {
        "region": region,
        "challenges": REGIONAL_CHALLENGES[region]["challenges"],
        "tips": personalized_tips
    }

def render_climate_tips_generator():
    """
    Render the climate tips generator interface.
    """
    st.header("🌱 Personalized Climate Action Tips")
    st.write("Get customized sustainability tips based on your location and interests")
    
    # User inputs
    col1, col2 = st.columns([2, 2])
    
    with col1:
        # District selection
        district_list = sorted(list(DISTRICT_REGIONS.keys()))
        selected_district = st.selectbox("Select Your District", district_list)
        
        # Region information
        region = get_region_for_district(selected_district)
        st.info(f"**Climate Region:** {region}")
        
        challenges = REGIONAL_CHALLENGES[region]["challenges"]
        st.write("**Regional Climate Challenges:**")
        for challenge in challenges:
            st.write(f"• {challenge}")
    
    with col2:
        # Sector selection
        st.write("**Select Areas of Interest:**")
        sectors = list(SECTOR_TIPS.keys())
        
        selected_sectors = []
        for sector in sectors:
            if st.checkbox(sector, value=True):
                selected_sectors.append(sector)
        
        # Number of tips
        tip_count = st.slider("Number of Tips", min_value=3, max_value=10, value=5)
    
    # Generate tips button
    generate_button = st.button("Generate Personalized Tips", type="primary", use_container_width=True)
    
    if generate_button or "climate_tips" in st.session_state:
        # Generate and store tips
        if generate_button or selected_district != st.session_state.get("last_tips_district", "") or selected_sectors != st.session_state.get("last_tips_sectors", []):
            tips_result = generate_personalized_tips(selected_district, selected_sectors, tip_count)
            st.session_state.climate_tips = tips_result
            st.session_state.last_tips_district = selected_district
            st.session_state.last_tips_sectors = selected_sectors
        else:
            tips_result = st.session_state.climate_tips
        
        # Display tips
        st.subheader("Your Personalized Climate Action Tips")
        
        for i, tip in enumerate(tips_result["tips"], 1):
            st.markdown(f"**{i}. {tip}**")
            st.divider()
        
        # Create sharable image/PDF option
        st.write("Want to share these tips?")
        col1, col2 = st.columns(2)
        
        with col1:
            st.download_button(
                "Download as PDF",
                data=b"Placeholder PDF data",  # In a real implementation, this would generate a PDF
                file_name=f"climate_tips_{selected_district}.pdf",
                mime="application/pdf"
            )
        
        with col2:
            if st.button("Share on Social Media", use_container_width=True):
                st.success("Sharing functionality would be implemented here!")
                
        # Additional resources
        st.subheader("Additional Resources")
        st.markdown("""
        For more detailed information on implementing these tips:
        - [Sindh Climate Change Authority](https://example.com)
        - [Pakistan Meteorological Department](https://example.com)
        - [Global Climate Action Portal](https://climateaction.unfccc.int/)
        """)
        
        # Feedback
        st.subheader("Feedback")
        st.write("Was this useful? Help us improve!")
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            st.button("👍 Very Useful", use_container_width=True)
        with col2:
            st.button("👌 Somewhat Useful", use_container_width=True)
        with col3:
            st.button("👎 Not Useful", use_container_width=True) 
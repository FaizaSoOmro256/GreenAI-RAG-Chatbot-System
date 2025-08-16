"""
Carbon Calculator module for GreenAI.
Allows users to estimate their carbon footprint.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from utils.ui import get_translation

def calculate_household_emissions(household_data):
    """Placeholder function for household emissions calculation"""
    # In a real implementation, this would use the actual calculation logic
    return 2.5  # Return placeholder value in tonnes CO2e

def calculate_transport_emissions(transport_data):
    """Placeholder function for transport emissions calculation"""
    # In a real implementation, this would use the actual calculation logic
    return 1.8  # Return placeholder value in tonnes CO2e

def show_carbon_calculator():
    """
    Display the carbon calculator page.
    """
    lang = st.session_state.get("language", "english")
    translations = {
        "english": {
            "title": "Carbon Footprint Calculator",
            "description": "Estimate your carbon footprint and discover ways to reduce it.",
            "household_section": "Household Emissions",
            "transport_section": "Transportation Emissions",
            "food_section": "Food & Consumption",
            "results_section": "Your Carbon Footprint",
            "calculate_button": "Calculate My Footprint",
            "reset_button": "Reset",
            "household_size": "Household Size",
            "electricity": "Monthly Electricity Consumption (kWh)",
            "natural_gas": "Monthly Natural Gas Usage (cubic meters)",
            "water": "Monthly Water Usage (cubic meters)",
            "waste": "Weekly Household Waste (kg)",
            "car_distance": "Weekly Car Travel Distance (km)",
            "car_efficiency": "Car Fuel Efficiency (km/liter)",
            "public_transport": "Weekly Public Transport Distance (km)",
            "flights": "Flights Per Year",
            "flight_hours": "Average Flight Hours",
            "meat_consumption": "Meat Consumption",
            "dairy_consumption": "Dairy Consumption",
            "local_food": "Local Food Percentage",
            "new_clothes": "New Clothes Purchases per Year",
            "electronics": "New Electronics Purchases per Year",
            "total_footprint": "Your Total Carbon Footprint",
            "tonnes_per_year": "tonnes CO₂e per year",
            "household_result": "Household Emissions",
            "transport_result": "Transport Emissions",
            "food_result": "Food & Consumption Emissions",
            "comparison": "How You Compare",
            "pakistan_average": "Pakistan Average",
            "global_average": "Global Average",
            "reduction_tips": "Tips to Reduce Your Footprint"
        },
        "urdu": {
            "title": "کاربن فٹ پرنٹ کیلکولیٹر",
            "description": "اپنے کاربن فٹ پرنٹ کا تخمینہ لگائیں اور اسے کم کرنے کے طریقے دریافت کریں۔",
            "household_section": "گھریلو اخراج",
            "transport_section": "نقل و حمل کے اخراج",
            "food_section": "خوراک اور استعمال",
            "results_section": "آپ کا کاربن فٹ پرنٹ",
            "calculate_button": "میرا فٹ پرنٹ حساب کریں",
            "reset_button": "دوبارہ ترتیب دیں",
            "household_size": "گھر کا سائز",
            "electricity": "ماہانہ بجلی کی کھپت (کلوواٹ گھنٹہ)",
            "natural_gas": "ماہانہ قدرتی گیس کا استعمال (کیوبک میٹر)",
            "water": "ماہانہ پانی کا استعمال (کیوبک میٹر)",
            "waste": "ہفتہ وار گھریلو فضلہ (کلوگرام)",
            "car_distance": "ہفتہ وار کار سفر کا فاصلہ (کلومیٹر)",
            "car_efficiency": "کار ایندھن کی کارکردگی (کلومیٹر/لیٹر)",
            "public_transport": "ہفتہ وار عوامی نقل و حمل کا فاصلہ (کلومیٹر)",
            "flights": "سالانہ پروازیں",
            "flight_hours": "اوسط پرواز کے گھنٹے",
            "meat_consumption": "گوشت کی کھپت",
            "dairy_consumption": "دودھ کی مصنوعات کی کھپت",
            "local_food": "مقامی خوراک کا فیصد",
            "new_clothes": "سالانہ نئے کپڑوں کی خریداری",
            "electronics": "سالانہ نئی الیکٹرانکس کی خریداری",
            "total_footprint": "آپ کا کل کاربن فٹ پرنٹ",
            "tonnes_per_year": "ٹن CO₂e فی سال",
            "household_result": "گھریلو اخراج",
            "transport_result": "نقل و حمل کے اخراج",
            "food_result": "خوراک اور استعمال کے اخراج",
            "comparison": "آپ کا موازنہ",
            "pakistan_average": "پاکستان کا اوسط",
            "global_average": "عالمی اوسط",
            "reduction_tips": "اپنے فٹ پرنٹ کو کم کرنے کے لیے تجاویز"
        },
        "sindhi": {
            "title": "ڪاربان فوٽ پرنٽ ڪيلڪيوليٽر",
            "description": "پنهنجي ڪاربان فوٽ پرنٽ جو اندازو لڳايو ۽ ان کي گهٽائڻ جا طريقا ڳوليو.",
            "household_section": "گهر جا اخراج",
            "transport_section": "ٽرانسپورٽ جا اخراج",
            "food_section": "کاڌي ۽ استعمال",
            "results_section": "توهان جو ڪاربان فوٽ پرنٽ",
            "calculate_button": "منهنجو فوٽ پرنٽ حساب ڪريو",
            "reset_button": "ٻيهر ترتيب ڏيو",
            "household_size": "گهر جو سائيز",
            "electricity": "مهيني ۾ بجلي جو استعمال (کلوواٽ ڪلاڪ)",
            "natural_gas": "مهيني ۾ قدرتي گيس جو استعمال (ڪيوبڪ ميٽر)",
            "water": "مهيني ۾ پاڻي جو استعمال (ڪيوبڪ ميٽر)",
            "waste": "هفتي ۾ گهريلو فضلو (ڪلوگرام)",
            "car_distance": "هفتي ۾ ڪار سفر جو فاصلو (ڪلوميٽر)",
            "car_efficiency": "ڪار ايندڻ جي ڪارڪردگي (ڪلوميٽر/ليٽر)",
            "public_transport": "هفتي ۾ عوامي ٽرانسپورٽ جو فاصلو (ڪلوميٽر)",
            "flights": "سال ۾ اڏامون",
            "flight_hours": "اوسط اڏام جا ڪلاڪ",
            "meat_consumption": "گوشت جي کپت",
            "dairy_consumption": "کير جي مصنوعات جي کپت",
            "local_food": "مقامي کاڌي جو سيڪڙو",
            "new_clothes": "سال ۾ نئين لباس جي خريداري",
            "electronics": "سال ۾ نئين اليڪٽرانڪس جي خريداري",
            "total_footprint": "توهان جو ڪل ڪاربان فوٽ پرنٽ",
            "tonnes_per_year": "ٽن CO₂e في سال",
            "household_result": "گهر جا اخراج",
            "transport_result": "ٽرانسپورٽ جا اخراج",
            "food_result": "کاڌي ۽ استعمال جا اخراج",
            "comparison": "توهان جو ڀيٽ",
            "pakistan_average": "پاڪستان جو اوسط",
            "global_average": "عالمي اوسط",
            "reduction_tips": "پنهنجي فوٽ پرنٽ کي گهٽائڻ لاءِ صلاح"
        }
    }
    
    t = translations[lang]
    
    # Display the main title with custom styling
    st.markdown("""
        <div style="
            text-align: center;
            margin: 2rem 0 3rem 0;
            padding: 2rem;
            background: linear-gradient(135deg, #F0F7FF, #E3F2FD);
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(33, 150, 243, 0.2);
            border-left: 5px solid #2196F3;
        ">
            <h1 style="
                color: #2196F3;
                font-size: 3rem;
                font-weight: bold;
                margin: 0;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
                letter-spacing: 1px;
                font-family: 'Segoe UI', Arial, sans-serif;
                background: linear-gradient(135deg, #2196F3, #1976D2);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            ">
                🌱 Carbon Calculator
            </h1>
            <p style="
                color: #455A64;
                font-size: 1.2rem;
                margin: 1rem 0 0 0;
                font-weight: 500;
                opacity: 0.9;
            ">
                Calculate your environmental impact and discover ways to reduce it
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Handle reset button state
    if "reset_clicked" not in st.session_state:
        st.session_state.reset_clicked = False
    
    # Initialize session state for form values if not already set or if reset was clicked
    default_values = {
        "household_size": 4,
        "electricity": 250,
        "natural_gas": 20,
        "water": 15,
        "waste": 10,
        "car_distance": 100,
        "car_efficiency": 12,
        "public_transport": 20,
        "flights": 0,
        "flight_hours": 0,
        "meat_consumption": "Medium",
        "dairy_consumption": "Medium",
        "local_food": 50,
        "new_clothes": 10,
        "electronics": 1
    }

    if "carbon_calc_values" not in st.session_state or st.session_state.reset_clicked:
        st.session_state.carbon_calc_values = default_values.copy()
        if "footprint_calculated" in st.session_state:
            del st.session_state["footprint_calculated"]
        st.session_state.reset_clicked = False
    
    # Create tabs for different categories
    tab1, tab2, tab3, tab4 = st.tabs([
        t["household_section"], 
        t["transport_section"], 
        t["food_section"],
        t["results_section"]
    ])
    
    with tab1:
        # Household emissions section
        st.number_input(t["household_size"], min_value=1, max_value=15, value=st.session_state.carbon_calc_values["household_size"], key="household_size")
        st.slider(t["electricity"], min_value=0, max_value=1000, value=st.session_state.carbon_calc_values["electricity"], key="electricity")
        st.slider(t["natural_gas"], min_value=0, max_value=100, value=st.session_state.carbon_calc_values["natural_gas"], key="natural_gas")
        st.slider(t["water"], min_value=0, max_value=50, value=st.session_state.carbon_calc_values["water"], key="water")
        st.slider(t["waste"], min_value=0, max_value=30, value=st.session_state.carbon_calc_values["waste"], key="waste")
    
    with tab2:
        # Transportation emissions
        st.slider(t["car_distance"], min_value=0, max_value=1000, value=st.session_state.carbon_calc_values["car_distance"], key="car_distance")
        st.slider(t["car_efficiency"], min_value=5, max_value=25, value=st.session_state.carbon_calc_values["car_efficiency"], key="car_efficiency")
        st.slider(t["public_transport"], min_value=0, max_value=200, value=st.session_state.carbon_calc_values["public_transport"], key="public_transport")
        st.slider(t["flights"], min_value=0, max_value=10, value=st.session_state.carbon_calc_values["flights"], key="flights")
        if st.session_state.flights > 0:
            st.slider(t["flight_hours"], min_value=1, max_value=20, value=st.session_state.carbon_calc_values["flight_hours"], key="flight_hours")
    
    with tab3:
        # Food and consumption
        st.selectbox(t["meat_consumption"], ["None", "Low", "Medium", "High"], index=2, key="meat_consumption")
        st.selectbox(t["dairy_consumption"], ["None", "Low", "Medium", "High"], index=2, key="dairy_consumption")
        st.slider(t["local_food"], min_value=0, max_value=100, value=st.session_state.carbon_calc_values["local_food"], key="local_food")
        st.slider(t["new_clothes"], min_value=0, max_value=50, value=st.session_state.carbon_calc_values["new_clothes"], key="new_clothes")
        st.slider(t["electronics"], min_value=0, max_value=10, value=st.session_state.carbon_calc_values["electronics"], key="electronics")
    
    with tab4:
        # Calculate button
        col1, col2 = st.columns([1, 1])
        
        with col1:
            calculate = st.button(t["calculate_button"], type="primary", use_container_width=True)
        
        with col2:
            if st.button(t["reset_button"], use_container_width=True):
                st.session_state.reset_clicked = True
                st.rerun()
        
        if calculate or "footprint_calculated" in st.session_state:
            st.session_state.footprint_calculated = True
            
            # Save the current values
            for key in st.session_state.carbon_calc_values.keys():
                if key in st.session_state:
                    st.session_state.carbon_calc_values[key] = st.session_state[key]
            
            # Calculate emissions
            household_emissions = calculate_household_emissions(st.session_state.carbon_calc_values)
            transport_emissions = calculate_transport_emissions(st.session_state.carbon_calc_values)
            food_emissions = 1.2  # Placeholder value
            
            total_emissions = household_emissions + transport_emissions + food_emissions
            
            # Display results
            st.subheader(t["total_footprint"])
            
            col1, col2, col3 = st.columns([1, 1, 1])
            
            with col1:
                st.metric(t["household_result"], f"{household_emissions:.1f}")
            
            with col2:
                st.metric(t["transport_result"], f"{transport_emissions:.1f}")
            
            with col3:
                st.metric(t["food_result"], f"{food_emissions:.1f}")
            
            st.markdown(f"### {total_emissions:.1f} {t['tonnes_per_year']}")
            
            # Comparison chart
            st.subheader(t["comparison"])
            
            comparison_data = {
                "Category": [t["pakistan_average"], "You", t["global_average"]],
                "Emissions": [0.9, total_emissions, 4.7]
            }
            
            df = pd.DataFrame(comparison_data)
            fig = px.bar(df, x="Category", y="Emissions", 
                         color="Category", 
                         title="",
                         labels={"Emissions": "Tonnes CO₂e per year"})
            st.plotly_chart(fig, use_container_width=True)
            
            # Tips
            st.subheader(t["reduction_tips"])
            
            tips = [
                "Replace inefficient appliances with energy-efficient models",
                "Reduce car usage and consider carpooling or cycling",
                "Consume less meat and more plant-based foods",
                "Reduce water heating, which is a major energy consumer",
                "Switch to renewable energy sources where possible"
            ]
            
            for tip in tips:
                st.markdown(f"• {tip}")
        else:
            st.info("Fill in your details in each tab and click 'Calculate My Footprint' to see your results.") 
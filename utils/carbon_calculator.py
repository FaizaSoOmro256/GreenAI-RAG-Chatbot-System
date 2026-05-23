"""
Carbon Footprint Calculator for the GreenAI application.

This module provides functions to calculate and visualize carbon footprints
for individuals and households based on various activities and consumption patterns.
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Union
import io
import base64
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

# Constants for carbon emission calculations
# All values are in kg CO2e (carbon dioxide equivalent)
EMISSIONS = {
    # Electricity (kg CO2e per kWh)
    "electricity": {
        "pakistan_avg": 0.42,  # Pakistan average
        "sindh_grid": 0.45,     # Sindh grid (slightly higher due to thermal power plants)
        "solar": 0.0,           # Solar power
        "natural_gas": 0.18     # Natural gas generation
    },
    
    # Transportation (kg CO2e per km)
    "transportation": {
        "car_petrol": 0.192,    # Average petrol car
        "car_diesel": 0.171,    # Average diesel car
        "motorcycle": 0.103,    # Motorcycle
        "bus": 0.105,           # Public bus (per passenger)
        "train": 0.041,         # Train (per passenger)
        "rickshaw": 0.09,       # Auto rickshaw
        "walking": 0.0,         # Walking
        "bicycle": 0.0          # Bicycle
    },
    
    # Diet (kg CO2e per day)
    "diet": {
        "meat_heavy": 7.19,     # High meat consumption
        "meat_medium": 5.63,    # Medium meat consumption
        "meat_low": 4.67,       # Low meat consumption
        "vegetarian": 3.81,     # Vegetarian
        "vegan": 2.89           # Vegan
    },
    
    # Waste (kg CO2e per kg of waste)
    "waste": {
        "landfill": 0.58,       # Waste sent to landfill
        "recycled": 0.18,       # Recycled waste
        "composted": 0.08       # Composted organic waste
    },
    
    # Water (kg CO2e per cubic meter)
    "water": 0.389,             # Water treatment and supply
    
    # Cooking fuel (kg CO2e per unit)
    "cooking": {
        "natural_gas": 2.15,    # Natural gas (per cubic meter)
        "lpg": 2.98,            # LPG (per kg)
        "kerosene": 2.52,       # Kerosene (per liter)
        "charcoal": 6.29,       # Charcoal (per kg)
        "wood": 1.65            # Firewood (per kg)
    }
}

# Average values for Sindh region (for reference calculations)
SINDH_AVERAGES = {
    "electricity_kwh_monthly": 250,          # kWh per month
    "water_cubic_meters_monthly": 15,        # cubic meters per month
    "waste_kg_weekly": 12,                   # kg per week
    "transportation_km_daily": {
        "car": 10,                           # km per day by car
        "motorcycle": 8,                     # km per day by motorcycle
        "public_transport": 5,               # km per day by public transport
        "walking": 1                         # km per day walking
    },
    "cooking_monthly": {
        "natural_gas": 20,                   # cubic meters per month
        "lpg": 10                            # kg per month
    }
}

# Local efficiency recommendations based on carbon calculation results
RECOMMENDATIONS = {
    "electricity": [
        "Install energy-efficient LED lighting throughout your home",
        "Turn off appliances and lights when not in use",
        "Consider installing solar panels for your home",
        "Use smart power strips to eliminate phantom energy use",
        "Upgrade to energy-efficient appliances where possible"
    ],
    "transportation": [
        "Consider carpooling or using public transport more frequently",
        "Maintain your vehicle properly for optimal fuel efficiency",
        "Combine multiple errands into single trips",
        "Try walking or cycling for short distances",
        "Consider an electric vehicle for your next purchase"
    ],
    "diet": [
        "Reduce meat consumption, especially red meat",
        "Buy locally grown and seasonal foods when possible",
        "Minimize food waste by planning meals carefully",
        "Try plant-based meals several times a week",
        "Grow some of your own vegetables if space allows"
    ],
    "waste": [
        "Separate waste for recycling where facilities exist",
        "Compost food scraps and garden waste",
        "Reduce single-use plastic consumption",
        "Choose products with minimal packaging",
        "Reuse and repurpose items instead of discarding them"
    ],
    "water": [
        "Fix leaking taps and pipes promptly",
        "Install water-efficient faucets and showerheads",
        "Collect rainwater for garden use",
        "Take shorter showers and turn off taps when brushing teeth",
        "Use water-efficient appliances like washing machines"
    ],
    "cooking": [
        "Use lids on pots to reduce cooking time and energy",
        "Switch to cleaner cooking fuels if possible",
        "Maintain cooking appliances for optimal efficiency",
        "Use pressure cookers to reduce cooking time and energy",
        "Consider solar cookers for suitable dishes"
    ]
}

@dataclass
class CarbonFootprintResult:
    """Stores carbon footprint calculation results"""
    total_emissions: float
    category_emissions: Dict[str, float]
    comparison_to_average: float  # Percentage compared to Sindh average
    recommendations: Dict[str, List[str]]
    
    def get_highest_categories(self, num: int = 3) -> List[Tuple[str, float]]:
        """Returns the highest emission categories"""
        sorted_categories = sorted(
            self.category_emissions.items(),
            key=lambda x: x[1],
            reverse=True
        )
        return sorted_categories[:num]

def calculate_electricity_footprint(monthly_kwh: float, source: str = "sindh_grid") -> float:
    """Calculate carbon footprint from electricity consumption"""
    if source in EMISSIONS["electricity"]:
        emission_factor = EMISSIONS["electricity"][source]
    else:
        emission_factor = EMISSIONS["electricity"]["sindh_grid"]
    
    # Annual emissions in kg CO2e
    return monthly_kwh * emission_factor * 12

def calculate_transportation_footprint(
    daily_distances: Dict[str, float]
) -> float:
    """Calculate carbon footprint from transportation"""
    total_emissions = 0
    
    for mode, distance in daily_distances.items():
        if mode in EMISSIONS["transportation"]:
            emission_factor = EMISSIONS["transportation"][mode]
            # Annual emissions in kg CO2e (365 days)
            total_emissions += distance * emission_factor * 365
    
    return total_emissions

def calculate_diet_footprint(diet_type: str) -> float:
    """Calculate carbon footprint from diet"""
    if diet_type in EMISSIONS["diet"]:
        emission_factor = EMISSIONS["diet"][diet_type]
    else:
        emission_factor = EMISSIONS["diet"]["meat_medium"]  # Default to medium meat
    
    # Annual emissions in kg CO2e (365 days)
    return emission_factor * 365

def calculate_waste_footprint(
    weekly_waste: float,
    waste_distribution: Dict[str, float] = {"landfill": 0.7, "recycled": 0.2, "composted": 0.1}
) -> float:
    """Calculate carbon footprint from waste"""
    total_emissions = 0
    
    for disposal_method, percentage in waste_distribution.items():
        if disposal_method in EMISSIONS["waste"]:
            waste_amount = weekly_waste * percentage
            emission_factor = EMISSIONS["waste"][disposal_method]
            # Annual emissions in kg CO2e (52 weeks)
            total_emissions += waste_amount * emission_factor * 52
    
    return total_emissions

def calculate_water_footprint(monthly_cubic_meters: float) -> float:
    """Calculate carbon footprint from water consumption"""
    emission_factor = EMISSIONS["water"]
    
    # Annual emissions in kg CO2e (12 months)
    return monthly_cubic_meters * emission_factor * 12

def calculate_cooking_footprint(
    monthly_usage: Dict[str, float]
) -> float:
    """Calculate carbon footprint from cooking fuel"""
    total_emissions = 0
    
    for fuel_type, amount in monthly_usage.items():
        if fuel_type in EMISSIONS["cooking"]:
            emission_factor = EMISSIONS["cooking"][fuel_type]
            # Annual emissions in kg CO2e (12 months)
            total_emissions += amount * emission_factor * 12
    
    return total_emissions

def calculate_total_carbon_footprint(
    electricity: Dict[str, Union[float, str]],
    transportation: Dict[str, float],
    diet: str,
    waste: Dict[str, Union[float, Dict[str, float]]],
    water: float,
    cooking: Dict[str, float]
) -> CarbonFootprintResult:
    """Calculate total carbon footprint across all categories"""
    # Calculate emissions for each category
    electricity_emissions = calculate_electricity_footprint(
        electricity["monthly_kwh"], electricity["source"]
    )
    
    transportation_emissions = calculate_transportation_footprint(
        transportation
    )
    
    diet_emissions = calculate_diet_footprint(diet)
    
    waste_emissions = calculate_waste_footprint(
        waste["weekly_kg"], waste["distribution"]
    )
    
    water_emissions = calculate_water_footprint(water)
    
    cooking_emissions = calculate_cooking_footprint(cooking)
    
    # Combine all emissions
    category_emissions = {
        "electricity": electricity_emissions,
        "transportation": transportation_emissions,
        "diet": diet_emissions,
        "waste": waste_emissions,
        "water": water_emissions,
        "cooking": cooking_emissions
    }
    
    total_emissions = sum(category_emissions.values())
    
    # Calculate comparison to Sindh average
    sindh_average = calculate_sindh_average_emissions()
    comparison_percentage = (total_emissions / sindh_average) * 100
    
    # Generate recommendations based on highest emission categories
    sorted_categories = sorted(
        category_emissions.items(),
        key=lambda x: x[1],
        reverse=True
    )
    
    # Get recommendations for top 3 categories
    top_categories = sorted_categories[:3]
    personalized_recommendations = {}
    
    for category, _ in top_categories:
        if category in RECOMMENDATIONS:
            personalized_recommendations[category] = RECOMMENDATIONS[category]
    
    return CarbonFootprintResult(
        total_emissions=total_emissions,
        category_emissions=category_emissions,
        comparison_to_average=comparison_percentage,
        recommendations=personalized_recommendations
    )

def calculate_sindh_average_emissions() -> float:
    """Calculate average carbon emissions for a household in Sindh"""
    # Electricity
    electricity_emissions = calculate_electricity_footprint(
        SINDH_AVERAGES["electricity_kwh_monthly"], "sindh_grid"
    )
    
    # Transportation
    transportation_emissions = calculate_transportation_footprint(
        SINDH_AVERAGES["transportation_km_daily"]
    )
    
    # Diet (assume medium meat consumption)
    diet_emissions = calculate_diet_footprint("meat_medium")
    
    # Waste (assume 70% landfill, 20% recycled, 10% composted)
    waste_emissions = calculate_waste_footprint(
        SINDH_AVERAGES["waste_kg_weekly"],
        {"landfill": 0.7, "recycled": 0.2, "composted": 0.1}
    )
    
    # Water
    water_emissions = calculate_water_footprint(
        SINDH_AVERAGES["water_cubic_meters_monthly"]
    )
    
    # Cooking
    cooking_emissions = calculate_cooking_footprint(
        SINDH_AVERAGES["cooking_monthly"]
    )
    
    return (
        electricity_emissions +
        transportation_emissions +
        diet_emissions +
        waste_emissions +
        water_emissions +
        cooking_emissions
    )

def render_carbon_calculator() -> None:
    """Render the carbon calculator interface in Streamlit"""
    st.title("Carbon Footprint Calculator")
    st.write("""
    Calculate your annual carbon footprint based on your lifestyle and consumption patterns.
    This tool helps you understand your environmental impact and provides personalized recommendations.
    """)
    
    # Create expandable sections for each category
    with st.expander("Electricity Usage", expanded=True):
        st.subheader("Electricity")
        electricity_kwh = st.number_input(
            "Monthly electricity consumption (kWh)",
            min_value=0.0,
            max_value=1000.0,
            value=250.0,
            step=10.0,
            help="Check your electricity bill for monthly kWh usage"
        )
        
        electricity_source = st.selectbox(
            "Primary electricity source",
            options=list(EMISSIONS["electricity"].keys()),
            index=1,  # Default to Sindh grid
            format_func=lambda x: x.replace("_", " ").title(),
            help="Select your primary source of electricity"
        )
    
    with st.expander("Transportation", expanded=False):
        st.subheader("Transportation")
        st.write("Enter your daily travel distance in kilometers for each mode of transport:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            car_distance = st.number_input(
                "Car (km/day)",
                min_value=0.0,
                max_value=200.0,
                value=10.0,
                step=1.0
            )
            
            motorcycle_distance = st.number_input(
                "Motorcycle (km/day)",
                min_value=0.0,
                max_value=200.0,
                value=0.0,
                step=1.0
            )
            
            bus_distance = st.number_input(
                "Bus (km/day)",
                min_value=0.0,
                max_value=200.0,
                value=0.0,
                step=1.0
            )
            
        with col2:
            train_distance = st.number_input(
                "Train (km/day)",
                min_value=0.0,
                max_value=200.0,
                value=0.0,
                step=1.0
            )
            
            rickshaw_distance = st.number_input(
                "Auto Rickshaw (km/day)",
                min_value=0.0,
                max_value=200.0,
                value=0.0,
                step=1.0
            )
            
            walking_cycling_distance = st.number_input(
                "Walking/Cycling (km/day)",
                min_value=0.0,
                max_value=50.0,
                value=1.0,
                step=0.5
            )
        
        # Create transportation dictionary
        transportation = {
            "car_petrol": car_distance,
            "motorcycle": motorcycle_distance,
            "bus": bus_distance,
            "train": train_distance,
            "rickshaw": rickshaw_distance,
            "walking": walking_cycling_distance * 0.5,  # Split between walking and cycling
            "bicycle": walking_cycling_distance * 0.5
        }
    
    with st.expander("Diet", expanded=False):
        st.subheader("Diet")
        diet_type = st.radio(
            "Select your typical diet pattern:",
            options=list(EMISSIONS["diet"].keys()),
            index=1,  # Default to medium meat
            format_func=lambda x: x.replace("_", " ").title(),
            help="Choose the option that best describes your typical diet"
        )
    
    with st.expander("Waste Management", expanded=False):
        st.subheader("Waste")
        waste_weekly = st.number_input(
            "Weekly household waste produced (kg)",
            min_value=0.0,
            max_value=100.0,
            value=12.0,
            step=1.0,
            help="Estimate the total weight of waste your household produces each week"
        )
        
        st.write("How is your waste typically disposed of? (Percentages should add up to 100%)")
        
        landfill_pct = st.slider(
            "Sent to landfill (%)",
            min_value=0.0,
            max_value=100.0,
            value=70.0,
            step=5.0
        )
        
        recycled_pct = st.slider(
            "Recycled (%)",
            min_value=0.0,
            max_value=100.0,
            value=20.0,
            step=5.0
        )
        
        composted_pct = st.slider(
            "Composted (%)",
            min_value=0.0,
            max_value=100.0,
            value=10.0,
            step=5.0
        )
        
        # Normalize percentages to ensure they sum to 1.0
        total_pct = landfill_pct + recycled_pct + composted_pct
        if total_pct == 0:
            landfill_pct, recycled_pct, composted_pct = 100.0, 0.0, 0.0
            st.warning("At least one disposal method must be selected. Defaulting to 100% landfill.")
        else:
            landfill_pct = landfill_pct / total_pct
            recycled_pct = recycled_pct / total_pct
            composted_pct = composted_pct / total_pct
            
            if total_pct != 100:
                st.info(f"Percentages have been normalized to sum to 100%: Landfill {landfill_pct:.1f}%, Recycled {recycled_pct:.1f}%, Composted {composted_pct:.1f}%")
        
        # Create waste dictionary
        waste = {
            "weekly_kg": waste_weekly,
            "distribution": {
                "landfill": landfill_pct / 100,
                "recycled": recycled_pct / 100,
                "composted": composted_pct / 100
            }
        }
    
    with st.expander("Water Usage", expanded=False):
        st.subheader("Water")
        water_monthly = st.number_input(
            "Monthly water consumption (cubic meters)",
            min_value=0.0,
            max_value=100.0,
            value=15.0,
            step=1.0,
            help="Estimate your monthly water usage from your water bill or utility records"
        )
    
    with st.expander("Cooking", expanded=False):
        st.subheader("Cooking Fuel")
        st.write("Enter your monthly cooking fuel consumption:")
        
        fuel_type = st.selectbox(
            "Primary cooking fuel",
            options=list(EMISSIONS["cooking"].keys()),
            index=0,  # Default to natural gas
            format_func=lambda x: x.replace("_", " ").title()
        )
        
        if fuel_type == "natural_gas":
            fuel_amount = st.number_input(
                "Natural gas (cubic meters/month)",
                min_value=0.0,
                max_value=100.0,
                value=20.0,
                step=1.0
            )
        elif fuel_type == "lpg":
            fuel_amount = st.number_input(
                "LPG (kg/month)",
                min_value=0.0,
                max_value=100.0,
                value=10.0,
                step=1.0
            )
        elif fuel_type == "kerosene":
            fuel_amount = st.number_input(
                "Kerosene (liters/month)",
                min_value=0.0,
                max_value=100.0,
                value=5.0,
                step=1.0
            )
        elif fuel_type in ["charcoal", "wood"]:
            fuel_amount = st.number_input(
                f"{fuel_type.title()} (kg/month)",
                min_value=0.0,
                max_value=100.0,
                value=5.0,
                step=1.0
            )
        
        # Create cooking dictionary (only the selected fuel)
        cooking = {fuel_type: fuel_amount}
    
    # Calculate button
    if st.button("Calculate Carbon Footprint", type="primary"):
        with st.spinner("Calculating your carbon footprint..."):
            # Create electricity dictionary
            electricity = {
                "monthly_kwh": electricity_kwh,
                "source": electricity_source
            }
            
            # Calculate carbon footprint
            result = calculate_total_carbon_footprint(
                electricity=electricity,
                transportation=transportation,
                diet=diet_type,
                waste=waste,
                water=water_monthly,
                cooking=cooking
            )
            
            # Display results
            display_carbon_footprint_results(result)

def create_carbon_footprint_pdf(result: CarbonFootprintResult) -> bytes:
    """Create a PDF report of carbon footprint calculation results"""
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Styles
    styles = getSampleStyleSheet()
    title_style = styles['Heading1']
    heading2_style = styles['Heading2']
    normal_style = styles['Normal']
    
    # Create custom styles
    section_title_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading2'],
        textColor=colors.green,
        spaceAfter=12
    )
    
    info_style = ParagraphStyle(
        'Info',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.blue,
        spaceAfter=6
    )
    
    # Title
    elements.append(Paragraph("Your Carbon Footprint Report", title_style))
    elements.append(Spacer(1, 12))
    
    # Date
    date_str = datetime.now().strftime("%B %d, %Y")
    elements.append(Paragraph(f"Generated on {date_str}", styles['Italic']))
    elements.append(Spacer(1, 24))
    
    # Summary section
    elements.append(Paragraph("Summary", section_title_style))
    
    # Convert to metric tons for easier reading
    total_tons = result.total_emissions / 1000
    
    summary_text = f"""
    Your annual carbon footprint is <b>{total_tons:.2f} tonnes CO₂e</b>, which is 
    <b>{result.comparison_to_average - 100:.1f}%</b> {'higher' if result.comparison_to_average > 100 else 'lower'} 
    than the average in Sindh.
    """
    elements.append(Paragraph(summary_text, normal_style))
    elements.append(Spacer(1, 12))
    
    # Environmental impact info
    trees_needed = total_tons * 16.5  # Each tree absorbs approximately 60 kg CO2 per year
    
    impact_text = f"""
    <b>Environmental Impact:</b><br/>
    • {trees_needed:.0f} trees would need to grow for one year to offset your emissions<br/>
    • This is equivalent to {total_tons * 2.5:.1f} return flights from Karachi to Islamabad
    """
    elements.append(Paragraph(impact_text, info_style))
    elements.append(Spacer(1, 20))
    
    # Category breakdown table
    elements.append(Paragraph("Emissions by Category", section_title_style))
    
    # Create the data for the table
    data = [['Category', 'Emissions (kg CO₂e)', 'Percentage']]
    
    # Sort categories by emissions (highest first)
    sorted_categories = sorted(
        result.category_emissions.items(),
        key=lambda x: x[1],
        reverse=True
    )
    
    for category, emissions in sorted_categories:
        category_name = category.replace('_', ' ').title()
        percentage = (emissions / result.total_emissions) * 100
        data.append([
            category_name,
            f"{emissions:.1f}",
            f"{percentage:.1f}%"
        ])
    
    # Add total row
    data.append(['Total', f"{result.total_emissions:.1f}", '100.0%'])
    
    # Create table
    table = Table(data, colWidths=[200, 120, 100])
    
    # Add style
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, -1), (-1, -1), colors.lightgrey),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])
    
    # Add zebra striping for the data rows
    for row in range(1, len(data) - 1):
        if row % 2 == 0:
            table_style.add('BACKGROUND', (0, row), (-1, row), colors.whitesmoke)
    
    table.setStyle(table_style)
    elements.append(table)
    elements.append(Spacer(1, 20))
    
    # Recommendations section
    elements.append(Paragraph("Personalized Recommendations", section_title_style))
    elements.append(Paragraph("Based on your carbon footprint calculation, here are some recommendations to reduce your environmental impact:", normal_style))
    elements.append(Spacer(1, 10))
    
    # Add recommendations for each category
    for idx, (category, recommendations) in enumerate(result.recommendations.items()):
        category_name = category.replace('_', ' ').title()
        elements.append(Paragraph(f"{idx+1}. {category_name}", styles['Heading3']))
        
        for rec in recommendations:
            elements.append(Paragraph(f"• {rec}", normal_style))
        
        elements.append(Spacer(1, 10))
    
    # About the calculator
    elements.append(Paragraph("About This Report", section_title_style))
    elements.append(Paragraph("""
    This report was generated by the Green AI Carbon Footprint Calculator, which helps users understand and 
    reduce their environmental impact. The calculations are based on standardized emission factors for different
    activities and consumption patterns, adjusted for the context of Sindh, Pakistan.
    """, normal_style))
    
    # Build the PDF
    doc.build(elements)
    
    # Get the PDF from the buffer
    buffer.seek(0)
    return buffer.getvalue()

def get_download_link(pdf_bytes, filename="carbon_footprint_report.pdf"):
    """Generate a download link for the PDF report"""
    b64 = base64.b64encode(pdf_bytes).decode()
    href = f'<a href="data:application/pdf;base64,{b64}" download="{filename}" class="download-button">Download PDF Report</a>'
    return href

def create_shareable_image(result: CarbonFootprintResult) -> bytes:
    """Create a shareable image with carbon footprint results"""
    try:
        # Use matplotlib to create a shareable image
        import matplotlib.pyplot as plt
        from matplotlib.figure import Figure
        from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
        
        # Create a figure
        fig = Figure(figsize=(10, 6), dpi=100)
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        
        # Clean the data
        categories = [cat.replace('_', ' ').title() for cat in result.category_emissions.keys()]
        emissions = list(result.category_emissions.values())
        
        # Create horizontal bar chart
        bars = ax.barh(categories, emissions, color='green')
        
        # Add labels and values to bars
        for bar in bars:
            width = bar.get_width()
            label_x_pos = width + 30
            ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{width:.1f} kg', 
                    va='center', color='black')
        
        # Set title and labels
        total_tons = result.total_emissions / 1000
        ax.set_title(f'My Carbon Footprint: {total_tons:.2f} tonnes CO₂e', fontsize=14, pad=20)
        ax.set_xlabel('Emissions (kg CO₂e per year)', fontsize=12)
        
        # Add a footer with website URL
        fig.text(0.5, 0.02, 'Generated with Green AI Carbon Calculator • www.greenai-sindh.org', 
                 ha='center', fontsize=8, color='gray')
        
        # Adjust layout
        fig.tight_layout(rect=[0, 0.05, 1, 0.95])
        
        # Save to BytesIO
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        
        return buf.getvalue()
    except Exception as e:
        print(f"Error creating shareable image: {str(e)}")
        # Return a fallback image or None
        return None

def display_carbon_footprint_results(result: CarbonFootprintResult) -> None:
    """Display carbon footprint calculation results with visualizations"""
    # Create tabs for different views of the results
    overview_tab, details_tab, recommendations_tab, export_tab = st.tabs(["Overview", "Detailed Breakdown", "Recommendations", "Export & Share"])
    
    with overview_tab:
        st.header("Your Carbon Footprint Overview")
        
        # Convert to metric tons for easier reading
        total_tons = result.total_emissions / 1000
        
        # Display the total footprint with a large metric
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(
                "Annual Carbon Footprint",
                f"{total_tons:.2f} tonnes CO₂e",
                f"{result.comparison_to_average - 100:.1f}% compared to average" if result.comparison_to_average != 100 else "Equal to average",
                delta_color="inverse"  # Lower is better, so use inverse colors
            )
        
        with col2:
            # Show equivalent activities
            trees_needed = total_tons * 16.5  # Each tree absorbs approximately 60 kg CO2 per year
            st.info(f"""
            **To offset your footprint:**
            - {trees_needed:.0f} trees would need to grow for one year
            - This is equivalent to {total_tons * 2.5:.1f} return flights from Karachi to Islamabad
            """)
        
        # Create a pie chart for category breakdown
        df = pd.DataFrame({
            'Category': list(result.category_emissions.keys()),
            'Emissions': list(result.category_emissions.values())
        })
        
        df['Category'] = df['Category'].str.replace('_', ' ').str.title()
        df['Percentage'] = df['Emissions'] / df['Emissions'].sum() * 100
        df = df.sort_values('Emissions', ascending=False)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        wedges, texts, autotexts = ax.pie(
            df['Emissions'], 
            labels=df['Category'],
            autopct='%1.1f%%',
            startangle=90,
            wedgeprops={'edgecolor': 'white', 'linewidth': 1}
        )
        
        # Equal aspect ratio ensures that pie is drawn as a circle
        ax.axis('equal')
        plt.setp(autotexts, size=9, weight="bold")
        plt.title("Carbon Footprint by Category", size=16)
        
        # Display the chart
        st.pyplot(fig)
        
        # Carbon footprint comparison
        st.subheader("How does your footprint compare?")
        
        comparison_data = {
            'Sindh Average': calculate_sindh_average_emissions() / 1000,
            'Pakistan Average': 2.2,  # tonnes CO2e per year
            'World Average': 4.8,     # tonnes CO2e per year
            'Your Footprint': total_tons
        }
        
        comp_df = pd.DataFrame({
            'Entity': list(comparison_data.keys()),
            'Tonnes CO₂e': list(comparison_data.values())
        })
        
        comparison_chart = alt.Chart(comp_df).mark_bar().encode(
            x=alt.X('Entity:N', sort=None),
            y=alt.Y('Tonnes CO₂e:Q', title='Annual Carbon Footprint (tonnes CO₂e)'),
            color=alt.condition(
                alt.datum.Entity == 'Your Footprint',
                alt.value('#1e88e5'),  # Blue for Your Footprint
                alt.value('#7CB342')   # Green for others
            ),
            tooltip=['Entity', 'Tonnes CO₂e']
        ).properties(
            width=600,
            height=400,
            title='Carbon Footprint Comparison'
        )
        
        st.altair_chart(comparison_chart, use_container_width=True)
    
    with details_tab:
        st.header("Detailed Breakdown")
        
        # Create detailed bar chart for each category
        emissions_df = pd.DataFrame({
            'Category': [k.replace('_', ' ').title() for k in result.category_emissions.keys()],
            'Emissions (kg CO₂e)': list(result.category_emissions.values())
        }).sort_values('Emissions (kg CO₂e)', ascending=False)
        
        detailed_chart = alt.Chart(emissions_df).mark_bar().encode(
            x=alt.X('Emissions (kg CO₂e):Q'),
            y=alt.Y('Category:N', sort='-x'),
            color=alt.Color('Category:N', legend=None),
            tooltip=['Category', 'Emissions (kg CO₂e)']
        ).properties(
            width=600,
            height=400,
            title='Emissions by Category (kg CO₂e per year)'
        )
        
        st.altair_chart(detailed_chart, use_container_width=True)
        
        # Tabular breakdown
        st.subheader("Emissions Table")
        st.dataframe(
            emissions_df,
            column_config={
                "Category": st.column_config.TextColumn("Category"),
                "Emissions (kg CO₂e)": st.column_config.NumberColumn(
                    "Annual Emissions (kg CO₂e)",
                    format="%.1f kg"
                )
            },
            hide_index=True,
            use_container_width=True
        )
        
        # Show the top contributors
        st.subheader("Top Contributors to Your Footprint")
        
        for idx, (category, emissions) in enumerate(result.get_highest_categories()):
            category_name = category.replace('_', ' ').title()
            st.write(f"**{idx+1}. {category_name}**: {emissions:.1f} kg CO₂e per year ({emissions/result.total_emissions*100:.1f}% of total)")
    
    with recommendations_tab:
        st.header("Personalized Recommendations")
        st.write("Based on your carbon footprint calculation, here are some targeted recommendations to reduce your environmental impact:")
        
        for idx, (category, recommendations) in enumerate(result.recommendations.items()):
            category_name = category.replace('_', ' ').title()
            st.subheader(f"{idx+1}. {category_name}")
            for rec in recommendations:
                st.markdown(f"• {rec}")
        
        # Call to action
        st.success("""
        **Take the Challenge!**
        
        Try implementing one recommendation from each category and recalculate your footprint in a month.
        Small changes can add up to make a significant impact on your carbon footprint!
        """)
        
        # Information about carbon offsetting
        st.info("""
        **About Carbon Offsetting**
        
        Carbon offsetting helps neutralize your emissions by funding projects that reduce greenhouse gas emissions elsewhere.
        Common offsetting projects include:
        - Renewable energy development
        - Forest conservation and reforestation
        - Methane capture from landfills
        - Energy efficiency initiatives
        
        Consider exploring local carbon offset programs in Pakistan to support sustainable development in your region.
        """)
    
    with export_tab:
        st.header("Export & Share Your Results")
        st.write("Save your carbon footprint results or share them with others.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Download PDF Report")
            st.write("Get a detailed PDF report of your carbon footprint calculation.")
            
            # Create PDF when button is clicked
            if st.button("Generate PDF Report", type="primary"):
                with st.spinner("Generating PDF report..."):
                    try:
                        pdf_bytes = create_carbon_footprint_pdf(result)
                        
                        # Create the download link
                        st.markdown(
                            get_download_link(pdf_bytes),
                            unsafe_allow_html=True
                        )
                        
                        # Preview the PDF using an embedded viewer
                        st.success("PDF generated successfully! Click the link above to download.")
                    except Exception as e:
                        st.error(f"Failed to generate PDF: {str(e)}")
        
        with col2:
            st.subheader("Share on Social Media")
            st.write("Share your carbon footprint results on social media to raise awareness.")
            
            # Create shareable image
            if st.button("Create Shareable Image"):
                with st.spinner("Creating shareable image..."):
                    try:
                        image_bytes = create_shareable_image(result)
                        
                        if image_bytes:
                            # Display the image
                            st.image(image_bytes, caption="Your Carbon Footprint Summary", use_column_width=True)
                            
                            # Create download link for the image
                            b64_image = base64.b64encode(image_bytes).decode()
                            href = f'<a href="data:image/png;base64,{b64_image}" download="carbon_footprint.png">Download Image</a>'
                            st.markdown(href, unsafe_allow_html=True)
                            
                            # Show social media sharing instructions
                            st.info("""
                            **How to share:**
                            1. Download the image above
                            2. Post it on your social media with hashtags:
                               #CarbonFootprint #ClimateAction #GreenAI
                            """)
                        else:
                            st.warning("Could not create the shareable image. Please try again.")
                    except Exception as e:
                        st.error(f"Failed to create shareable image: {str(e)}")
        
        # Email sharing option
        st.subheader("Email Your Results")
        
        # Simple email form
        with st.form("email_form"):
            st.markdown("#### Send Your Results via Email")
            email = st.text_input("Recipient Email Address")
            message = st.text_area("Add a Personal Message (Optional)", 
                                 value=f"Here's my carbon footprint calculation: {result.total_emissions/1000:.2f} tonnes CO₂e per year.")
            
            # Submit button
            submit_email = st.form_submit_button("Send Email")
        
        if submit_email:
            # This would normally connect to an email service
            # For now, we'll just show a success message
            if email and '@' in email:
                st.success(f"Email would be sent to {email} (Email functionality not implemented in this demo)")
            else:
                st.error("Please enter a valid email address")

# Integration with Green AI main app
def add_carbon_calculator_to_navigation():
    """
    Function to be called from app.py to add Carbon Calculator to navigation options
    """
    return {
        "id": "carbon_calculator",
        "icon": "🌱",
        "label": "Carbon Calculator"
    }

def render_carbon_calculator_view():
    """
    Function to be called from app.py when the Carbon Calculator view is selected
    """
    st.markdown(f"### 🌱 Carbon Footprint Calculator")
    st.markdown("Calculate your personal or household carbon footprint and discover ways to reduce your environmental impact.")
    
    render_carbon_calculator()
    
    # Add some contextual information about carbon footprints in Pakistan
    with st.expander("About Carbon Footprints in Pakistan"):
        st.write("""
        ## Carbon Footprints in Pakistan
        
        Pakistan contributes less than 1% to global greenhouse gas emissions, but is among the countries most vulnerable to climate change impacts.
        The national average carbon footprint is about 2.2 tonnes CO₂e per person annually, significantly lower than the global average of 4.8 tonnes.
        
        ### Regional Variations
        
        - **Urban areas** (like Karachi) tend to have higher carbon footprints due to greater energy consumption and transportation usage
        - **Rural areas** typically have lower footprints but often rely on biomass fuels that contribute to indoor air pollution
        - **Sindh province** faces unique challenges, including coastal vulnerability and heat stress in urban centers
        
        ### Climate Action Plan
        
        Pakistan's climate commitments include:
        - Reducing emissions by 50% by 2030 (15% unconditionally, 35% subject to international support)
        - Increasing the share of renewable energy to 30% by 2030
        - Expanding forest cover and implementing mass transit systems in major cities
        
        *This calculator helps you understand your personal contribution and find ways to support these national goals.*
        """)

if __name__ == "__main__":
    # For testing the module independently
    render_carbon_calculator() 
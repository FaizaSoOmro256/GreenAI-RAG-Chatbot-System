"""
Offsets Recommender module for Ecosphere AI.
Suggests carbon offset projects and initiatives.
"""

import streamlit as st
from utils.ui import get_translation
import io
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def show_offsets_recommender():
    """
    Display the offsets recommender page with carbon offset suggestions.
    """
    # Sidebar filters
    st.sidebar.title("Carbon Offset Projects")
    districts = [
        "All",  # Adding "All" as a default option
        "Karachi", "Hyderabad", "Sukkur", "Larkana", "Nawabshah", 
        "Mirpurkhas", "Jacobabad", "Thatta", "Dadu", "Khairpur"
    ]
    selected_location = st.sidebar.selectbox("Location", districts, index=0)
    budget = st.sidebar.slider("Budget (PKR)", min_value=500, max_value=10000, value=2000, step=500)
    interests = [
        "Renewable Energy", "Reforestation", "Community Projects", 
        "Sustainable Agriculture", "Waste Management"
    ]
    selected_interests = st.sidebar.multiselect("Areas of Interest", interests, default=["Renewable Energy"])
    find_projects = st.sidebar.button("Find Projects", type="primary")
    
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
                🌱 Offsets Recommender
            </h1>
            <p style="
                color: #455A64;
                font-size: 1.2rem;
                margin: 1rem 0 0 0;
                font-weight: 500;
                opacity: 0.9;
            ">
                Discover carbon offset projects and initiatives to reduce your environmental impact
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    if find_projects:
        # Display project recommendations
        st.subheader("Project Recommendations")
        st.write(f"Location: {selected_location}")
        st.write(f"Budget: PKR {budget:,}")
        st.write(f"Interests: {', '.join(selected_interests)}")
        
        # Sample project recommendations
        st.info(get_translation(None, "no_results"))

    # Example offset projects with appropriate images
    offset_projects = [
        {
            "title": "Indus Delta Mangrove Restoration",
            "category": "Reforestation",
            "location": "Thatta",
            "description": "Support mangrove planting in the Indus Delta to protect coastal communities and sequester carbon.",
            "cost": 1500,
            "impact": "10 trees/month, ~1.2 tonnes CO₂/year",
            "image": "https://images.pexels.com/photos/1166209/pexels-photo-1166209.jpeg?auto=compress&cs=tinysrgb&w=300&h=200&dpr=1"
        },
        {
            "title": "Solar for Schools Initiative",
            "category": "Renewable Energy",
            "location": "Hyderabad",
            "description": "Help install solar panels on school rooftops to reduce fossil fuel usage and provide reliable electricity.",
            "cost": 2500,
            "impact": "~2.5 tonnes CO₂/year",
            "image": "https://images.unsplash.com/photo-1508514177221-188b1cf16e9d?w=300&h=200&fit=crop&q=80"
        },
        {
            "title": "Community Composting Program",
            "category": "Waste Management",
            "location": "Karachi",
            "description": "Support a community-based composting initiative to reduce methane emissions from landfills.",
            "cost": 1000,
            "impact": "~0.8 tonnes CO₂/year",
            "image": "https://images.unsplash.com/photo-1604187351574-c75ca79f5807?w=300&h=200&fit=crop&q=80"
        },
        {
            "title": "Sustainable Irrigation Systems",
            "category": "Sustainable Agriculture",
            "location": "Mirpurkhas",
            "description": "Support efficient irrigation systems for farmers to reduce water usage and associated emissions.",
            "cost": 2000,
            "impact": "~1.5 tonnes CO₂/year",
            "image": "https://images.unsplash.com/photo-1594502184342-2e12f877aa73?w=300&h=200&fit=crop&q=80"
        },
        {
            "title": "Biogas Digesters for Rural Communities",
            "category": "Renewable Energy",
            "location": "Larkana",
            "description": "Help install biogas digesters to convert agricultural waste into clean cooking fuel and reduce firewood usage.",
            "cost": 3000,
            "impact": "~2.0 tonnes CO₂/year",
            "image": "https://images.unsplash.com/photo-1471193945509-9ad0617afabf?w=300&h=200&fit=crop&q=80"
        },
        {
            "title": "Wind Power Expansion Project",
            "category": "Renewable Energy",
            "location": "Thatta",
            "description": "Support the expansion of wind power capacity in the Jhimpir-Gharo corridor of Sindh.",
            "cost": 5000,
            "impact": "~5.0 tonnes CO₂/year",
            "image": "https://images.unsplash.com/photo-1467533003447-e295ff1b0435?w=300&h=200&fit=crop&q=80"
        },
        {
            "title": "Urban Tree Planting Initiative",
            "category": "Reforestation",
            "location": "Karachi",
            "description": "Support planting shade trees in urban areas to reduce heat island effect and sequester carbon.",
            "cost": 800,
            "impact": "5 trees/month, ~0.5 tonnes CO₂/year",
            "image": "https://images.unsplash.com/photo-1444492417251-9c84a5fa18e0?w=300&h=200&fit=crop&q=80"
        },
        {
            "title": "Organic Farming Transition Program",
            "category": "Sustainable Agriculture",
            "location": "Nawabshah",
            "description": "Help farmers transition to organic farming practices that reduce emissions from fertilizers.",
            "cost": 1800,
            "impact": "~1.3 tonnes CO₂/year",
            "image": "https://images.unsplash.com/photo-1592982537447-7440770cbfc9?w=300&h=200&fit=crop&q=80"
        },
        {
            "title": "Water Conservation Awareness Initiative",
            "category": "Community Projects",
            "location": "Sukkur",
            "description": "Support community education programs on water conservation practices to reduce energy used in water pumping and treatment.",
            "cost": 1200,
            "impact": "~0.9 tonnes CO₂/year",
            "image": "https://images.unsplash.com/photo-1541675154750-0444c7d51e8e?w=300&h=200&fit=crop&q=80"
        },
        {
            "title": "Plastic Waste Reduction Campaign",
            "category": "Waste Management",
            "location": "Dadu",
            "description": "Support initiatives to reduce single-use plastics and promote recycling in communities across Dadu district.",
            "cost": 900,
            "impact": "~0.7 tonnes CO₂/year",
            "image": "https://images.unsplash.com/photo-1528190336454-13cd56b45b5a?w=300&h=200&fit=crop&q=80"
        }
    ]
    
    # Filter projects (if Find button is clicked)
    if find_projects:
        # Apply filters
        filtered_projects = [
            p for p in offset_projects 
            if (p["cost"] <= budget) and 
               (p["location"] == selected_location or selected_location == "All") and
               (p["category"] in selected_interests or not selected_interests)
        ]
    else:
        filtered_projects = offset_projects
    
    # Display projects
    if filtered_projects:
        for i, project in enumerate(filtered_projects):
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.image(project["image"], width=300)
            
            with col2:
                st.subheader(project["title"])
                st.markdown(project["description"])
                
                # Project details
                col_a, col_b, col_c = st.columns(3)
                
                with col_a:
                    st.markdown(f"**{get_translation(None, 'project_category')}**: {project['category']}")
                
                with col_b:
                    st.markdown(f"**{get_translation(None, 'project_location')}**: {project['location']}")
                
                with col_c:
                    st.markdown(f"**{get_translation(None, 'project_cost')}**: PKR {project['cost']}/month")
                
                st.markdown(f"**{get_translation(None, 'project_impact')}**: {project['impact']}")
                
                # Create PDF report function
                def generate_pdf_report(project):
                    buffer = io.BytesIO()
                    doc = SimpleDocTemplate(buffer, pagesize=letter)
                    styles = getSampleStyleSheet()
                    
                    # Create custom styles
                    title_style = ParagraphStyle(
                        'TitleStyle',
                        parent=styles['Heading1'],
                        fontSize=16,
                        textColor=colors.darkgreen,
                        spaceAfter=12
                    )
                    
                    heading_style = ParagraphStyle(
                        'HeadingStyle',
                        parent=styles['Heading2'],
                        fontSize=14,
                        textColor=colors.darkgreen,
                        spaceAfter=6,
                        spaceBefore=12
                    )
                    
                    normal_style = styles['Normal']
                    normal_style.fontSize = 11
                    normal_style.spaceAfter = 6
                    
                    # Build PDF content
                    elements = []
                    
                    # Title
                    elements.append(Paragraph(f"{project['title']} - Project Report", title_style))
                    elements.append(Spacer(1, 0.25*inch))
                    
                    # Project Overview
                    elements.append(Paragraph("Project Overview", heading_style))
                    elements.append(Paragraph(project['description'], normal_style))
                    elements.append(Spacer(1, 0.1*inch))
                    
                    # Project Details
                    elements.append(Paragraph("Project Details", heading_style))
                    elements.append(Paragraph(f"<b>{get_translation(None, 'project_category')}:</b> {project['category']}", normal_style))
                    elements.append(Paragraph(f"<b>{get_translation(None, 'project_location')}:</b> {project['location']}", normal_style))
                    elements.append(Paragraph(f"<b>{get_translation(None, 'project_cost')}:</b> PKR {project['cost']}", normal_style))
                    elements.append(Paragraph(f"<b>{get_translation(None, 'project_impact')}:</b> {project['impact']}", normal_style))
                    elements.append(Spacer(1, 0.1*inch))
                    
                    # Implementation Plan
                    elements.append(Paragraph("Implementation Plan", heading_style))
                    elements.append(Paragraph(
                        f"The {project['title']} project aims to reduce carbon emissions through sustainable "
                        f"practices in {project['location']}. By supporting this initiative, you can offset "
                        f"your carbon footprint while contributing to local community development.", 
                        normal_style
                    ))
                    elements.append(Spacer(1, 0.1*inch))
                    
                    # Benefits
                    elements.append(Paragraph("Benefits", heading_style))
                    elements.append(Paragraph("• Reduces greenhouse gas emissions", normal_style))
                    elements.append(Paragraph("• Supports local communities", normal_style))
                    elements.append(Paragraph("• Contributes to Pakistan's climate goals", normal_style))
                    elements.append(Paragraph("• Promotes sustainable practices in Sindh", normal_style))
                    elements.append(Spacer(1, 0.1*inch))
                    
                    # How To Get Involved
                    elements.append(Paragraph("How To Get Involved", heading_style))
                    elements.append(Paragraph(
                        "To support this project, contact the Ecosphere AI team at contact@ecosphereai.org or visit our website.",
                        normal_style
                    ))
                    
                    # Footer
                    elements.append(Spacer(1, 0.5*inch))
                    elements.append(Paragraph(
                        "This report was generated by Ecosphere AI - Sustainable Climate Actions for Sindh",
                        ParagraphStyle(
                            'Footer',
                            parent=styles['Italic'],
                            textColor=colors.grey,
                            fontSize=9,
                            alignment=1  # Center alignment
                        )
                    ))
                    
                    # Build the PDF
                    doc.build(elements)
                    buffer.seek(0)
                    return buffer
                
                # Create download button for PDF report
                pdf_buffer = generate_pdf_report(project)
                st.download_button(
                    label=get_translation(None, "learn_more"),
                    data=pdf_buffer,
                    file_name=f"{project['title'].lower().replace(' ', '_')}_report.pdf",
                    mime="application/pdf",
                    key=f"download_{i}",
                    use_container_width=True
                )
            
            st.divider() 
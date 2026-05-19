"""
Knowledge Base module for Ecosphere AI.
Provides access to climate change information and resources.
"""

import streamlit as st
import pandas as pd
import io
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

# Define the custom_header function directly in this file to avoid import issues
def custom_header(title, description=None):
    """
    Display a custom header with title and optional description.
    
    Args:
        title (str): The title to display
        description (str, optional): Additional description text
    """
    # Determine colors based on theme
    if "theme" not in st.session_state:
        st.session_state.theme = "light"
        
    if st.session_state.theme == "dark":
        title_color = "#00E5FF"  # Bright cyan for dark theme
        desc_color = "#B0B0B0"
        border_color = "#1E4976"
        gradient_start = "#0A1929"
        gradient_end = "#132F4C"
        accent_color = "#00E5FF"
        shadow_color = "rgba(0, 229, 255, 0.3)"
    else:
        title_color = "#2196F3"  # Material blue for light theme
        desc_color = "#455A64"
        border_color = "#BBDEFB"
        gradient_start = "#F0F7FF"
        gradient_end = "#E3F2FD"
        accent_color = "#2196F3"
        shadow_color = "rgba(33, 150, 243, 0.2)"
    
    # Apply custom CSS for the header
    st.markdown(f"""
    <style>
    .beautiful-header {{
        background: linear-gradient(135deg, {gradient_start}, {gradient_end});
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 30px;
        box-shadow: 0 8px 32px {shadow_color};
        border: 1px solid {border_color};
        position: relative;
        overflow: hidden;
    }}
    
    .beautiful-header::before {{
        content: '';
        position: absolute;
        top: -50px;
        right: -50px;
        width: 100px;
        height: 100px;
        background: radial-gradient(circle, {accent_color}20, transparent);
        border-radius: 50%;
    }}
    
    .beautiful-header::after {{
        content: '';
        position: absolute;
        bottom: -30px;
        left: -30px;
        width: 60px;
        height: 60px;
        background: radial-gradient(circle, {accent_color}15, transparent);
        border-radius: 50%;
    }}
    
    .header-content {{
        position: relative;
        z-index: 2;
    }}
    
    .header-title {{
        color: {title_color};
        font-size: 32px;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        letter-spacing: 1px;
        font-family: 'Segoe UI', Arial, sans-serif;
    }}
    
    .header-description {{
        color: {desc_color};
        font-size: 18px;
        line-height: 1.6;
        margin-top: 10px;
        font-weight: 400;
        opacity: 0.9;
    }}
    
    .header-underline {{
        width: 100px;
        height: 4px;
        background: linear-gradient(90deg, {accent_color}, {title_color});
        border-radius: 2px;
        margin-top: 20px;
        box-shadow: 0 2px 8px {shadow_color};
    }}
    </style>
    """, unsafe_allow_html=True)
    
    # Create the header using Streamlit components
    with st.container():
        st.markdown(f"""
        <div class="beautiful-header">
            <div class="header-content">
                <div class="header-title">📚 {title}</div>
                {f'<div class="header-description">{description}</div>' if description else ''}
                <div class="header-underline"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Custom function to get translations
def get_translation(translations, key):
    """Get translation for the current language"""
    lang = st.session_state.get("language", "english")
    return translations[lang][key] if key in translations[lang] else key

def show_knowledge_base():
    """
    Display the knowledge base page with resources and information about climate change.
    """
    lang = st.session_state.get("language", "english")
    translations = {
        "english": {
            "title": "Knowledge Base",
            "description": "Access resources and information about climate change in Sindh.",
            "category_title": "Categories",
            "resources_title": "Resources",
            "search_placeholder": "Search for resources...",
            "no_results": "No results found. Try different search terms.",
            "featured": "Featured Resources",
            "recent": "Recent Updates",
            "download": "Download",
            "view": "View",
            "filter_by": "Filter by:",
            "all": "All",
            "research": "Research",
            "policy": "Policy",
            "guides": "Guides",
            "local": "Local"
        },
        "urdu": {
            "title": "معلوماتی مرکز",
            "description": "سندھ میں آب و ہوا کی تبدیلی کے بارے میں وسائل اور معلومات تک رسائی حاصل کریں۔",
            "category_title": "زمرہ جات",
            "resources_title": "وسائل",
            "search_placeholder": "وسائل کے لیے تلاش کریں...",
            "no_results": "کوئی نتیجہ نہیں ملا۔ مختلف تلاش کے الفاظ آزمائیں۔",
            "featured": "نمایاں وسائل",
            "recent": "حالیہ اپڈیٹس",
            "download": "ڈاؤن لوڈ",
            "view": "دیکھیں",
            "filter_by": "فلٹر کریں:",
            "all": "تمام",
            "research": "تحقیق",
            "policy": "پالیسی",
            "guides": "رہنما",
            "local": "مقامی"
        },
        "sindhi": {
            "title": "ڄاڻ جو مرڪز",
            "description": "سنڌ ۾ آب و هوا جي تبديلي بابت وسيلن ۽ معلومات تائين پهچ حاصل ڪريو.",
            "category_title": "زمرا",
            "resources_title": "وسيلا",
            "search_placeholder": "وسيلن لاءِ ڳولا ڪريو...",
            "no_results": "ڪوبه نتيجو نه مليو. مختلف ڳولا جا لفظ آزمايو.",
            "featured": "چونڊيل وسيلا",
            "recent": "تازا اپڊيٽس",
            "download": "ڊائون لوڊ",
            "view": "ڏسو",
            "filter_by": "فلٽر جي ذريعي:",
            "all": "سڀ",
            "research": "تحقيق",
            "policy": "پاليسي",
            "guides": "رهنمائي",
            "local": "مقامي"
        }
    }
    
    t = {k: get_translation(translations, k) for k in translations["english"].keys()}
    
    # Display header
    custom_header(t["title"], t["description"])
    
    # Add CSS for smaller filter button text
    st.markdown("""
    <style>
    /* Make filter buttons text smaller to prevent wrapping */
    div[data-testid="stButton"] button {
        font-size: 9px !important;
        padding: 6px 8px !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        line-height: 1.2 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Main layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Search functionality with better styling
        search_query = st.text_input(label="", placeholder=t["search_placeholder"])
        
        # Filter options
        st.write(t["filter_by"])
        filter_cols = st.columns(5)
        with filter_cols[0]:
            all_selected = st.button(t["all"], use_container_width=True, type="primary")
        with filter_cols[1]:
            research_selected = st.button(t["research"], use_container_width=True)
        with filter_cols[2]:
            policy_selected = st.button(t["policy"], use_container_width=True)
        with filter_cols[3]:
            guides_selected = st.button(t["guides"], use_container_width=True)
        with filter_cols[4]:
            local_selected = st.button(t["local"], use_container_width=True)
        
        # Resources list
        st.subheader(t["resources_title"])
        
        # Comprehensive resource database
        resources = [
            {
                "title": "Climate Change Impact Assessment in Sindh",
                "description": "A comprehensive report on how climate change affects different regions of Sindh.",
                "type": "Research",
                "format": "PDF",
                "date": "2023-01-15"
            },
            {
                "title": "Adaptation Strategies for Coastal Communities",
                "description": "Guidelines for communities in Thatta and Badin to adapt to rising sea levels.",
                "type": "Guide",
                "format": "PDF",
                "date": "2023-03-22"
            },
            {
                "title": "Renewable Energy Potential in Sindh",
                "description": "Analysis of solar and wind energy potential across different districts.",
                "type": "Research",
                "format": "Report",
                "date": "2022-11-05"
            },
            {
                "title": "Sindh Climate Change Policy",
                "description": "Official climate change policy document for Sindh province with focus areas and targets.",
                "type": "Policy",
                "format": "PDF",
                "date": "2023-02-18"
            },
            {
                "title": "Water Management in Changing Climate",
                "description": "Strategies for efficient water management in drought-prone areas of Sindh.",
                "type": "Guide",
                "format": "Handbook",
                "date": "2023-05-10"
            },
            {
                "title": "Agriculture Adaptation Techniques",
                "description": "Research on crop varieties and farming techniques suitable for changing climate in Sindh.",
                "type": "Research",
                "format": "Report",
                "date": "2023-04-30"
            },
            {
                "title": "Local Climate Stories from Tharparkar",
                "description": "Case studies and personal accounts of climate impacts from Tharparkar district.",
                "type": "Local",
                "format": "Article",
                "date": "2023-06-12"
            }
        ]
        
        # Filter resources based on search query and type filter
        filtered_resources = resources
        if search_query:
            filtered_resources = [r for r in resources if search_query.lower() in r["title"].lower() or search_query.lower() in r["description"].lower()]
        
        # Apply type filters
        if not all_selected:
            if research_selected:
                filtered_resources = [r for r in filtered_resources if r["type"] == "Research"]
            elif policy_selected:
                filtered_resources = [r for r in filtered_resources if r["type"] == "Policy"]
            elif guides_selected:
                filtered_resources = [r for r in filtered_resources if r["type"] == "Guide"]
            elif local_selected:
                filtered_resources = [r for r in filtered_resources if r["type"] == "Local"]
        
        if not filtered_resources:
            st.warning(t["no_results"])
        
        for item in filtered_resources:
            with st.container():
                col_a, col_b = st.columns([5, 1])
                with col_a:
                    st.markdown(f"**{item['title']}**")
                    st.markdown(item['description'])
                    st.caption(f"Type: {item['type']} | Format: {item['format']} | Date: {item['date']}")
                with col_b:
                    # Create PDF report function for each resource
                    def generate_pdf_report(resource):
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
                        elements.append(Paragraph(f"{resource['title']}", title_style))
                        elements.append(Spacer(1, 0.25*inch))
                        
                        # Resource Overview
                        elements.append(Paragraph("Resource Overview", heading_style))
                        elements.append(Paragraph(resource['description'], normal_style))
                        elements.append(Spacer(1, 0.1*inch))
                        
                        # Resource Details
                        elements.append(Paragraph("Resource Details", heading_style))
                        
                        data = [
                            ["Type", resource['type']],
                            ["Format", resource['format']],
                            ["Publication Date", resource['date']]
                        ]
                        
                        table = Table(data, colWidths=[2*inch, 3*inch])
                        table.setStyle(TableStyle([
                            ('BACKGROUND', (0, 0), (0, -1), colors.lightgreen),
                            ('TEXTCOLOR', (0, 0), (0, -1), colors.darkgreen),
                            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                            ('FONTSIZE', (0, 0), (-1, -1), 10),
                            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                        ]))
                        
                        elements.append(table)
                        elements.append(Spacer(1, 0.2*inch))
                        
                        # Sample Content - specific to each resource type
                        elements.append(Paragraph("Sample Content", heading_style))
                        
                        if resource['type'] == "Research":
                            elements.append(Paragraph("<b>Abstract:</b>", normal_style))
                            elements.append(Paragraph(
                                f"This research paper examines {resource['title'].lower()} in the context of climate change in Sindh province. "
                                f"The study collected data from multiple districts and analyzed patterns over a five-year period. "
                                f"Key findings indicate significant correlations between climate variables and local environmental conditions.",
                                normal_style
                            ))
                            elements.append(Paragraph("<b>Methodology:</b>", normal_style))
                            elements.append(Paragraph(
                                "Data was collected through field surveys, satellite imagery analysis, and meteorological records. "
                                "Statistical analysis included multivariate regression and time-series analysis using R and Python.",
                                normal_style
                            ))
                            elements.append(Paragraph("<b>Key Findings:</b>", normal_style))
                            elements.append(Paragraph(
                                "• Significant increase in average temperatures across all districts\n"
                                "• Changes in precipitation patterns affecting agricultural productivity\n"
                                "• Correlation between climate variables and environmental indicators",
                                normal_style
                            ))
                        elif resource['type'] == "Policy":
                            elements.append(Paragraph("<b>Executive Summary:</b>", normal_style))
                            elements.append(Paragraph(
                                f"This policy document outlines the strategic framework for addressing {resource['title'].lower()}. "
                                f"It provides guidelines for government agencies, NGOs, and local communities to coordinate efforts "
                                f"in building climate resilience and implementing sustainable practices.",
                                normal_style
                            ))
                            elements.append(Paragraph("<b>Policy Objectives:</b>", normal_style))
                            elements.append(Paragraph(
                                "• Establish a coordinated approach to climate adaptation and mitigation\n"
                                "• Define roles and responsibilities of various stakeholders\n"
                                "• Set measurable targets for climate action in Sindh",
                                normal_style
                            ))
                            elements.append(Paragraph("<b>Implementation Timeline:</b>", normal_style))
                            elements.append(Paragraph(
                                "2023-2025: Initial assessment and planning phase\n"
                                "2025-2027: Implementation of priority actions\n"
                                "2027-2030: Scaling successful initiatives and policy revision",
                                normal_style
                            ))
                        elif resource['type'] == "Guide":
                            elements.append(Paragraph("<b>Introduction:</b>", normal_style))
                            elements.append(Paragraph(
                                f"This practical guide provides actionable steps for implementing {resource['title'].lower()}. "
                                f"It is designed for community leaders, local government officials, and individuals seeking to "
                                f"contribute to climate resilience in their areas.",
                                normal_style
                            ))
                            elements.append(Paragraph("<b>Practical Steps:</b>", normal_style))
                            elements.append(Paragraph(
                                "1. Assess local vulnerabilities and resources\n"
                                "2. Develop a context-specific action plan\n"
                                "3. Implement small-scale pilot initiatives\n"
                                "4. Monitor results and adjust approaches\n"
                                "5. Scale successful practices",
                                normal_style
                            ))
                            elements.append(Paragraph("<b>Case Study:</b>", normal_style))
                            elements.append(Paragraph(
                                "A community in Thatta district successfully implemented these practices, resulting in improved "
                                "water management and reduced vulnerability to climate impacts.",
                                normal_style
                            ))
                        else:  # Local
                            elements.append(Paragraph("<b>Community Perspectives:</b>", normal_style))
                            elements.append(Paragraph(
                                f"This document captures local experiences and knowledge related to {resource['title'].lower()}. "
                                f"Through interviews and participatory research, it documents how communities are experiencing "
                                f"and responding to climate change impacts.",
                                normal_style
                            ))
                            elements.append(Paragraph("<b>Key Insights:</b>", normal_style))
                            elements.append(Paragraph(
                                "• Local observations of changing weather patterns\n"
                                "• Traditional knowledge useful for adaptation\n"
                                "• Community-led initiatives for resilience\n"
                                "• Challenges and support needs identified by residents",
                                normal_style
                            ))
                        
                        # Footer
                        elements.append(Spacer(1, 0.5*inch))
                        elements.append(Paragraph(
                            "This document was generated by Ecosphere AI - Sustainable Climate Actions for Sindh",
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
                    pdf_buffer = generate_pdf_report(item)
                    st.download_button(
                        label=t["download"],
                        data=pdf_buffer,
                        file_name=f"{item['title'].lower().replace(' ', '_')}.pdf",
                        mime="application/pdf",
                        key=f"download_{item['title']}",
                        use_container_width=True
                    )
                st.divider()
    
    with col2:
        # Featured resources section
        st.subheader(t["featured"])
        with st.container():
            st.image("https://images.unsplash.com/photo-1598335624134-5bceb5de202d?w=300&h=200&fit=crop&q=80", use_container_width=True)
            st.markdown("**IPCC Sixth Assessment Report: Regional Focus**")
            st.markdown("Key findings relevant to South Asia and Pakistan")
            st.button(t["view"], key="view_featured_1", use_container_width=True)
        
        st.divider()
        
        # Recent updates
        st.subheader(t["recent"])
        updates = [
            "New policy brief on coastal protection measures (2 days ago)",
            "Updated rainfall patterns visualization (1 week ago)",
            "New case study on urban heat islands in Karachi (2 weeks ago)"
        ]
        
        for i, update in enumerate(updates):
            st.markdown(f"• {update}")
        
        # Climate change categories with icons
        st.divider()
        st.subheader(t["category_title"])
        
        categories = {
            "🌡️ Climate Science": "Scientific data and research",
            "🌱 Adaptation": "Adapting to climate impacts",
            "🔄 Mitigation": "Reducing emissions",
            "📜 Policy": "Government policies and plans",
            "🏙️ Local Impact": "Effects on Sindh communities"
        }
        
        for cat, desc in categories.items():
            with st.container():
                st.markdown(f"**{cat}**")
                st.caption(desc)
                st.divider() 
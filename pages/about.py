"""
About module for GreenAI.
Provides information about the application, its purpose, and creators.
"""

import streamlit as st
from utils.ui import get_translation
import base64

def get_image_base64(image_path):
    """Convert image to base64 for embedding in HTML"""
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
            return encoded_string
    except Exception as e:
        st.error(f"Error loading image {image_path}: {str(e)}")
        return None

def show_about():
    """
    Display the about page for GreenAI.
    """
    lang = st.session_state.get("language", "english")
    translations = {
        "english": {
            "description": "Learn about our mission and how we're helping communities in Sindh adapt to climate change.",
            "mission_title": "Our Mission",
            "mission_text": "GreenAI aims to provide accessible, multilingual climate information and tools to help communities in Sindh understand, adapt to, and mitigate the impacts of climate change.",
            "features_title": "Key Features",
            "contact_title": "Contact Us",
            "feedback_title": "Feedback",
            "feedback_placeholder": "Share your thoughts or suggestions...",
            "feedback_button": "Submit Feedback",
            "thanks_message": "Thank you for your feedback!"
        },
        "urdu": {
            "description": "ہمارے مشن اور آب و ہوا کی تبدیلی سے موافقت میں سندھ کے برادریوں کی مدد کرنے کے بارے میں جانیں۔",
            "mission_title": "ہمارا مشن",
            "mission_text": "گرین اے آئی کا مقصد سندھ میں برادریوں کو آب و ہوا کی تبدیلی کے اثرات کو سمجھنے، ان سے موافقت کرنے اور ان کو کم کرنے میں مدد کے لیے قابل رسائی، کثیر لسانی آب و ہوا کی معلومات اور ٹولز فراہم کرنا ہے۔",
            "features_title": "اہم خصوصیات",
            "contact_title": "ہم سے رابطہ کریں",
            "feedback_title": "آراء",
            "feedback_placeholder": "اپنے خیالات یا تجاویز شیئر کریں...",
            "feedback_button": "فیڈبیک جمع کریں",
            "thanks_message": "آپ کی فیڈبیک کے لیے شکریہ!"
        },
        "sindhi": {
            "description": "اسان جي مشن ۽ سنڌ ۾ برادرين کي آب و هوا جي تبديلي سان موافقت ۾ مدد ڪرڻ بابت ڄاڻو.",
            "mission_title": "اسان جو مشن",
            "mission_text": "گرين اي آءِ جو مقصد سنڌ ۾ برادرين کي آب و هوا جي تبديلي جي اثرن کي سمجهڻ، انهن سان موافقت ڪرڻ ۽ انهن کي گهٽائڻ ۾ مدد لاءِ قابل رسائي، ڪثير لساني آب و هوا جي معلومات ۽ اوزارن فراهم ڪرڻ آهي.",
            "features_title": "اهم خصوصيتون",
            "contact_title": "اسان سے رابطہ کريں",
            "feedback_title": "راءِ",
            "feedback_placeholder": "پنهنجا خيال يا تجويزون شيئر ڪريو...",
            "feedback_button": "فيڊبيڪ جمع ڪريو",
            "thanks_message": "توهان جي فيڊبيڪ لاءِ مهرباني!"
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
                🤖 About GreenAI
            </h1>
            <p style="
                color: #455A64;
                font-size: 1.2rem;
                margin: 1rem 0 0 0;
                font-weight: 500;
                opacity: 0.9;
            ">
                Learn about our mission and how we're helping communities in Sindh adapt to climate change
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Mission section with enhanced styling
    st.markdown("""
    <div style='background: linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 100%); padding: 30px; border-radius: 15px; margin: 20px 0;'>
        <h2 style='color: #1976D2; margin-bottom: 20px;'>Our Mission</h2>
        <p style='color: #455A64; font-size: 1.1rem; line-height: 1.6;'>GreenAI aims to provide accessible, multilingual climate information and tools to help communities in Sindh understand, adapt to, and mitigate the impacts of climate change.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key features section with enhanced styling
    st.markdown("""
    <style>
    .features-container {
        background: #ffffff;
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .features-header {
        color: #1E88E5;
        font-size: 2rem;
        font-weight: 600;
        margin-bottom: 2rem;
        text-align: center;
    }
    .feature-card {
        background: #f8f9fa;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid #1E88E5;
        transition: transform 0.3s ease;
    }
    .feature-card:hover {
        transform: translateX(10px);
        background: #f0f7ff;
    }
    .feature-icon {
        font-size: 2rem;
        margin-bottom: 1rem;
        color: #1E88E5;
    }
    .feature-title {
        color: #1E88E5;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 0.8rem;
    }
    .feature-description {
        color: #455A64;
        font-size: 1.1rem;
        line-height: 1.6;
        margin: 0;
    }
    .team-card {
        background: linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 100%);
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
        min-height: 450px;
    }
    .team-card:hover {
        transform: translateY(-5px);
    }
    .profile-image {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        margin-bottom: 20px;
        border: 4px solid #FFFFFF;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        object-fit: cover;
        object-position: top;
    }
    .team-name {
        color: #1976D2;
        margin: 5px 0;
        font-size: 1.4rem;
        font-weight: 600;
    }
    .team-role {
        color: #455A64;
        font-size: 1.2rem;
        margin: 5px 0;
        font-weight: 500;
    }
    .team-description {
        color: #455A64;
        font-size: 1rem;
        margin: 10px 0;
        line-height: 1.5;
    }
    .team-contact {
        color: #1976D2;
        text-decoration: none;
        font-size: 1rem;
        display: inline-block;
        margin-top: 10px;
    }
    .social-links {
        margin-top: 15px;
    }
    .social-links a {
        color: #1976D2;
        margin: 0 10px;
        font-size: 1.2rem;
        text-decoration: none;
    }
    </style>
    """, unsafe_allow_html=True)

    # Features container
    st.markdown('<div class="features-container">', unsafe_allow_html=True)
    
    # Features header
    st.markdown('<h2 class="features-header">Key Features</h2>', unsafe_allow_html=True)
    
    features = [
        {
            "icon": "🌍",
            "title": "Multilingual Support",
            "description": "Available in English, Urdu, and Sindhi to serve diverse communities."
        },
        {
            "icon": "🤖",
            "title": "AI-Powered Assistant",
            "description": "Advanced AI to answer questions about climate change in Sindh."
        },
        {
            "icon": "📊",
            "title": "Data Visualizations",
            "description": "Interactive charts and maps to understand climate impacts."
        },
        {
            "icon": "🌡️",
            "title": "Weather Integration",
            "description": "Real-time weather data for districts in Sindh."
        },
        {
            "icon": "🌱",
            "title": "Carbon Calculator",
            "description": "Tools to estimate and reduce your carbon footprint."
        }
    ]
    
    # Display features
    for feature in features:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">{feature['icon']}</div>
            <div class="feature-title">{feature['title']}</div>
            <div class="feature-description">{feature['description']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Team section with enhanced styling
    st.markdown("""
    <div style='margin: 40px 0;'>
        <h2 style='color: #1976D2; margin-bottom: 30px; text-align: center;'>Our Team</h2>
        <p style='color: #455A64; font-size: 1.1rem; text-align: center; margin-bottom: 30px;'>Meet the dedicated team behind GreenAI</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create columns for team members
    col1, col2, col3 = st.columns(3)
    
    # Team member cards with detailed information
    with col1:
        st.markdown(f"""
        <div class="team-card">
            <img src="data:image/jpeg;base64,{get_image_base64('assets/profiles/faiza.jpg')}" 
                 alt="Faiza Soomro" 
                 class="profile-image"
                 onerror="this.src='https://i.pravatar.cc/150?img=1'">
            <h3 class="team-name">Faiza Soomro</h3>
            <p class="team-role">Group Leader & Lead Developer</p>
            <p class="team-description">The driving force behind the project. Faiza led the team, handled all development, and ensured the project's successful completion from start to finish.</p>
            <a href="mailto:faizaoomro780@gmail.com" class="team-contact">faizaoomro780@gmail.com</a>
            <div class="social-links">
                <a href="https://linkedin.com/in/faizasoomro" target="_blank">LinkedIn</a>
                <a href="https://github.com/faizasoomro" target="_blank">GitHub</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="team-card">
            <img src="data:image/jpeg;base64,{get_image_base64('assets/profiles/damini.jpg')}" 
                 alt="Damini Lohana" 
                 class="profile-image"
                 onerror="this.onerror=null; this.src='https://i.pravatar.cc/150?img=5';">
            <h3 class="team-name">Damini Lohana</h3>
            <p class="team-role">Team Member</p>
            <p class="team-description">Contributed ideas, participated in discussions, and supported the documentation and presentation process.</p>
            <a href="mailto:daminilohana@gmail.com" class="team-contact">daminilohana@gmail.com</a>
            <div class="social-links">
                <a href="https://linkedin.com/in/daminilohana" target="_blank">LinkedIn</a>
                <a href="https://github.com/daminilohana" target="_blank">GitHub</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="team-card">
            <img src="data:image/jpeg;base64,{get_image_base64('assets/profiles/sahrish.jpg')}" 
                 alt="Sahrish Turk" 
                 class="profile-image"
                 onerror="this.onerror=null; this.src='https://i.pravatar.cc/150?img=8';">
            <h3 class="team-name">Sahrish Turk</h3>
            <p class="team-role">Team Member</p>
            <p class="team-description">Assisted with research, testing, and overall coordination during different phases of the project. Supported data gathering and analysis.</p>
            <a href="mailto:sahrishturk8@gmail.com" class="team-contact">sahrishturk8@gmail.com</a>
            <div class="social-links">
                <a href="https://linkedin.com/in/sahrishturk" target="_blank">LinkedIn</a>
                <a href="https://github.com/sahrishturk" target="_blank">GitHub</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Team achievements with enhanced styling
    st.markdown("""
    <div style='background: linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 100%); padding: 30px; border-radius: 20px; margin: 40px 0; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        <h2 style='color: #1976D2; margin-bottom: 25px; font-size: 1.8rem; text-align: center;'>Team Achievements</h2>
        <div style='display: flex; flex-direction: column; gap: 15px;'>
            <div style='background: rgba(255, 255, 255, 0.9); padding: 15px; border-radius: 12px; display: flex; align-items: center; gap: 15px;'>
                <span style='color: #1976D2; font-size: 1.5rem;'>✓</span>
                <p style='color: #455A64; font-size: 1.1rem; margin: 0;'>Developed a multilingual climate information system</p>
            </div>
            <div style='background: rgba(255, 255, 255, 0.9); padding: 15px; border-radius: 12px; display: flex; align-items: center; gap: 15px;'>
                <span style='color: #1976D2; font-size: 1.5rem;'>✓</span>
                <p style='color: #455A64; font-size: 1.1rem; margin: 0;'>Implemented real-time weather data integration</p>
            </div>
            <div style='background: rgba(255, 255, 255, 0.9); padding: 15px; border-radius: 12px; display: flex; align-items: center; gap: 15px;'>
                <span style='color: #1976D2; font-size: 1.5rem;'>✓</span>
                <p style='color: #455A64; font-size: 1.1rem; margin: 0;'>Created an AI-powered chatbot for climate queries</p>
            </div>
            <div style='background: rgba(255, 255, 255, 0.9); padding: 15px; border-radius: 12px; display: flex; align-items: center; gap: 15px;'>
                <span style='color: #1976D2; font-size: 1.5rem;'>✓</span>
                <p style='color: #455A64; font-size: 1.1rem; margin: 0;'>Built interactive data visualizations</p>
            </div>
            <div style='background: rgba(255, 255, 255, 0.9); padding: 15px; border-radius: 12px; display: flex; align-items: center; gap: 15px;'>
                <span style='color: #1976D2; font-size: 1.5rem;'>✓</span>
                <p style='color: #455A64; font-size: 1.1rem; margin: 0;'>Integrated carbon footprint calculation tools</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Custom CSS for enhanced styling
    st.markdown("""
    <style>
    .main-header {
        color: #1976D2;
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .section-header {
        color: #1976D2;
        font-size: 2rem;
        font-weight: 600;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #1976D2;
    }
    .supervisor-card {
        background: linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 2rem 0;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    .supervisor-card:hover {
        transform: translateY(-5px);
    }
    .gratitude-box {
        background: rgba(227, 242, 253, 0.7);
        padding: 2rem;
        border-radius: 15px;
        margin: 1.5rem 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        border-left: 5px solid #1976D2;
    }
    .contact-box {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        height: 100%;
        transition: transform 0.3s ease;
    }
    .contact-box:hover {
        transform: translateY(-3px);
    }
    .contact-header {
        color: #1976D2;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    .contact-text {
        color: #455A64;
        font-size: 1.2rem;
        line-height: 1.6;
    }
    .version-info {
        text-align: center;
        margin: 3rem 0;
        padding: 1.5rem;
        background: linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 100%);
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    }
    .contact-section {
        background: linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .contact-item {
        display: flex;
        align-items: center;
        margin: 1.5rem 0;
        padding: 1rem;
        background: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        transition: transform 0.3s ease;
    }
    .contact-item:hover {
        transform: translateY(-3px);
    }
    .contact-icon {
        font-size: 2rem;
        margin-right: 1.5rem;
        color: #1976D2;
    }
    .contact-link {
        color: #1976D2;
        text-decoration: none;
        font-weight: 500;
    }
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    .contact-card {
        background: linear-gradient(135deg, #1E88E5 0%, #1565C0 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 2rem 0;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        color: white;
    }
    .contact-header {
        display: flex;
        align-items: center;
        margin-bottom: 1.5rem;
    }
    .contact-logo {
        width: 50px;
        height: 50px;
        margin-right: 1rem;
    }
    .contact-title {
        font-size: 1.8rem;
        font-weight: 600;
        margin: 0;
        color: white;
    }
    .contact-info {
        background: rgba(255, 255, 255, 0.1);
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .contact-label {
        color: white;
        font-size: 1.1rem;
        margin: 0;
    }
    .contact-value {
        color: white;
        font-size: 1.2rem;
        font-weight: 500;
        margin: 0.5rem 0 0 0;
    }
    </style>
    """, unsafe_allow_html=True)

    # Acknowledgements section with enhanced styling
    st.markdown('<h1 class="main-header">Acknowledgements</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Project Supervisor</h2>', unsafe_allow_html=True)
    
    # Supervisor card with enhanced styling
    st.markdown("""
    <div class="supervisor-card">
        <h3 style="color: #1976D2; margin: 0 0 1rem 0; font-size: 1.8rem; font-weight: 600;">Madam Zojan Memon</h3>
        <p style="color: #455A64; font-size: 1.4rem; margin: 0.5rem 0; font-weight: 500;">Supervisor</p>
        <p style="color: #455A64; font-size: 1.2rem; margin: 0.5rem 0;">Department of Computer Science</p>
        <p style="color: #455A64; font-size: 1.2rem; margin: 0.5rem 0; font-weight: 500;">UNIVERSITY OF SUFISM AND MODERN SCIENCES, BHITSHAH</p>
    </div>
    """, unsafe_allow_html=True)

    # Gratitude message with enhanced styling
    st.markdown("""
    <div class="gratitude-box">
        <p style="color: #455A64; font-size: 1.3rem; line-height: 1.8; margin: 0; text-align: justify;">
            We would like to express our deepest gratitude to our supervisor, Madam Zojan Memon, for her invaluable guidance, continuous support, and expert advice throughout the development of this project. Her mentorship has been instrumental in shaping GreenAI into what it is today.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Additional thanks with enhanced styling
    st.markdown("""
    <div class="gratitude-box">
        <p style="color: #455A64; font-size: 1.3rem; line-height: 1.8; margin: 0; text-align: justify;">
            We also extend our thanks to our mentors, teachers, and the open-source community for their support and guidance in developing this project.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Contact section
    st.markdown("""
    <style>
    .contact-container {
        background: #ffffff;
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .contact-header {
        color: #1E88E5;
        font-size: 2rem;
        font-weight: 600;
        margin-bottom: 2rem;
        text-align: center;
    }
    .contact-item {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        border-left: 4px solid #1E88E5;
        transition: transform 0.3s ease;
    }
    .contact-item:hover {
        transform: translateX(10px);
        background: #f0f7ff;
    }
    .contact-label {
        color: #1E88E5;
        font-size: 1.2rem;
        font-weight: 500;
        margin-bottom: 1.2rem;
        display: block;
    }
    .contact-value {
        color: #455A64;
        font-size: 1.1rem;
        margin: 0;
        padding-left: 0.5rem;
        display: block;
        margin-top: 0.5rem;
    }
    .contact-link {
        color: #1E88E5;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    .contact-link:hover {
        color: #1565C0;
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)

    # Contact container
    st.markdown('<div class="contact-container">', unsafe_allow_html=True)
    
    # Contact header
    st.markdown('<h2 class="contact-header">Contact Us</h2>', unsafe_allow_html=True)
    
    # Email section
    st.markdown("""
    <div class="contact-item">
        <div class="contact-label">📧 Email</div>
        <div class="contact-value">
            <a href="mailto:faizaoomro780@gmail.com" class="contact-link">faizaoomro780@gmail.com</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Phone section
    st.markdown("""
    <div class="contact-item">
        <div class="contact-label">📱 Phone</div>
        <div class="contact-value">
            <a href="tel:+923070021780" class="contact-link">+92 307 0021780</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
   
    
    # Office Address section
    st.markdown("""
    <div class="contact-item">
        <div class="contact-label">🏢 Office Address</div>
        <div class="contact-value">
            Department of Computer Science<br>
            University of Sufism and Modern Sciences<br>
            Bhitshah, Sindh, Pakistan
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Feedback section
    st.markdown("""
    <style>
    .feedback-container {{
        background: #ffffff;
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }}
    .feedback-header {{
        color: #1E88E5;
        font-size: 1.8rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
    }}
    </style>
    """, unsafe_allow_html=True)

    # Feedback container
    st.markdown('<div class="feedback-container">', unsafe_allow_html=True)
    
    # Feedback header
    st.markdown('<h2 class="feedback-header">Share Your Feedback</h2>', unsafe_allow_html=True)
    
    # Feedback form
    feedback = st.text_area("", placeholder=t["feedback_placeholder"], height=150)
    
    if st.button(t["feedback_button"], type="primary"):
        st.success(t["thanks_message"])
        
    st.markdown('</div>', unsafe_allow_html=True)
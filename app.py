import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Yishuai Zheng",
    page_icon="🧑‍💻",
    layout="wide"
)

# Custom CSS (keep all your original CSS)
st.markdown("""
<style>
    /* Main Styles */
    .main-header {
        font-size: 3rem !important;
        font-weight: 700 !important;
        color: #19795B !important;
    }
    .sub-header {
        font-size: 2rem !important;
        font-weight: 600 !important;
        color: #49AE8E !important;
    }
    .section-header {
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        color: #11684C !important;
    }
    .highlight {
        color: #19795B;
        font-weight: 600;
    }
    .card {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background-color: #f8f9fa;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    .project-card {
        padding: 2rem;
        border-radius: 0.7rem;
        background-color: #f1f7fe;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 1.5rem;
        border-left: 5px solid #1E88E5;
    }
    hr {
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    
    /* Custom sidebar styling */
    .css-1d391kg, .css-1v3fvcr {
        background-color: #f5f5f5;
    }
    
    /* Style for sidebar tabs */
    .sidebar-tabs {
        display: flex;
        flex-direction: column;
        width: 100%;
        margin-top: 1rem;
        gap: 8px;
    }
    
    .sidebar-tab {
        padding: 10px;
        border-radius: 5px;
        background-color: #e0e0e0;
        cursor: pointer;
        transition: all 0.3s;
        display: flex;
        align-items: center;
    }
    
    .sidebar-tab:hover, .sidebar-tab.active {
        background-color: #19795B;
        color: white;
    }
    
    .sidebar-tab-icon {
        margin-right: 10px;
    }
    
    /* Timeline styles */
    .timeline-container {
        position: relative;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .timeline-container::after {
        content: '';
        position: absolute;
        width: 6px;
        background-color: #ddd;
        top: 0;
        bottom: 0;
        left: 32px;
        margin-left: -3px;
    }
    
    .timeline-item {
        padding: 20px 40px;
        position: relative;
        background-color: #f8f9fa;
        border-radius: 6px;
        margin-bottom: 30px;
        margin-left: 50px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    
    .timeline-item::before {
        content: '';
        position: absolute;
        width: 25px;
        height: 25px;
        border-radius: 50%;
        background-color: #19795B;
        border: 4px solid #fff;
        left: -59px;
        top: 20px;
        z-index: 1;
    }
    
    .timeline-experience::before {
        background-color: #1E88E5;
    }
    
    .timeline-date {
        font-weight: 700;
        color: #19795B;
        margin-bottom: 5px;
        font-size: 1.1rem;
    }
    
    .timeline-experience .timeline-date {
        color: #1E88E5;
    }
    
    .timeline-title {
        font-weight: 600;
        margin-bottom: 8px;
        font-size: 1.2rem;
    }
    
    .timeline-desc {
        font-size: 0.95rem;
        color: #555;
    }
    
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
</style>
""", unsafe_allow_html=True)

# Create a session state variable for navigation
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Create sidebar with tab navigation
with st.sidebar:
    st.write("<span style='font-size: 150px;'>🔍</span>", unsafe_allow_html=True)
    st.markdown("## Yishuai Zheng")
    st.markdown("#### Product Designer (UXUI)")
    st.markdown("---")
    
    # Create navigation tabs
    # Highlight active tab by disabling the button
    tab_home = st.button("😈 Home", use_container_width=True, disabled=(st.session_state.page == "Home"))
    tab_projects = st.button("🌇 Projects", use_container_width=True, disabled=(st.session_state.page == "Projects"))
    tab_resume = st.button("👾 Resume", use_container_width=True, disabled=(st.session_state.page == "Resume"))
    tab_contact = st.button("🍻 Contact", use_container_width=True, disabled=(st.session_state.page == "Contact"))
    
    # Fixed navigation logic - Using st.rerun() properly
    if tab_home and st.session_state.page != "Home":
        st.session_state.page = "Home"
        st.rerun()
    if tab_projects and st.session_state.page != "Projects":
        st.session_state.page = "Projects"
        st.rerun()
    if tab_resume and st.session_state.page != "Resume":
        st.session_state.page = "Resume"
        st.rerun()
    if tab_contact and st.session_state.page != "Contact":
        st.session_state.page = "Contact"
        st.rerun()
    
    st.markdown("---")
    st.markdown("### Connect")
    st.markdown("[Email](mailto:yishuaiz@uw.edu)")
    st.markdown("[Portfolio](http://www.yishuaizheng.com)")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/yishuai-zheng-067892201/)")
    st.markdown("[GitHub](https://github.com/Yishuai1108)")

# HOME PAGE
if st.session_state.page == "Home":
    st.markdown('<h1 class="main-header">Hello, I\'m Yishuai Zheng!</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-header">Product Designer & Technology Innovator</h2>', unsafe_allow_html=True)
    
    # Profile introduction with photo
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### About Me
        
        I'm a product designer with expertise in UXUI design, currently pursuing a Master's in 
        Technology Innovation at the University of Washington. With professional experience at 
        companies like VIPSHOP, Capgemini, and RayInsight Venture, I specialize in user research, 
        UXUI design, web development, and both hardware and software prototyping.
        
        My design philosophy centers around <span class="highlight">creating intuitive and impactful 
        user experiences</span> that solve real problems. I believe in the power of thoughtful 
        design to transform how people interact with technology.
        """, unsafe_allow_html=True)
    
    with col2:
        st.image("assets/profile.jpg", use_column_width=True)
    
    # Projects Overview Section
    st.markdown('<h2 class="sub-header">Projects Overview</h2>', unsafe_allow_html=True)
    st.markdown("I approach design with a user-centered mindset, focusing on:")
    
    # Create columns with minimal width (forces them to expand)
    cols = st.columns(3, gap="large")
    
    # Define projects
    projects = [
        {"image": "assets/figure1.png", "text": "Cat Health Monitoring App"},
        {"image": "assets/figure2.png", "text": "AI Mental Health Chatbot"},
        {"image": "assets/figure3.png", "text": "Elder Version of Grocery Shopping"},
    ]
    
    # Display projects in columns
    for i, project in enumerate(projects):
        with cols[i]:
            st.image(project["image"], use_column_width=True)
            st.markdown(f"<p style='text-align: center;'>{project['text']}</p>", unsafe_allow_html=True)
    
    st.markdown('<div style="margin-bottom: 40px;"></div>', unsafe_allow_html=True)
    
    # Skills Section
    st.markdown('<h2 class="sub-header">Core Skills</h2>', unsafe_allow_html=True)
    skill_cols = st.columns(7, gap="medium")
    skills = [
        {"icon": "assets/icon1.png", "text": "User Research"},
        {"icon": "assets/icon2.png", "text": "UI Design"},
        {"icon": "assets/icon3.png", "text": "Coding"},
        {"icon": "assets/icon4.png", "text": "Hardware Prototyping"},
        {"icon": "assets/icon5.png", "text": "3D Modeling"},
        {"icon": "assets/icon6.png", "text": "Animation Design"},
        {"icon": "assets/icon7.png", "text": "Video Editing"},
    ]
    
    # Display each skill in its column
    for i, skill in enumerate(skills):
        if i < len(skill_cols):  # Make sure we don't exceed the number of columns
            with skill_cols[i]:
                st.image(skill["icon"], use_column_width=True)
                st.markdown(f"<p style='text-align: center; font-size: 0.7em;'>{skill['text']}</p>", unsafe_allow_html=True)
    
    # Timeline / Experience with brief descriptions
    st.markdown('<h2 class="sub-header">My Journey</h2>', unsafe_allow_html=True)
    
    # Timeline data with both education and experience
    timeline_data = [
        {"year": "2026", "event": "Completed MS in Technology Innovation", "type": "Education", "description": "Graduated with specialization in product design and technology innovation from University of Washington."},
        {"year": "2024", "event": "Started MS in Technology Innovation", "type": "Education", "description": "Began graduate studies at University of Washington, focusing on advanced design methodologies and emerging technologies."},
        {"year": "2023", "event": "UIUX Intern at VIPSHOP & Capgemini", "type": "Experience", "description": "Designed financial services UI that increased click-through rate from 2.4% to 5.1% and follower engagement by 22%."},
        {"year": "2023", "event": "Product Designer at RayInsight Venture", "type": "Experience", "description": "Led brand identity development and website design, implementing information architecture based on stakeholder interviews."},
        {"year": "2023", "event": "Graduated with BFA in Interaction Design", "type": "Education", "description": "Completed undergraduate degree at School of Visual Arts with 3.86 GPA and honors recognition."},
        {"year": "2021", "event": "Product Design Intern at Hangar Design Group", "type": "Experience", "description": "Redesigned ALTER's Tmall store UI, enhancing visual impact and increasing click-through rates."},
        {"year": "2019", "event": "Started BFA in Interaction Design", "type": "Education", "description": "Began undergraduate studies at School of Visual Arts, focusing on interaction design fundamentals."}
    ]
    
    # Create enhanced timeline with education/experience distinction
    st.markdown('<div class="timeline-container">', unsafe_allow_html=True)
    for item in timeline_data:
        css_class = "timeline-education" if item["type"] == "Education" else "timeline-experience"
        
        st.markdown(f"""
        <div class="timeline-item {css_class}">
            <div class="timeline-date">{item["year"]} - {item["type"]}</div>
            <div class="timeline-title">{item["event"]}</div>
            <div class="timeline-desc">{item["description"]}</div>
        </div>
        """, unsafe_allow_html=True)

# PROJECTS PAGE
elif st.session_state.page == "Projects":
    st.markdown('<h1 class="main-header">My Projects</h1>', unsafe_allow_html=True)
    st.markdown("""
    Here are some selected projects that showcase my skills in user research, 
    design thinking, and product development.
    """)
    
    # Project 1
    st.markdown('<h2 class="sub-header">Psychological Counseling AI Chatbot</h2>', unsafe_allow_html=True)
    
    proj1_col1, proj1_col2 = st.columns([2, 3])
    
    with proj1_col1:
        st.image("assets/figure2.png", use_column_width=True)
        
        with st.expander("View Process"):
            st.markdown("""
            1. **Research**: Conducted literature review and interviewed individuals with various mental health issues
            2. **Analysis**: Analyzed competitors like ChatGPT, Bard, and Bing Chat
            3. **Ideation**: Brainstormed methods to enhance trust between users and AI
            4. **Design**: Created character-based interactions with humanized dialogues
            5. **Testing**: Performed usability tests with potential users
            6. **Iteration**: Refined design based on feedback
            """)
    
    with proj1_col2:
        st.markdown("""
        ### Overview
        
        Addressed mental health issues by developing an AI therapy chatbot based on psychological principles and a 
        patient-therapist matching system using the Big Five Model.
        
        ### Key Features
        - AI-powered conversations rooted in psychological therapeutic approaches
        - Personalized therapist matching algorithm
        - Trust-building character design
        - Humanized dialogue system
        
        ### Outcomes
        - Created a low-barrier entry point for individuals hesitant to begin traditional therapy
        - Designed an intuitive interface that encouraged user engagement
        - Developed a system that could effectively match users with appropriate human therapists when needed
        """)
    
    
    # Project 2
    st.markdown('<h2 class="sub-header">Cat Health Monitoring App</h2>', unsafe_allow_html=True)
    
    proj2_col1, proj2_col2 = st.columns([2, 3])
    
    with proj2_col1:
        st.image("assets/figure1.png", use_column_width=True)
        
    
    with proj2_col2:
        st.markdown("""
        ### Overview
        
        Designed an integrated solution—water dispenser, litter box, and companion app—to 
        monitor cat hydration and hygiene, aimed at preventing feline urinary stones.
        
        ### Approach
        - Led brainstorming and tested 14 ideas with users, narrowing down to 3 optimal solutions
        - Developed an Emotion Map to visualize user experience improvements before and after using 
        the system
        - Focused on both health tracking and user peace of mind through seamless product-app integration
        
        
        ### Results
        - Delivered a comprehensive product ecosystem addressing key pet health concerns
        - Demonstrated clear emotional and functional benefits through design artifacts
        
        ### Key Learnings
        - Holistic product design enhances both user and pet well-being
        - Iterative testing is essential for refining multi-component solutions
        - Emotional mapping helps reveal user value beyond functional metrics
        """)
    
    # Project 3
    st.markdown('<h2 class="sub-header">Senior Users Version of Freshippo App</h2>', unsafe_allow_html=True)
    
    proj3_col1, proj3_col2 = st.columns([2, 3])
    
    with proj3_col1:
        st.image("assets/figure3.png", use_column_width=True)
    
    with proj3_col2:
        st.markdown("""
        ### Overview
        
        Redesigned a fresh food shopping app to better serve senior users (50+) by focusing 
        on food quality, pricing, accessibility, and usability.
        
        ### Approach
        - Interviewed seniors to uncover key pain points and needs
        - Analyzed five grocery apps with a senior-focus using a star rating system
        - Designed three core features: food quality comparison, price sorting, and voice assistance
        - Mapped user flows and stakeholder relationships to uncover design opportunities
        - Simplified navigation and UI for better accessibility
        
        ### Results
        - Defined senior user needs and design priorities
        - Delivered actionable features and design assets for implementation
        - Enhanced app accessibility and relevance for older users
        
        ### Key Learnings
        - Empathy-driven research is critical for inclusive design
        - Simplicity and clarity are key for senior usability
        - Competitor and ecosystem analysis reveals deeper insights
        """)   


# RESUME PAGE
elif st.session_state.page == "Resume":
    st.markdown('<h1 class="main-header">Resume</h1>', unsafe_allow_html=True)
    
    # Create two columns for resume and download section
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown('<h2 class="sub-header">Education</h2>', unsafe_allow_html=True)
        

        st.markdown("### University of Washington")
        st.markdown("**Master of Science in Technology Innovation** | Sep 2024 - Mar 2026")
        st.markdown("""
        Core Courses: Tech Foundation, Intro to Sensors and Circuits, Fabrication and Physical Prototyping, Design Thinking Studio
        """)
        
        st.markdown("### School of Visual Arts")
        st.markdown("**Bachelor of Fine Arts in Interaction Design** | Sep 2019 - May 2023")
        st.markdown("""
        - GPA: 3.86/4.0
        - Core Courses: UXUI Design, User Research Methods, Visual Computing, Graphic/Animation Design, Ecology and Economics
        - Honors & Awards: UW MSTI Scholarship, Young Ones Student Awards, SVA Honors Program, SVA Portfolio Top Percentile
        """)
        
        # Experience
        st.markdown('<h2 class="sub-header">Professional Experience</h2>', unsafe_allow_html=True)
        
        st.markdown("### VIPSHOP")
        st.markdown("**UIUX Intern at Internet Finance Business Department** | Oct 2023 – Apr 2024")
        st.markdown("""
        - Involved in the end-to-end B2C design process; collaborated closely with product managers, developers, and customer team
        - Improved user conversion rates and enhanced user engagement for VIPS' financial services account by designing an attractive, functional banner
        - Executed A/B testing with actual customers; notably increased the click-through rate from 2.4% to 5.1% and follower engagement from 21% to 43%
        - Participated in the customer service team's meetings to understand users' pain points and needs in real-world cases
        """)
        
        st.markdown("### Capgemini Consulting Group")
        st.markdown("**UIUX Intern** | Jul 2023 - Sep 2023")
        st.markdown("""
        - Participated in the competitive bidding project of Audi Premium Experience; collaborated with business analysts to conduct comprehensive user research
        - Developed nine business personas with different user goals; initiated an ideal user journey map from the test drive phase and extending through post-purchase services
        - Redesigned Schlumberger's internal oil system, enhanced user flow, simplified workflows, and revamped the UI by recreating all icons in Illustration
        - Successfully created a more intuitive user experience
        """)
        
        st.markdown("### RayInsight Venture")
        st.markdown("**Product Designer** | Jun 2023 - Sep 2023")
        st.markdown("""
        - Communicated with the client to determine the desired visual style for their brand
        - Produced multiple design solution sets, including logos, websites, and visual identity manuals
        - Led the development of an information architecture derived from interviews with over ten stakeholders
        - Created low-fidelity wireframes for three rounds of usability testing
        - Developed the website from scratch within a 1-month time frame
        """)
        
        st.markdown("### Hangar Design Group")
        st.markdown("**Product Design Intern** | May 2021 - Aug 2021")
        st.markdown("""
        - Conducted in-depth brand research, analyzed the potential business value of different visual design approaches
        - Utilized Illustrator and Adobe XD to redesign the UI of ALTER's Tmall store
        - Presented multiple visual and interactive solutions
        - Improved the interaction between the platform and users, particularly emphasized the fashion sector
        - Increased click-through rates by elevating visual impact
        """)
        
        # Skills
        st.markdown('<h2 class="sub-header">Skills</h2>', unsafe_allow_html=True)
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown("### Technical Skills")
            st.markdown("""
            - Figma
            - Python
            - Fusion360
            - Adobe Photoshop / Illustrator / InDesign / After Effects
            - Cinema 4D
            - Final Cut Pro
            """)
        
        with col_b:
            st.markdown("### Design Skills")
            st.markdown("""
            - User Research
            - UXUI Design
            - Web Development (Html, CSS)
            - Hardware & Software Prototyping
            - Information Architecture
            - Wireframing
            - 3D Modeling
            - Interaction / Graphic / Animation Design
            - Product Thinking
            """)

    with col2:
        # Download Resume Section
        st.markdown("### Download Resume")
        st.download_button(
            label="Download PDF Resume",
            data=b"Resume content would be here",
            file_name="Yishuai_Zheng_Resume.pdf",
            mime="application/pdf"
        )
        
        # Contact Information
        st.markdown("### Contact Information")
        st.markdown("""
        **Email:**  
        yishuaiz@uw.edu  
        yishuai.11@outlook.com
        
        **Phone:**  
        +1 425-765-8796
        
        **Website:**  
        www.yishuaizheng.com
        """)

# CONTACT PAGE
elif st.session_state.page == "Contact":
    st.markdown('<h1 class="main-header">Contact Me</h1>', unsafe_allow_html=True)
    
    # Create two columns for form and contact info
    col1, col2 = st.columns([3, 2])
    
    with col1:
        # Contact form
        st.markdown("### Get in Touch")
        st.markdown("""
        I'd love to hear from you! Whether you have a project in mind, job opportunity, 
        or just want to connect, feel free to reach out using the form below.
        """)
        
        contact_name = st.text_input("Name")
        contact_email = st.text_input("Email")
        contact_subject = st.text_input("Subject")
        contact_message = st.text_area("Message", height=150)
        
        if st.button("Send Message", type="primary"):
            if contact_name and contact_email and contact_message:
                st.success("Thank you! Your message has been sent.")
            else:
                st.error("Please fill in all required fields.")
    
    with col2:
        # Contact Information
        st.markdown("### Contact Information")
        st.markdown("""
        **Email:**  
        yishuaiz@uw.edu  
        yishuai.11@outlook.com
        
        **Phone:**  
        +1 425-765-8796
        
        **Location:**  
        University of Washington  
        Seattle, WA 98195
        
        **Website:**  
        www.yishuaizheng.com
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Social Media
        st.markdown("### Connect on Social Media")
        
        social_col1, social_col2 = st.columns(2)
        
        with social_col1:
            st.markdown("""
            [LinkedIn](https://www.linkedin.com/in/yishuai-zheng-067892201/)  
            [GitHub](https://github.com/Yishuai1108)
            """)
        
        with social_col2:
            st.markdown("""
            [Behance](https://www.behance.net/)  
            [Dribbble](https://dribbble.com/)
            """)
        
    
    # Availability Section
    st.markdown('<h2 class="section-header">My Availability</h2>', unsafe_allow_html=True)
    st.markdown("""
    I'm currently open to:
    - Full-time product design opportunities
    - Freelance UX/UI design projects
    - Consulting on user research and experience design
    - Speaking engagements related to design and technology
    
    My typical response time is within 24-48 hours.
    """)

# Footer for all pages
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #757575; font-size: 0.8rem;">
        © 2025 Yishuai Zheng. All Rights Reserved.
    </div>
    """, 
    unsafe_allow_html=True
)
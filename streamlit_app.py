import streamlit as st
import base64
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="AI Developer Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for animations and styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        animation: gradientShift 15s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
        50% { background: linear-gradient(135deg, #764ba2 0%, #667eea 100%); }
        100% { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
    }
    
    .hero-section {
        text-align: center;
        padding: 60px 20px;
        animation: fadeInDown 1s ease-out;
    }
    
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        color: white;
        margin-bottom: 10px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .hero-subtitle {
        font-size: 1.8rem;
        color: #f0f0f0;
        margin-bottom: 15px;
        font-weight: 300;
    }
    
    .hero-description {
        font-size: 1.2rem;
        color: #e0e0e0;
        max-width: 700px;
        margin: 0 auto;
        line-height: 1.6;
    }
    
    .section-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        animation: fadeInUp 0.8s ease-out;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .section-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.3);
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .project-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        color: white;
        transition: transform 0.3s ease;
        cursor: pointer;
    }
    
    .project-card:hover {
        transform: scale(1.03);
    }
    
    .project-title {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 10px;
    }
    
    .project-description {
        font-size: 1rem;
        line-height: 1.6;
        opacity: 0.95;
    }
    
    .skill-badge {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 10px 20px;
        border-radius: 25px;
        margin: 8px;
        font-weight: 500;
        animation: popIn 0.5s ease-out;
    }
    
    @keyframes popIn {
        0% {
            transform: scale(0);
        }
        50% {
            transform: scale(1.1);
        }
        100% {
            transform: scale(1);
        }
    }
    
    .contact-btn {
        background: white;
        color: #667eea;
        padding: 15px 40px;
        border-radius: 30px;
        font-size: 1.1rem;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        margin: 10px;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .contact-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    }
    
    .timeline-item {
        border-left: 3px solid #667eea;
        padding-left: 20px;
        margin: 20px 0;
        animation: slideInLeft 0.8s ease-out;
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    h1, h2, h3 {
        color: #333;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 12px 30px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <div class="hero-title">AI/ML Developer & Innovator</div>
    <div class="hero-subtitle">Transforming Ideas into Intelligent Solutions</div>
    <div class="hero-description">
        Passionate about building cutting-edge AI applications that solve real-world problems. 
        Specializing in GenAI, LLMs, and intelligent automation.
    </div>
</div>
""", unsafe_allow_html=True)

# Navigation
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("🏠 About", use_container_width=True):
        st.session_state.section = "about"
with col2:
    if st.button("💼 Projects", use_container_width=True):
        st.session_state.section = "projects"
with col3:
    if st.button("🎓 Education", use_container_width=True):
        st.session_state.section = "education"
with col4:
    if st.button("🛠️ Skills", use_container_width=True):
        st.session_state.section = "skills"
with col5:
    if st.button("📧 Contact", use_container_width=True):
        st.session_state.section = "contact"

if 'section' not in st.session_state:
    st.session_state.section = "about"

# About Section
if st.session_state.section == "about":
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("## 👨‍💻 About Me")
    st.markdown("""
    I'm an AI/ML Developer currently working as a **Project Associate (AI/ML)** at Boot & Boost Entrepreneur LLP. 
    With a strong foundation in Computer Applications from Banaras Hindu University, I specialize in building 
    innovative AI-powered solutions using state-of-the-art technologies.
    
    My expertise lies in:
    - 🤖 **Generative AI & Large Language Models (LLMs)**
    - 🔄 **AI-Powered Automation & Workflow Solutions**
    - 📊 **Business Intelligence & Report Generation**
    - 💬 **Conversational AI & Chatbot Development**
    - 🎯 **Hackathon Participation & Innovation**
    
    I'm passionate about leveraging AI to create practical solutions that drive business value and improve user experiences.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Work Experience
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("## 💼 Work Experience")
    st.markdown("""
    <div class="timeline-item">
        <h3>🚀 Project Associate (AI/ML)</h3>
        <h4>Boot & Boost Entrepreneur LLP</h4>
        <p><strong>Present</strong></p>
        <p>
        Developing cutting-edge AI solutions for business automation and intelligence. 
        Working with modern LLM frameworks and APIs to create innovative applications 
        that solve real-world problems for entrepreneurs and startups.
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Projects Section
elif st.session_state.section == "projects":
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("## 🚀 Featured Projects")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Project 1
    st.markdown("""
    <div class="project-card">
        <div class="project-title">🎯 Business Idea Generation & Validation Report Generator</div>
        <div class="project-description">
            A comprehensive Streamlit application powered by Groq API and LLaMA 3.3 model that helps entrepreneurs 
            and startups generate professional business validation reports. Features include:
            <br><br>
            ✅ AI-powered business analysis and insights<br>
            ✅ Professional PDF report generation with ReportLab<br>
            ✅ Interactive form-based data collection<br>
            ✅ Market validation and feasibility assessment<br>
            ✅ Deployed on Streamlit Cloud for easy access
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 4])
    with col1:
        st.link_button("🔗 View Project", "https://github.com/shiv4321/Idea_validation", use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Project 2
    st.markdown("""
    <div class="project-card">
        <div class="project-title">📊 AI-Powered PPT Generator</div>
        <div class="project-description">
            An intelligent presentation generation tool leveraging Groq API and LLaMA 3.3 model 
            to automatically create professional PowerPoint presentations. Key features:
            <br><br>
            ✅ Automated slide content generation<br>
            ✅ Smart formatting and layout optimization<br>
            ✅ Topic-based presentation creation<br>
            ✅ Export to multiple formats<br>
            ✅ Fast generation using advanced LLM technology
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Project 3
    st.markdown("""
    <div class="project-card">
        <div class="project-title">🏥 Physiotherapy Chatbot</div>
        <div class="project-description">
            A specialized conversational AI chatbot designed to provide physiotherapy guidance 
            and support to patients. Features include:
            <br><br>
            ✅ Natural language understanding for medical queries<br>
            ✅ Exercise recommendations and guidance<br>
            ✅ Symptom assessment and preliminary advice<br>
            ✅ 24/7 availability for patient support<br>
            ✅ Context-aware conversations with memory
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Additional Projects
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 🎨 Other AI Projects")
    st.markdown("""
    - 🤖 **Custom Chatbot Solutions** - Domain-specific conversational agents
    - 📈 **Data Analysis Tools** - AI-powered insights and visualization
    - 🔍 **Text Processing Applications** - NLP-based text analysis and generation
    - 🎯 **Automation Scripts** - Intelligent workflow automation
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Education Section
elif st.session_state.section == "education":
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("## 🎓 Education")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="timeline-item">
            <h3>🎓 Master of Computer Applications (M.C.A)</h3>
            <h4>Banaras Hindu University</h4>
            <p><strong>2022 - 2024</strong></p>
            <p>Advanced studies in Computer Applications with focus on AI/ML, software development, 
            and modern computing technologies.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="timeline-item">
            <h3>🎓 BSc. (Hons.) Computer Science</h3>
            <h4>Banaras Hindu University</h4>
            <p><strong>2019 - 2022</strong></p>
            <p>Strong foundation in computer science fundamentals, programming, 
            algorithms, and data structures.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Achievements
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("## 🏆 Achievements & Participation")
    st.markdown("""
    ### 🚀 Google Agentic AI Hackathon
    Participated in Google's prestigious Agentic AI hackathon, competing with talented developers 
    to build innovative AI solutions. Gained hands-on experience with cutting-edge AI technologies 
    and collaborative problem-solving.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Skills Section
elif st.session_state.section == "skills":
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("## 🛠️ Technical Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### AI/ML Technologies")
        skills_ai = ["LLaMA 3.3", "Groq API", "OpenAI GPT", "LangChain", 
                     "Generative AI", "NLP", "Machine Learning", "Deep Learning"]
        for skill in skills_ai:
            st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("### Programming Languages")
        skills_prog = ["Python", "JavaScript", "SQL", "HTML/CSS"]
        for skill in skills_prog:
            st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("### Frameworks & Tools")
        skills_frameworks = ["Streamlit", "FastAPI", "TensorFlow", "PyTorch", 
                            "ReportLab", "Pandas", "NumPy", "Scikit-learn"]
        for skill in skills_frameworks:
            st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("### Cloud & Deployment")
        skills_cloud = ["Streamlit Cloud", "Git", "GitHub", "Docker", "REST APIs"]
        for skill in skills_cloud:
            st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Contact Section
elif st.session_state.section == "contact":
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("## 📧 Get In Touch")
    
    st.markdown("""
    I'm always open to discussing new projects, creative ideas, or opportunities to be part of your vision.
    Feel free to reach out!
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 📧 Email
        Drop me an email and I'll get back to you as soon as possible.
        """)
        
    with col2:
        st.markdown("""
        ### 💼 LinkedIn
        Connect with me on LinkedIn to stay updated with my professional journey.
        """)
        
    with col3:
        st.markdown("""
        ### 🐱 GitHub
        Check out my repositories and contributions on GitHub.
        """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Contact Form
    st.markdown("### 💌 Send a Message")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message", height=150)
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            st.success("✅ Thank you for your message! I'll get back to you soon.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: white; padding: 20px;">
    <p style="font-size: 1.1rem;">🚀 Built with Streamlit | © 2024 AI Developer Portfolio</p>
    <p style="font-size: 0.9rem; opacity: 0.8;">Crafted with passion for innovation and excellence</p>
</div>
""", unsafe_allow_html=True)

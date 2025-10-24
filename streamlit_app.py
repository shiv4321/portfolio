import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="AI Developer Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS with interactive mouse effects and animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        background: #000000;
        position: relative;
        overflow-x: hidden;
    }
    
    #particles-canvas {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 0;
        pointer-events: none;
    }
    
    .content-wrapper {
        position: relative;
        z-index: 1;
    }
    
    .hero-section {
        text-align: center;
        padding: 80px 20px;
        animation: fadeInDown 1.2s ease-out;
        position: relative;
    }
    
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-50px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .hero-title {
        font-size: 4rem;
        font-weight: 700;
        background: linear-gradient(45deg, #ffffff, #a0a0a0, #ffffff);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 15px;
        animation: gradientFlow 3s ease infinite, textGlow 2s ease-in-out infinite;
        text-shadow: 0 0 30px rgba(255,255,255,0.3);
    }
    
    @keyframes gradientFlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes textGlow {
        0%, 100% { filter: brightness(1) drop-shadow(0 0 10px rgba(255,255,255,0.5)); }
        50% { filter: brightness(1.3) drop-shadow(0 0 20px rgba(255,255,255,0.8)); }
    }
    
    .hero-subtitle {
        font-size: 2rem;
        color: #e0e0e0;
        margin-bottom: 20px;
        font-weight: 300;
        animation: fadeIn 1.5s ease-out 0.3s both;
    }
    
    .hero-description {
        font-size: 1.3rem;
        color: #b0b0b0;
        max-width: 800px;
        margin: 0 auto;
        line-height: 1.8;
        animation: fadeIn 1.8s ease-out 0.6s both;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    .section-card {
        background: linear-gradient(135deg, rgba(30,30,30,0.95) 0%, rgba(20,20,20,0.98) 100%);
        border-radius: 25px;
        padding: 40px;
        margin: 30px 0;
        box-shadow: 0 15px 50px rgba(255,255,255,0.1);
        animation: slideInUp 0.8s ease-out;
        transition: all 0.4s ease;
        border: 1px solid rgba(255,255,255,0.1);
        position: relative;
        overflow: hidden;
    }
    
    .section-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        opacity: 0;
        transition: opacity 0.5s ease;
    }
    
    .section-card:hover::before {
        opacity: 1;
        animation: rotateGlow 3s linear infinite;
    }
    
    @keyframes rotateGlow {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .section-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 60px rgba(255,255,255,0.2);
        border-color: rgba(255,255,255,0.3);
    }
    
    @keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(50px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .project-card {
        background: linear-gradient(135deg, rgba(50,50,50,0.9) 0%, rgba(30,30,30,0.95) 100%);
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        color: white;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
        border: 1px solid rgba(255,255,255,0.15);
        position: relative;
        overflow: hidden;
    }
    
    .project-card::after {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(255,255,255,0.2) 0%, transparent 70%);
        transform: translate(-50%, -50%);
        transition: width 0.6s ease, height 0.6s ease;
    }
    
    .project-card:hover::after {
        width: 500px;
        height: 500px;
    }
    
    .project-card:hover {
        transform: scale(1.05) translateZ(0);
        box-shadow: 0 20px 50px rgba(255,255,255,0.25);
        border-color: rgba(255,255,255,0.4);
    }
    
    .project-title {
        font-size: 1.6rem;
        font-weight: 600;
        margin-bottom: 15px;
        position: relative;
        z-index: 1;
    }
    
    .project-description {
        font-size: 1.05rem;
        line-height: 1.8;
        opacity: 0.9;
        position: relative;
        z-index: 1;
    }
    
    .skill-badge {
        display: inline-block;
        background: linear-gradient(135deg, rgba(80,80,80,0.8) 0%, rgba(50,50,50,0.9) 100%);
        color: white;
        padding: 12px 24px;
        border-radius: 30px;
        margin: 10px;
        font-weight: 500;
        animation: popIn 0.6s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        transition: all 0.3s ease;
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .skill-badge:hover {
        background: linear-gradient(135deg, rgba(120,120,120,0.9) 0%, rgba(80,80,80,0.95) 100%);
        transform: translateY(-5px) scale(1.1);
        box-shadow: 0 10px 25px rgba(255,255,255,0.3);
        border-color: rgba(255,255,255,0.5);
    }
    
    @keyframes popIn {
        0% {
            transform: scale(0) rotate(-180deg);
            opacity: 0;
        }
        50% {
            transform: scale(1.2) rotate(10deg);
        }
        100% {
            transform: scale(1) rotate(0deg);
            opacity: 1;
        }
    }
    
    .timeline-item {
        border-left: 3px solid rgba(255,255,255,0.5);
        padding-left: 25px;
        margin: 25px 0;
        animation: slideInLeft 0.8s ease-out;
        position: relative;
        transition: all 0.3s ease;
    }
    
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -8px;
        top: 0;
        width: 13px;
        height: 13px;
        border-radius: 50%;
        background: white;
        box-shadow: 0 0 15px rgba(255,255,255,0.8);
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); box-shadow: 0 0 15px rgba(255,255,255,0.8); }
        50% { transform: scale(1.3); box-shadow: 0 0 25px rgba(255,255,255,1); }
    }
    
    .timeline-item:hover {
        border-left-color: white;
        padding-left: 30px;
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    h1, h2, h3, h4 {
        color: #ffffff;
    }
    
    p, li {
        color: #d0d0d0;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, rgba(80,80,80,0.9) 0%, rgba(50,50,50,0.95) 100%);
        color: white;
        border: 2px solid rgba(255,255,255,0.3);
        border-radius: 30px;
        padding: 14px 32px;
        font-weight: 600;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        font-size: 1.05rem;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 10px 30px rgba(255,255,255,0.4);
        background: linear-gradient(135deg, rgba(120,120,120,0.95) 0%, rgba(80,80,80,1) 100%);
        border-color: rgba(255,255,255,0.6);
    }
    
    .stButton>button:active {
        transform: translateY(-1px) scale(1.02);
    }
    
    /* Link Button Styling */
    .stLink>a {
        background: linear-gradient(135deg, rgba(80,80,80,0.9) 0%, rgba(50,50,50,0.95) 100%);
        color: white !important;
        border: 2px solid rgba(255,255,255,0.3);
        border-radius: 30px;
        padding: 14px 32px;
        font-weight: 600;
        transition: all 0.4s ease;
        text-decoration: none;
        display: inline-block;
    }
    
    .stLink>a:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(255,255,255,0.4);
        background: linear-gradient(135deg, rgba(120,120,120,0.95) 0%, rgba(80,80,80,1) 100%);
        border-color: rgba(255,255,255,0.6);
    }
    
    /* Form Styling */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background: rgba(30,30,30,0.8);
        border: 2px solid rgba(255,255,255,0.2);
        color: white;
        border-radius: 15px;
        transition: all 0.3s ease;
    }
    
    .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
        border-color: rgba(255,255,255,0.5);
        box-shadow: 0 0 20px rgba(255,255,255,0.2);
    }
    
    /* Floating particles effect */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
    
    .floating {
        animation: float 3s ease-in-out infinite;
    }
</style>
""", unsafe_allow_html=True)

# Interactive Mouse Effect with Particles
components.html("""
<canvas id="particles-canvas"></canvas>
<script>
    const canvas = document.getElementById('particles-canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    
    const particles = [];
    const particleCount = 100;
    
    class Particle {
        constructor(x, y) {
            this.x = x || Math.random() * canvas.width;
            this.y = y || Math.random() * canvas.height;
            this.size = Math.random() * 3 + 1;
            this.speedX = Math.random() * 2 - 1;
            this.speedY = Math.random() * 2 - 1;
            this.opacity = Math.random() * 0.5 + 0.3;
        }
        
        update() {
            this.x += this.speedX;
            this.y += this.speedY;
            
            if (this.x > canvas.width || this.x < 0) this.speedX *= -1;
            if (this.y > canvas.height || this.y < 0) this.speedY *= -1;
        }
        
        draw() {
            ctx.fillStyle = `rgba(255, 255, 255, ${this.opacity})`;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
        }
    }
    
    for (let i = 0; i < particleCount; i++) {
        particles.push(new Particle());
    }
    
    let mouse = { x: null, y: null, radius: 150 };
    
    window.addEventListener('mousemove', (e) => {
        mouse.x = e.clientX;
        mouse.y = e.clientY;
        
        for (let i = 0; i < 3; i++) {
            particles.push(new Particle(mouse.x, mouse.y));
        }
    });
    
    function connectParticles() {
        for (let i = 0; i < particles.length; i++) {
            for (let j = i + 1; j < particles.length; j++) {
                const dx = particles[i].x - particles[j].x;
                const dy = particles[i].y - particles[j].y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                
                if (distance < 120) {
                    ctx.strokeStyle = `rgba(255, 255, 255, ${0.2 * (1 - distance / 120)})`;
                    ctx.lineWidth = 1;
                    ctx.beginPath();
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(particles[j].x, particles[j].y);
                    ctx.stroke();
                }
            }
            
            if (mouse.x !== null && mouse.y !== null) {
                const dx = particles[i].x - mouse.x;
                const dy = particles[i].y - mouse.y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                
                if (distance < mouse.radius) {
                    ctx.strokeStyle = `rgba(255, 255, 255, ${0.5 * (1 - distance / mouse.radius)})`;
                    ctx.lineWidth = 2;
                    ctx.beginPath();
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(mouse.x, mouse.y);
                    ctx.stroke();
                    
                    const forceX = dx / distance;
                    const forceY = dy / distance;
                    const force = (mouse.radius - distance) / mouse.radius;
                    particles[i].x += forceX * force * 3;
                    particles[i].y += forceY * force * 3;
                }
            }
        }
    }
    
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        for (let i = 0; i < particles.length; i++) {
            particles[i].update();
            particles[i].draw();
        }
        
        connectParticles();
        
        if (particles.length > particleCount) {
            particles.splice(0, particles.length - particleCount);
        }
        
        requestAnimationFrame(animate);
    }
    
    animate();
    
    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
</script>
""", height=0)

# Hero Section
st.markdown("""
<div class="content-wrapper">
    <div class="hero-section">
        <div class="hero-title">AI/ML Developer & Innovator</div>
        <div class="hero-subtitle">Transforming Ideas into Intelligent Solutions</div>
        <div class="hero-description">
            Passionate about building cutting-edge AI applications that solve real-world problems. 
            Specializing in GenAI, LLMs, and intelligent automation.
        </div>
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
    
    # Project 3 - Physiotherapy Chatbot
    st.markdown("""
    <div class="project-card">
        <div class="project-title">🏥 PhysioFlex - AI Physiotherapy Chatbot</div>
        <div class="project-description">
            A specialized conversational AI chatbot designed to provide physiotherapy guidance 
            and support to patients. This intelligent assistant offers personalized exercise recommendations 
            and health advice. Features include:
            <br><br>
            ✅ Natural language understanding for medical queries<br>
            ✅ Personalized exercise recommendations and guidance<br>
            ✅ Symptom assessment and preliminary advice<br>
            ✅ 24/7 availability for patient support<br>
            ✅ Context-aware conversations with memory<br>
            ✅ Deployed on Hugging Face Spaces
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 4])
    with col1:
        st.link_button("🔗 Try PhysioFlex", "https://shiv22419-physio-flex.hf.space/", use_container_width=True)
    
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
        skills_cloud = ["Streamlit Cloud", "Hugging Face", "Git", "GitHub", "Docker", "REST APIs"]
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
<div style="text-align: center; color: white; padding: 30px;">
    <p style="font-size: 1.1rem;">🚀 Built with Streamlit | © 2024 AI Developer Portfolio</p>
    <p style="font-size: 0.9rem; opacity: 0.8;">Crafted with passion for innovation and excellence</p>
</div>
""", unsafe_allow_html=True)

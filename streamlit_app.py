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
    
    /* Force black background */
    .stApp {
        background-color: #000000 !important;
    }
    
    .main {
        background-color: #000000 !important;
    }
    
    .block-container {
        background-color: #000000 !important;
    }
    
    section[data-testid="stSidebar"] {
        background-color: #000000 !important;
    }
    
    #particles-canvas {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 0;
        pointer-events: none;
        background-color: #000000;
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
        background: linear-gradient(45deg, #ffffff, #c0c0c0, #ffffff);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 15px;
        animation: gradientFlow 3s ease infinite;
        filter: drop-shadow(0 0 20px rgba(255,255,255,0.4));
    }
    
    @keyframes gradientFlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
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
        background: rgba(20, 20, 20, 0.95);
        border-radius: 25px;
        padding: 40px;
        margin: 30px 0;
        box-shadow: 0 15px 50px rgba(255,255,255,0.05);
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
        background: radial-gradient(circle, rgba(255,255,255,0.08) 0%, transparent 70%);
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
        box-shadow: 0 20px 60px rgba(255,255,255,0.15);
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
        background: rgba(30, 30, 30, 0.9);
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
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        transform: translate(-50%, -50%);
        transition: width 0.6s ease, height 0.6s ease;
    }
    
    .project-card:hover::after {
        width: 500px;
        height: 500px;
    }
    
    .project-card:hover {
        transform: scale(1.05) translateZ(0);
        box-shadow: 0 20px 50px rgba(255,255,255,0.2);
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
        background: rgba(40, 40, 40, 0.9);
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
        background: rgba(80, 80, 80, 0.95);
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
        border-left: 3px solid rgba(255,255,255,0.4);
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
        color: #ffffff !important;
    }
    
    p, li {
        color: #d0d0d0 !important;
    }
    
    .stButton>button {
        background: rgba(40, 40, 40, 0.95) !important;
        color: white !important;
        border: 2px solid rgba(255,255,255,0.3) !important;
        border-radius: 30px !important;
        padding: 14px 32px !important;
        font-weight: 600 !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        font-size: 1.05rem !important;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px) scale(1.05) !important;
        box-shadow: 0 10px 30px rgba(255,255,255,0.4) !important;
        background: rgba(80, 80, 80, 0.95) !important;
        border-color: rgba(255,255,255,0.6) !important;
    }
    
    .stButton>button:active {
        transform: translateY(-1px) scale(1.02) !important;
    }
    
    /* Form Styling */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background: rgba(30,30,30,0.9) !important;
        border: 2px solid rgba(255,255,255,0.2) !important;
        color: white !important;
        border-radius: 15px !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
        border-color: rgba(255,255,255,0.5) !important;
        box-shadow: 0 0 20px rgba(255,255,255,0.2) !important;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
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
    
    // Make sure canvas has black background
    canvas.style.backgroundColor = '#000000';
    
    const particles = [];
    const mouse = { x: null, y: null, radius: 200 };
    let mouseParticles = [];
    
    class Particle {
        constructor(x, y, fromMouse = false) {
            this.x = x || Math.random() * canvas.width;
            this.y = y || Math.random() * canvas.height;
            this.size = fromMouse ? Math.random() * 2 + 1 : Math.random() * 1.5 + 0.5;
            this.speedX = (Math.random() - 0.5) * 0.5;
            this.speedY = (Math.random() - 0.5) * 0.5;
            this.opacity = fromMouse ? 1 : Math.random() * 0.3 + 0.1;
            this.fromMouse = fromMouse;
            this.life = fromMouse ? 100 : Infinity;
            this.maxLife = 100;
        }
        
        update() {
            this.x += this.speedX;
            this.y += this.speedY;
            
            if (this.fromMouse) {
                this.life--;
                this.opacity = this.life / this.maxLife;
            }
            
            if (this.x > canvas.width) this.x = 0;
            if (this.x < 0) this.x = canvas.width;
            if (this.y > canvas.height) this.y = 0;
            if (this.y < 0) this.y = canvas.height;
        }
        
        draw() {
            ctx.fillStyle = `rgba(255, 255, 255, ${this.opacity})`;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
            
            // Add glow effect
            ctx.shadowBlur = 10;
            ctx.shadowColor = `rgba(255, 255, 255, ${this.opacity})`;
        }
    }
    
    // Initialize background particles
    for (let i = 0; i < 50; i++) {
        particles.push(new Particle());
    }
    
    // Mouse move event - create white trail
    window.addEventListener('mousemove', (e) => {
        mouse.x = e.clientX;
        mouse.y = e.clientY;
        
        // Create multiple particles at mouse position
        for (let i = 0; i < 5; i++) {
            mouseParticles.push(new Particle(
                mouse.x + (Math.random() - 0.5) * 20, 
                mouse.y + (Math.random() - 0.5) * 20, 
                true
            ));
        }
    });
    
    function connectParticles() {
        // Connect mouse trail particles
        for (let i = 0; i < mouseParticles.length; i++) {
            for (let j = i + 1; j < mouseParticles.length; j++) {
                const dx = mouseParticles[i].x - mouseParticles[j].x;
                const dy = mouseParticles[i].y - mouseParticles[j].y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                
                if (distance < 100) {
                    ctx.strokeStyle = `rgba(255, 255, 255, ${0.6 * (1 - distance / 100)})`;
                    ctx.lineWidth = 2;
                    ctx.beginPath();
                    ctx.moveTo(mouseParticles[i].x, mouseParticles[i].y);
                    ctx.lineTo(mouseParticles[j].x, mouseParticles[j].y);
                    ctx.stroke();
                }
            }
        }
        
        // Draw circle around mouse
        if (mouse.x !== null && mouse.y !== null) {
            ctx.beginPath();
            ctx.arc(mouse.x, mouse.y, 30, 0, Math.PI * 2);
            ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
            ctx.lineWidth = 2;
            ctx.stroke();
            
            ctx.beginPath();
            ctx.arc(mouse.x, mouse.y, 50, 0, Math.PI * 2);
            ctx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
            ctx.lineWidth = 1;
            ctx.stroke();
        }
    }
    
    function animate() {
        // Clear with black background
        ctx.fillStyle = '#000000';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        // Reset shadow
        ctx.shadowBlur = 0;
        
        // Update and draw background particles
        for (let i = 0; i < particles.length; i++) {
            particles[i].update();
            particles[i].draw();
        }
        
        // Update and draw mouse particles
        for (let i = mouseParticles.length - 1; i >= 0; i--) {
            mouseParticles[i].update();
            mouseParticles[i].draw();
            
            if (mouseParticles[i].life <= 0) {
                mouseParticles.splice(i, 1);
            }
        }
        
        connectParticles();
        
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
    Hello! I'm an AI/ML Developer currently working as a **Project Associate (AI/ML)** at **Boot & Boost Entrepreneur LLP**. 
    
    With a Master's degree in Computer Applications from the prestigious **Banaras Hindu University**, I bring a solid 
    academic foundation combined with hands-on experience in cutting-edge AI technologies.
    
    ### What I Do
    
    I specialize in building intelligent, practical AI solutions that transform business processes and create real value. 
    My work focuses on leveraging the latest advancements in artificial intelligence to solve complex problems in innovative ways.
    
    ### My Expertise
    
    - 🤖 **Generative AI & LLMs**: Harnessing the power of models like LLaMA 3.3, GPT, and Groq API to create intelligent applications
    - 🔄 **AI Automation**: Building smart workflows that streamline business operations and increase efficiency
    - 📊 **Business Intelligence**: Developing AI-powered tools for data analysis, report generation, and decision support
    - 💬 **Conversational AI**: Creating sophisticated chatbots and virtual assistants for various domains
    - 🚀 **Rapid Prototyping**: Turning ideas into working applications quickly using modern frameworks like Streamlit
    
    ### My Approach
    
    I believe in creating AI solutions that are:
    - **Practical**: Focused on solving real-world problems
    - **User-Centric**: Designed with the end-user experience in mind
    - **Scalable**: Built to grow with business needs
    - **Innovative**: Leveraging cutting-edge technologies while maintaining reliability
    
    ### Beyond Work
    
    When I'm not coding, you'll find me:
    - 🏆 Participating in hackathons (like Google's Agentic AI Hackathon)
    - 📚 Learning about the latest AI research and technologies
    - 🌐 Contributing to open-source projects
    - 🎯 Exploring new ways to apply AI in solving everyday challenges
    
    I'm passionate about the intersection of AI and practical problem-solving, and I'm always excited to take on new 
    challenges that push the boundaries of what's possible with machine learning and artificial intelligence.
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
        Leading the development of innovative AI solutions for business automation and intelligence. 
        Working extensively with modern LLM frameworks (LLaMA 3.3, Groq API) and Python ecosystem 
        to create practical applications that solve real-world problems for entrepreneurs and startups.
        </p>
        <p><strong>Key Responsibilities:</strong></p>
        <ul>
            <li>Designing and implementing AI-powered business tools and automation systems</li>
            <li>Developing conversational AI solutions for various industry domains</li>
            <li>Building and deploying scalable applications using Streamlit and cloud platforms</li>
            <li>Collaborating with stakeholders to identify AI opportunities and deliver value</li>
            <li>Staying current with latest AI/ML technologies and best practices</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Projects Section
elif st.session_state.section == "projects":
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("## 🚀 Featured Projects")
    st.markdown("*Hover over each project card to see the interactive effects!*")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Project 1
    st.markdown("""
    <div class="project-card">
        <div class="project-title">🎯 Business Idea Generation & Validation Report Generator</div>
        <div class="project-description">
            A comprehensive Streamlit application powered by Groq API and LLaMA 3.3 model that helps entrepreneurs 
            and startups generate professional business validation reports. This tool streamlines the ideation and 
            validation process, making it accessible to anyone with a business idea.
            <br><br>
            <strong>Key Features:</strong><br>
            ✅ AI-powered business analysis and market insights<br>
            ✅ Professional PDF report generation with ReportLab<br>
            ✅ Interactive form-based data collection<br>
            ✅ Comprehensive market validation and feasibility assessment<br>
            ✅ Deployed on Streamlit Cloud for easy accessibility<br>
            ✅ Fast generation using state-of-the-art LLaMA 3.3 model
            <br><br>
            <strong>Technologies:</strong> Python, Streamlit, Groq API, LLaMA 3.3, ReportLab, Streamlit Cloud
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
            An intelligent presentation generation tool that leverages Groq API and LLaMA 3.3 model 
            to automatically create professional PowerPoint presentations from simple topic inputs. 
            Perfect for professionals, students, and educators who need quick, quality presentations.
            <br><br>
            <strong>Key Features:</strong><br>
            ✅ Automated slide content generation with AI<br>
            ✅ Smart formatting and professional layout optimization<br>
            ✅ Topic-based presentation creation<br>
            ✅ Export to multiple formats (PPTX, PDF)<br>
            ✅ Fast generation using advanced LLM technology<br>
            ✅ Customizable themes and styles
            <br><br>
            <strong>Technologies:</strong> Python, Groq API, LLaMA 3.3, python-pptx, AI Content Generation
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
            and support to patients. PhysioFlex offers personalized exercise recommendations, 
            answers health-related queries, and provides 24/7 support to users seeking physiotherapy advice.
            <br><br>
            <strong>Key Features:</strong><br>
            ✅ Natural language understanding for medical and physiotherapy queries<br>
            ✅ Personalized exercise recommendations based on user symptoms<br>
            ✅ Symptom assessment and preliminary advice<br>
            ✅ 24/7 availability for patient support and guidance<br>
            ✅ Context-aware conversations with memory of previous interactions<br>
            ✅ Deployed on Hugging Face Spaces for global accessibility
            <br><br>
            <strong>Technologies:</strong> Python, NLP, LLM, Hugging Face Spaces, Conversational AI
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 4])
    with col1:
        st.link_button("🔗 Try PhysioFlex", "https://shiv22419-physio-flex.hf.space/", use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Additional Projects
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 🎨 Other AI Projects & Experiments")
    st.markdown("""
    Beyond my featured projects, I've developed numerous AI applications and tools:
    
    - 🤖 **Custom Domain-Specific Chatbots** - Conversational agents tailored for specific industries and use cases
    - 📈 **Data Analysis & Visualization Tools** - AI-powered insights and interactive dashboards
    - 🔍 **Text Processing Applications** - NLP-based tools for text analysis, summarization, and generation
    - 🎯 **Workflow Automation Scripts** - Intelligent automation solutions for repetitive tasks
    - 🔬 **ML Model Experimentation** - Exploring various machine learning algorithms and techniques
    - 📝 **Content Generation Tools** - AI-powered writing assistants and content creators
    
    Each project showcases different aspects of AI/ML capabilities and explores innovative solutions 
    to real-world problems.
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
            <p>
            Advanced studies in Computer Applications with specialized focus on AI/ML, 
            software development, and modern computing technologies. Completed rigorous 
            coursework in algorithms, data structures, machine learning, deep learning, 
            and software engineering principles.
            </p>
            <p><strong>Key Areas:</strong> AI/ML, Software Engineering, Data Science, Web Technologies</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="timeline-item">
            <h3>🎓 BSc. (Hons.) Computer Science</h3>
            <h4>Banaras Hindu University</h4>
            <p><strong>2019 - 2022</strong></p>
            <p>
            Established a strong foundation in computer science fundamentals including programming, 
            algorithms, data structures, operating systems, and database management. 
            Developed problem-solving skills and logical thinking through theoretical and practical coursework.
            </p>
            <p><strong>Key Areas:</strong> Programming, Algorithms, Data Structures, Mathematics, Computer Fundamentals</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Achievements
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("## 🏆 Achievements & Participation")
    st.markdown("""
    ### 🚀 Google Agentic AI Hackathon
    
    Participated in Google's prestigious Agentic AI hackathon, competing alongside talented developers 
    from around the world to build innovative AI solutions. This experience provided invaluable exposure to:
    
    - **Cutting-edge AI Technologies**: Hands-on experience with the latest AI frameworks and tools
    - **Collaborative Problem-Solving**: Working with diverse teams to tackle complex challenges
    - **Rapid Prototyping**: Building functional AI applications under time constraints
    - **Innovation & Creativity**: Thinking outside the box to create unique solutions
    - **Networking**: Connecting with fellow AI enthusiasts and industry professionals
    
    This hackathon strengthened my skills in agentic AI systems and reinforced my passion for 
    building intelligent, autonomous solutions.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Skills Section
elif st.session_state.section == "skills":
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("## 🛠️ Technical Skills")
    st.markdown("*Hover over each skill badge to see the interactive effects!*")
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("### 🤖 AI/ML Technologies")
        skills_ai = ["LLaMA 3.3", "Groq API", "OpenAI GPT", "LangChain", 
                     "Generative AI", "NLP", "Machine Learning", "Deep Learning",
                     "TensorFlow", "PyTorch", "Hugging Face"]
        for skill in skills_ai:
            st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("### 💻 Programming Languages")
        skills_prog = ["Python", "JavaScript", "SQL", "HTML/CSS", "C++"]
        for skill in skills_prog:
            st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("### 🔧 Frameworks & Tools")
        skills_frameworks = ["Streamlit", "FastAPI", "Flask", "Django",
                            "ReportLab", "Pandas", "NumPy", "Scikit-learn",
                            "Matplotlib", "Seaborn"]
        for skill in skills_frameworks:
            st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("### ☁️ Cloud & Deployment")
        skills_cloud = ["Streamlit Cloud", "Hugging Face Spaces", "Git", "GitHub", 
                       "Docker", "REST APIs", "CI/CD"]
        for skill in skills_cloud:
            st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Additional Skills Section
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 🎯 Core Competencies")
    st.markdown("""
    - **Problem Solving**: Strong analytical and critical thinking abilities
    - **Software Development**: Full-stack development with focus on AI integration
    - **Project Management**: Agile methodologies and team collaboration
    - **Research & Development**: Staying updated with latest AI trends and innovations
    - **Communication**: Technical writing and presentation skills
    - **Rapid Learning**: Quick adaptation to new technologies and frameworks
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Contact Section
elif st.session_state.section == "contact":
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("## 📧 Get In Touch")
    
    st.markdown("""
    I'm always open to discussing new projects, creative ideas, or opportunities to be part of your vision.
    Whether you're looking for an AI/ML developer, want to collaborate on an exciting project, or just want 
    to connect and talk about AI, feel free to reach out!
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Contact Options
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("""
        ### 📧 Email
        Drop me an email and I'll get back to you as soon as possible.
        
        **Response Time**: Usually within 24 hours
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("""
        ### 💼 LinkedIn
        Connect with me on LinkedIn to stay updated with my professional journey and latest projects.
        
        **Let's Network!**
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col3:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("""
        ### 🐱 GitHub
        Check out my repositories and contributions on GitHub. Explore my code and projects!
        
        **Open Source**
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Contact Form
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 💌 Send Me a Message")
    st.markdown("Fill out the form below and I'll get back to you soon!")
    
    with st.form("contact_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Your Name *")
        with col2:
            email = st.text_input("Your Email *")
        
        subject = st.text_input("Subject *")
        message = st.text_area("Your Message *", height=150, 
                               placeholder="Tell me about your project, question, or just say hi!")
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            submitted = st.form_submit_button("✉️ Send Message", use_container_width=True)
        
        if submitted:
            if name and email and subject and message:
                st.success("✅ Thank you for your message! I'll get back to you soon.")
                st.balloons()
            else:
                st.error("❌ Please fill out all required fields.")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Additional Info
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 🌟 What I'm Looking For")
    st.markdown("""
    - **Exciting AI/ML Projects**: Challenging problems that push the boundaries of AI
    - **Collaboration Opportunities**: Working with talented teams on innovative solutions
    - **Freelance Work**: Short-term projects or consulting opportunities
    - **Open Source Contributions**: Contributing to meaningful open-source projects
    - **Learning & Growth**: Opportunities to expand my skills and knowledge
    
    Let's build something amazing together! 🚀
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: white; padding: 30px; position: relative; z-index: 1;">
    <p style="font-size: 1.1rem; margin-bottom: 10px;">🚀 Built with Streamlit & Passion for AI</p>
    <p style="font-size: 0.9rem; opacity: 0.7;">© 2024 AI Developer Portfolio | Crafted with innovation and excellence</p>
    <p style="font-size: 0.85rem; opacity: 0.6; margin-top: 10px;">Move your mouse to see the magic ✨</p>
</div>
""", unsafe_allow_html=True)

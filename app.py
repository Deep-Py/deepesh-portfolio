import streamlit as st
import requests
import plotly.express as px

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Deepesh Pawar | Portfolio",
    page_icon="🚀",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg,#1f1c2c,#928dab);
    color:white;
}
.card {
    background: rgba(255,255,255,0.1);
    padding:20px;
    border-radius:15px;
    margin-bottom:15px;
    backdrop-filter: blur(10px);
}
.hero {
    text-align:center;
    padding:40px;
    border-radius:20px;
    background: linear-gradient(135deg,#00c6ff,#0072ff);
}
</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown("""
<div class="hero">
<h1>🚀 Deepesh Pawar</h1>
<h3>Database Engineer → Data Scientist</h3>
<p>Python | SQL | Data Automation | 10+ Years Experience</p>
</div>
""", unsafe_allow_html=True)

# ---------------- METRICS ----------------
c1, c2, c3 = st.columns(3)
c1.metric("Experience", "10+ Years")
c2.metric("Data Quality ↑", "95%")
c3.metric("Efficiency ↑", "20%")

# ---------------- TABS ----------------
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "👤 About",
    "📊 Skills",
    "💼 Experience",
    "📁 Projects",
    "💻 GitHub",
    "🤖 Assistant"
])

# ---------------- ABOUT ----------------
with tab1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("""
    Data Engineer with 10+ years of experience in automation, analytics, and data systems.

    ✅ Expert in Python, SQL, Data Pipelines  
    ✅ Improved data quality by 95%  
    ✅ Strong stakeholder communication  

    🎯 Goal: Transition into Data Science roles
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("📍 Navi Mumbai | 📞 +91 8879535097")
    st.write("✉️ deepesh.pawar151192@gmail.com")
    st.write("🔗 http://www.linkedin.com/in/deepesh-pawar/")

# ---------------- SKILLS ----------------
with tab2:
    st.header("📊 Skills Dashboard")

    data = {
        "Skill": ["Python","SQL","Pandas","ETL","Visualization"],
        "Level": [90,92,88,85,80]
    }

    fig = px.bar(data, x="Skill", y="Level", color="Skill")
    st.plotly_chart(fig, use_container_width=True)

# ---------------- EXPERIENCE (TIMELINE) ----------------
with tab3:
    st.header("💼 Experience Timeline")

    with st.expander("🚀 Database Engineer II – Here Technologies (2022–Present)", expanded=True):
        st.write("""
        - Improved data quality by **95%**
        - Reduced manual effort by **20%**
        - Prevented major data loss using SQL
        - Worked with stakeholders across teams
        """)

    with st.expander("📊 Database Engineer I – Here Technologies (2019–2022)"):
        st.write("""
        - Conducted data quality checks before releases
        - Achieved **100% clean data ingestion**
        - Managed JIRA pipelines
        """)

    with st.expander("🧭 Spatial Data Specialist – Here Technologies (2015–2019)"):
        st.write("""
        - SME for 5+ projects
        - Resolved 30+ issues
        - Managed 15+ team members
        """)

# ---------------- PROJECTS ----------------
with tab4:
    st.header("📁 Projects")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🛒 Walmart Customer Profiling")
        st.image("assets/walmart.png", use_column_width=True)
        st.write("""
        - Customer segmentation model  
        - Marketing recommendations  
        - Python, Pandas, NumPy  
        """)

    with col2:
        st.subheader("🎬 Netflix Engagement")
        st.image("assets/netflix.png", use_column_width=True)
        st.write("""
        - Improved recommendation system  
        - Increased engagement by **15%**  
        - SQL + Python  
        """)

# ---------------- GITHUB ----------------
with tab5:
    st.header("💻 GitHub Projects")

    username = "your-github-username"  # ✅ CHANGE THIS

    try:
        url = f"https://api.github.com/users/{username}/repos"
        response = requests.get(url)

        if response.status_code == 200:
            repos = response.json()

            for repo in repos[:6]:
                st.markdown(f"""
                <div class="card">
                    <h4>{repo['name']}</h4>
                    <p>{repo['description'] if repo['description'] else "No description"}</p>
                    <a href="{repo['html_url']}" target="_blank">🔗 View Repo</a>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("Could not fetch repos")

    except:
        st.error("GitHub connection error")

# ---------------- SIMPLE AI ASSISTANT ----------------
with tab6:
    st.header("🤖 Ask Me")

    q = st.text_input("Ask recruiter-style questions")

    if q:
        q = q.lower()

        if "experience" in q:
            st.success("✅ 10+ years in Data Engineering & Analytics")

        elif "skills" in q:
            st.success("✅ Python, SQL, ETL, Data Analysis, Visualization")

        elif "projects" in q:
            st.success("✅ Walmart Profiling & Netflix Engagement projects")

        elif "strength" in q:
            st.success("✅ Strong data quality + automation mindset")

        else:
            st.info("✅ Experienced Data Engineer transitioning to Data Science")

# ---------------- RESUME DOWNLOAD ----------------
st.markdown("---")

with open("resume.pdf", "rb") as f:
    st.download_button(
        label="📥 Download Resume",
        data=f,
        file_name="Deepesh_Pawar_Resume.pdf",
        mime="application/pdf"
    )

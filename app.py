import streamlit as st
import requests
import plotly.express as px

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Deepesh Pawar | AI Portfolio",
    page_icon="🚀",
    layout="wide"
)

# ---------------- THEME ----------------
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
tabs = st.tabs(["👤 About", "📊 Analytics", "💼 Experience", "💻 GitHub", "🤖 AI Assistant", "📜 Resume"])

# ---------------- ABOUT ----------------
with tabs[0]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("""
    Data Engineer with 10+ years of experience in automation, analytics, and large-scale data systems.

    🔹 Expert in SQL, Python & Data Pipelines  
    🔹 Proven 95% improvement in data accuracy  
    🔹 Strong stakeholder communication  

    Goal: Transition into Data Science and Machine Learning roles.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- ANALYTICS DASHBOARD ----------------
with tabs[1]:
    st.header("📊 Skills Analytics")

    data = {
        "Skill": ["Python","SQL","Pandas","ETL","Visualization"],
        "Level": [90,92,88,85,80]
    }

    fig = px.bar(data, x="Skill", y="Level", color="Skill")
    st.plotly_chart(fig, use_container_width=True)

# ---------------- EXPERIENCE ----------------
with tabs[2]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Here Technologies")
    st.write("""
    **Database Engineer II (2022–Present)**  
    - Improved data quality by 95%  
    - Reduced manual effort by 20%  

    **Database Engineer I (2019–2022)**  
    - 100% clean data ingestion  
    - Managed pipelines and UAT
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- GITHUB INTEGRATION ----------------
with tabs[3]:
    st.header("💻 GitHub Projects")

    username = "Deep-Py"  # CHANGE THIS

    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        repos = response.json()
        for repo in repos[:6]:
            st.markdown(f"""
            <div class="card">
            <h4>{repo['name']}</h4>
            <p>{repo['description']}</p>
            <a href="{repo['html_url']}" target="_blank">View Project</a>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("Unable to fetch GitHub repos")

# ---------------- AI CHATBOT ----------------
with tabs[4]:
    st.header("🤖 Ask About Me")

    user_q = st.text_input("Ask recruiter-style questions:")

    if user_q:
        if "experience" in user_q.lower():
            st.write("✅ 10+ years in Data Engineering & Analytics.")

        elif "skills" in user_q.lower():
            st.write("✅ Python, SQL, ETL, Data Analysis, Visualization.")

        elif "projects" in user_q.lower():
            st.write("✅ Walmart Profiling & Netflix Engagement project.")

        elif "strength" in user_q.lower():
            st.write("✅ Strong data quality focus + automation expertise.")

        else:
            st.write("✅ Experienced Data Engineer transitioning into Data Science.")

# ---------------- RESUME DOWNLOAD ----------------
with tabs[5]:
    st.header("📜 Download Resume")

    with open("resume.pdf", "rb") as f:
        st.download_button(
            label="Download PDF Resume",
            data=f,
            file_name="Deepesh_Pawar_Resume.pdf",
            mime="application/pdf"
        )

# ---------------- FOOTER ----------------

st.markdown("---")
st.markdown("© Deepesh Pawar")


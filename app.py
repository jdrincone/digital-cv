from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Juan David Rincón"
PAGE_ICON = ":wave:"
NAME = "Juan David Rincón"
DESCRIPTION = """
Data Scientist with solid analytical thinking and problem-solving skills developed though 2+ 
of experience in the industrie and 3+ of academic research in
scientific computation and theoretical physics.
"""
EMAIL = "jdrincone@gmail.com"
CEL = "(+57) 300 364-8095"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/jdrincone/",
    "GitHub": "https://jdrincone.github.com",
    "Pag web": "https://jdrincone.github.io/Portafolio/",
}
PROJECTS = {
    "🏆 Analísis de mercados inmoviliarios": "https://jdrincone.github.io/Portafolio/post/proyect-8/",
    "🏆 2020 Kaggle Machine Learning & Data Science Survey": "https://jdrincone.github.io/Portafolio/post/proyect-4/",
    "🏆 Instabilities in an Optical Black-Hole Laser": "https://onlinelibrary.wiley.com/doi/abs/10.1002/andp.202000239",
    "🏆 Influence of the densification process on the structural, microstructural, and dielectric properties of PLMN-PT:0.5Er ceramics": "https://link.springer.com/article/10.1007/s10832-021-00257-4",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write("📚", CEL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️  Experience deploying and mantaining data extraction, transformation,
      and loading (ETL) processes. Currently working with advanced Python 
      and PySpark to create and automate data flows within a company extracting 
      information from diverse sources, including SQL databases and AWS S3.
- ✔️ Experience in proficiency in data cleaning techniques, ensuring the delivery
     of high-quality data.
- ✔️ Strong background in developing and managing business intelligence
     solutions for organizations. This involves the creation and implementation 
     of predictive and forecasting models with techniques of machine learning, 
     statistics and numerical modeling in Python
- ✔️ Experience in software and product development and engineering design, e,g, backend deployment
     (data pipelines, APIs), CI/CD best practices.
- ✔️ As an individual, I am highly responsible and thrive in leadership roles, 
     motivated by continuous improvement and possess a natural ability to learn quickly.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Numpy, TensorFlow, Statmodels, Scypy), SQL, Git, Julia.
- 📊 Data Visulization: PowerBi, MS Excel, Plotly, Matplotlib.
- 📚 Modeling: Logistic regression, linear regression, decition trees, Natural Gradient 
     Boosting (NGBoost), support vector machine (SVM),clustering, PCA.
- 🗄️ Databases: Postgres, MongoDB, MySQL.
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Analyst |  Quipux**")
st.write("03/2021 - Present")
st.write(
    """
- ► Data cleaning process manager.
- ► Developing and managing business intelligence solutions for the organization.
- ► Automation and optimization of processes and code using OOP in Python.
- ► Providing reports through office applications to improve business processes.
- ► Time series analysis.
- ► Data mining.
- ► Analytics project management.
- ► Design unit python tests.
- ► Generation of predictive behavior models.
"""
)


st.write("🚧", "**Researcher in training |  CINVESTAV**")
st.write("08/2017 - 26/2019")
st.write(
    """
- ► Scientific computing.
- ► Hawking radiation analogue.
- ► Mathematical Physics.
"""
)
# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- Títulos academicos ---
st.write('\n')
st.subheader("Academic Title")
st.write("---")
st.write(
    """
- ► Msc Física, Centro de Investigación y de Estudios Avanzados del
    Polictécnico Nacional (CINVESTAV), México.
- ► Física, Universidad de Antioquia, Sede Medellín.

- 📚 Curso en Métodos computacionales en estadística, Escuela de Ingenieros, Sede Medellín.
- 📚 Diplomado en Artificial Intelligence and deep learning, Universidad Nacional de Colombia, Medellín.
- 📚 Certificación Data Science Junior, Acámica, Academia Argentina, Curso intermedio-avanzado. Certificado avalado por IBM y Globant.
- 📚 Diplomado en Data Science and Machine Learning, Universidad Nacional de Colombia, Sede Bogotá.
"""
)


# Main python file
import streamlit as st

st.set_page_config(layout="wide")

col1, col2, col3 = st.columns([1, 5.5, 2])

with col1:
    st.image("images/Frank Affatigato.png", width=250)

with col2:
    st.title("Frank Affatigato")
    content = """
    Senior Data Analyst with 7+ years of experience and a Master's degree in Information Systems. 
    I specialize in data engineering, building scalable pipelines to streamline and optimize data workflows. 
    My work focuses on creating actionable insights through data science initiatives and dynamic visualizations. 
    Proficient in Python and Databricks, I transform raw data into clear, impactful intelligence that supports strategic decision-making. 
    Passionate about using technology to solve complex challenges, I constantly seek ways to innovate and improve data solutions.
    """

    st.info(content)

st.write("Below you can find some of the apps I have built in Python. Feel free to contact me!")

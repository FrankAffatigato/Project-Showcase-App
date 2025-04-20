# Main python file
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2, empty_col1 = st.columns([1.5, 4.5, 2])

with col1:
    st.title("")
    st.image("images/Frank Affatigato.png", width=350)

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

df = pd.read_csv("data.csv", sep=";")

col3, empty_col2, col4 = st.columns([2, 0.5, 2])

# Create first column for projects
with col3:
    for index, row in df[0:10].iterrows():
        st.header(row["title"])
        st.image(f"images/{row['image']}", width=550)
        st.write(row["description"])
        st.write(f"[Source Code]({row['url']})")

# Create second column for projects
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.image(f"images/{row['image']}", width=550)
        st.write(row["description"])
        st.write(f"[Source Code]({row['url']})")
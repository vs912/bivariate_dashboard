import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("cleaned_data.csv")

# Streamlit config
st.set_page_config(page_title="Bivariate Dashboard", layout="centered")
st.title("📊 Mental Health Survey – Bivariate Analysis")

# Dropdown variables
category_vars = [
    'anonymity', 'remote_work', 'tech_company', 'wellness_program', 'care_options',
    'mental_health_interview', 'phys_health_interview', 'coworkers', 'supervisor',
    'mental_vs_physical', 'obs_consequence', 'leave'
]
grouping_vars = ['treatment', 'Gender', 'family_history']

# Custom labels for titles
title_map = {
    'anonymity': "Is mental health support anonymous?",
    'remote_work': "Do you work remotely?",
    'tech_company': "Do you work in a tech company?",
    'wellness_program': "Does your company offer a wellness program?",
    'care_options': "Are mental health care options provided?",
    'mental_health_interview': "Would you disclose mental health issues in an interview?",
    'phys_health_interview': "Would you disclose physical health issues in an interview?",
    'coworkers': "Comfort discussing mental health with coworkers?",
    'supervisor': "Comfort discussing mental health with supervisor?",
    'mental_vs_physical': "Is mental health as important as physical health?",
    'obs_consequence': "Observed consequences for disclosing mental health?",
    'leave': "Comfort taking mental health leave?"
}

# Dropdown selectors
x_col = st.selectbox("Select a category (X-axis):", category_vars)
group_col = st.selectbox("Group by:", grouping_vars)

# Generate chart
if x_col and group_col:
    temp = df[[x_col, group_col]].dropna()

    fig = px.histogram(
        temp,
        x=x_col,
        color=group_col,
        barmode='group',
        text_auto=True,
        color_discrete_sequence=px.colors.qualitative.Set2,
        title=f"{title_map.get(x_col, x_col)} grouped by {group_col}"
    )

    fig.update_layout(
        xaxis_title=x_col,
        yaxis_title="Count",
        title_x=0.5,
        font=dict(size=14),
        plot_bgcolor='white',
        paper_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

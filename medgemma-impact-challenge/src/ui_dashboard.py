# 1. Install Streamlit and a tool to tunnel it so you can see it
!pip install -q streamlit pyngrok

# 2. Create the Dashboard Script
with open('app.py', 'w') as f:
    f.write("""
import streamlit as st
import json
import pandas as pd

st.set_page_config(page_title="MedChron Live", page_icon="🧠")

st.title("MedChron: Mental Health Dashboard")
st.subheader("Passive Behavioral Phenotyping via MedGemma 1.5")

# --- Sidebar: User Info ---
st.sidebar.header("User Profile")
st.sidebar.text("ID: nihal_student_unf")
st.sidebar.progress(75, text="Cognitive Load: High")

# --- Main Metrics ---
col1, col2, col3 = st.columns(3)
col1.metric("Sleep Fragmentation", "High", "+20%")
col2.metric("App Switching", "14/min", "Critical")
col3.metric("Brain Rest", "4.2 hrs", "-1.5 hrs")

# --- The AI Live Report ---
st.header("Live Mental Health Narrative")
# In a real app, this text comes from your MedGemma output
st.info(\"\"\"
**AI Observation:** Based on 24-hour device logs, you are showing signs of 
circadian rhythm disruption. Your phone activity between 01:00 and 03:00 
correlated with high laptop CPU usage suggests a 'burnout' state. 
**Recommendation:** Schedule a 20-minute 'Digital Reset' and aim for a 
consistent device-off time tonight.
\"\"\")

# --- Activity Visualization ---
st.header("Digital Activity Trends")
# Simulating some data
chart_data = pd.DataFrame({
    'Hour': list(range(24)),
    'Stress Level': [10, 5, 5, 2, 2, 5, 10, 20, 40, 60, 80, 75, 70, 65, 85, 90, 95, 80, 60, 50, 65, 80, 90, 95]
})
st.line_chart(chart_data.set_index('Hour'))

st.success("Data is being processed locally on Edge AI to ensure total privacy.")
""")

print("app.py created. You are ready to build the UI!")

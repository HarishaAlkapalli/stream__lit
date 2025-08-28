import streamlit as st
import pandas as pd

# Load data once
@st.cache_data
def load_data():
    # Change this to your actual file path
    df = pd.read_csv("final_allocation_with_pref5.csv")
    return df

st.set_page_config(page_title="Student Result Checker", layout="centered")
st.title("🎓 Student Result Checker")

# Load file
df = load_data()

# Input box
student_id = st.text_input("Enter your Unique ID (Roll Number):")

if student_id:
    # Search in dataframe
    result = df[df["UniqueID"].astype(str) == student_id]
    if not result.empty:
        st.success("✅ Result Found!")
        st.write(result)   # shows the row
        # You can also show in a nicer format
        st.metric("UniqueID", result.iloc[0]["UniqueID"])
        st.metric("CollegeID", result.iloc[0]["CollegeID"])
        st.metric("PrefNumber", result.iloc[0]["PrefNumber"])
    else:
        st.error("❌ No record found for this Unique ID")


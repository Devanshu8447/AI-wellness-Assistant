import streamlit as st
from utils.gad7_scoring import run_gad7
from utils.emotion_parser import run_emotion_chat


def run_mental_health_agent():
    st.subheader("🧠 Mental Health Support")

    mh_option = st.radio(
        "Choose a service", ["Calculate Anxiety Level (GAD-7)", "Emotion-Based Chatbot"]
    )

    if mh_option == "Calculate Anxiety Level (GAD-7)":
        run_gad7()
    else:
        run_emotion_chat()

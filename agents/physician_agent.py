import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os
from dotenv import load_dotenv


load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",  
    task="conversational",
)
model = ChatHuggingFace(llm=llm)


def run_physician_agent():
    st.subheader("🩺 General Physician AI")
    questions = [
        "What symptoms are you experiencing?",
        "How long have you had these symptoms?",
        "Do you have any chronic conditions?",
        "Are you taking any medication?",
        "On a scale of 1 to 10, how severe is it?",
    ]
    responses = []

    with st.form("physician_form"):
        for i, q in enumerate(questions):
            responses.append(st.text_input(q, key=f"q{i}"))
        submitted = st.form_submit_button("Generate Prescription")

    if submitted:
        # Combine all responses into a prompt
        prompt = "\n".join([f"{questions[i]} {responses[i]}" for i in range(5)])
        prompt = (
            """
You are a qualified general physician. Based on the patient's answers to the following 5 health-related questions, analyze the information and generate a short and informative prescription.

The prescription should include:
- Probable diagnosis
- Suggested medications or treatments
- Rest or dietary recommendations
- Optional advice on whether to visit a clinic

Use simple language that a non-medical person can understand.
Respond as a general physician.  
Do not explain your thinking. Just give the response you would say to the user.
"""
            + prompt
        )

        # Get response from LLM
        result = model.invoke(prompt)
        st.success("Prescription:")
        st.write(result.content)

import streamlit as st

# from langchain.llms import HuggingFaceHub
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os
from dotenv import load_dotenv

# Load environment
load_dotenv()

# Global model
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task="conversational",
    ##model_kwargs={"temperature": 0.7, "max_new_tokens": 512}
)
model = ChatHuggingFace(llm=llm)


def run_emotion_chat():
    st.subheader("🗣️ Emotion-Based Chatbot")
    feeling = st.text_area("Tell me how you're feeling today...")

    if st.button("Get Emotional Support"):
        prompt = f"""You are a caring AI mental wellness companion.
        Respond as a mental health assistant. Be kind and empathetic. 
Do not explain your thinking. Just give the response you would say to the user.
The user is feeling: "{feeling}"
Respond empathetically and suggest 2–3 general tips or exercises to help them cope.
"""
        result = model.invoke(prompt)
        st.success("Here’s what I suggest:")
        st.write(result.content)

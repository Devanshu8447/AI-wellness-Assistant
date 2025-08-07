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


def run_diet_planner_agent():
    st.subheader("🥗 Personalized Diet Planner")

    with st.form("diet_form"):
        age = st.number_input("Age", 5, 100)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        height = st.number_input("Height (cm)")
        weight = st.number_input("Weight (kg)")
        activity = st.selectbox(
            "Activity Level",
            ["Sedentary", "Light", "Moderate", "Active", "Very Active"],
        )
        calories = st.number_input("Current Daily Calorie Intake", 1000, 5000)
        submitted = st.form_submit_button("Generate Diet Plan")

    if submitted:
        prompt = f"""You are a certified dietician. Generate a one-day meal plan based on:
- Age: {age}
- Gender: {gender}
- Height: {height} cm
- Weight: {weight} kg
- Activity Level: {activity}
- Current Daily Calorie Intake: {calories} kcal
Plan should include breakfast, lunch, dinner, and 2 snacks, with portion sizes and total calories.
Respond as a dietitian. 
Do not explain your thinking. Just give the response you would say to the user.
"""

        result = model.invoke(prompt)
        st.success("Here’s your personalized diet plan:")
        st.write(result.content)

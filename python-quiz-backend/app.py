import os
import streamlit as st
import json

st.title("Quiz Backend – Admin Preview")

# Correct: path joined safely
questions_path = os.path.join("static", "questions.json")
if os.path.exists(python-quiz-backend/static/questions.json):
    with open(questions_path, "r", encoding="utf-8") as f:
        st.header("Questions")
        st.json(json.load(f))
else:
    st.error("questions.json not found!")

rewards_path = os.path.join("static", "rewards.json")
if os.path.exists(rewards_path):
    with open(rewards_path, "r", encoding="utf-8") as f:
        st.header("Rewards")
        st.json(json.load(f))
else:
    st.error("rewards.json not found!")

st.info("Tip: Update the JSON files on GitHub to change the quiz. The frontend will fetch automatically.")

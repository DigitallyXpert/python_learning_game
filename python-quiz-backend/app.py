import streamlit as st
import json

st.title("Quiz Backend – Admin Preview")

st.header("Questions")
with open("static/questions.json", "r", encoding="utf-8") as f:
    st.json(json.load(f))

st.header("Rewards")
with open("static/rewards.json", "r", encoding="utf-8") as f:
    st.json(json.load(f))

st.info("Tip: Update the JSON files on GitHub to change the quiz. The frontend will fetch automatically.")

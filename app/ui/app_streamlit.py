import streamlit as st
import requests
from app.core.rag_engine import ask_ai

st.title("🤖 Enterprise Data Assistant")

question = st.text_input("Ask about revenue, regions, or trends:")

if question:
    with st.spinner("Analyzing database..."):
        # Connect to your FastAPI backend
        response = requests.get(f"http://127.0.0.1:8000/ask?question={question}")
        answer = response.json().get("answer")
        st.success(f"Result: {answer}")

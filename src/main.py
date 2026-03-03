import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from fastapi import FastAPI
from local_rag_w_openai import ask_ai

app = FastAPI()

@app.get("/ask")
def handle_query(question: str):
    data = ask_ai(question)
    return {"status": "success", "answer": data}
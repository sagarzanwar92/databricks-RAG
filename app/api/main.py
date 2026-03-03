import uvicorn
from fastapi import FastAPI, Query
from app.core.rag_engine import ask_ai

app = FastAPI(
    title="Sales Data RAG API",
    description="A professional GenAI Backend for querying Sales Databases via SQL-RAG.",
    version="1.0.0"
)

@app.get("/ask")
def handle_query(question: str = Query(..., description="The natural language question for the Sales RAG")):
    """
    Endpoint to ask questions about the Sales database.
    Example: /ask?question=What is the total revenue?
    """
    try:
        # Calls the centralized RAG logic from core/rag_engine.py
        data = ask_ai(question)
        return {
            "status": "success",
            "question": question,
            "answer": data
        }
    except Exception as e:
        return {
            "status": "error",
            "detail": str(e)
        }

if __name__ == "__main__":
    # Start the server on port 8000
    # Note: Use "app.api.main:app" so uvicorn can find the path correctly for reloading
    uvicorn.run("app.api.main:app", host="127.0.0.1", port=8000, reload=True)
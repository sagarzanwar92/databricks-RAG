import uvicorn
from fastapi import FastAPI, Query
from with_openai import ask_ai  # Direct import works now!

app = FastAPI(title="Sales Data RAG API")

@app.get("/ask")
def handle_query(question: str = Query(..., description="The question for the Sales RAG")):
    """
    Endpoint to ask questions about the Sales database.
    Example: /ask?question=What is the total revenue?
    """
    try:
        # Call your existing logic from with_openai.py
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
    uvicorn.run(app, host="127.0.0.1", port=8000)
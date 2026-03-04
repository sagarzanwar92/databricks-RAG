import uvicorn
from fastapi import FastAPI, Query
from app.core.rag_engine import ask_ai

# for better management of frequent requests - Avoid spamming
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded


limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app = FastAPI(
    title="Sales Data RAG API",
    description="A professional GenAI Backend for querying Sales Databases via SQL-RAG.",
    version="1.0.0"
)

@limiter.limit("5/minute")
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
    
    #uvicorn.run("app.api.main:app", host="127.0.0.1", port=8000, reload=True)  -- --> This host has been changed to make 0.0 in order to communicate with docker
    uvicorn.run("app.api.main:app", host="0.0.0.0", port=8000, reload=True)
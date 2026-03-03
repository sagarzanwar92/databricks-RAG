@echo off
title Data-RAG Control Center

:: 1. Start the FastAPI Backend
echo Starting FastAPI Backend on Port 8000...
start "Backend (FastAPI)" cmd /k "call C:\Users\DELL\python_envs\ai_master\Scripts\activate && python -m app.api.main"

:: 2. Start the Streamlit Frontend
echo Starting Streamlit Dashboard on Port 8501...
start "Frontend (Streamlit)" cmd /k "call C:\Users\DELL\python_envs\ai_master\Scripts\activate && python -m streamlit run app/ui/app_streamlit.py"

:: 3. Start the Chainlit Chatbot
echo Starting Chainlit Chat on Port 8001...
start "Frontend (Chainlit)" cmd /k "call C:\Users\DELL\python_envs\ai_master\Scripts\activate && chainlit run app/ui/app_chainlit.py --port 8001"

echo.
echo All systems are launching! 
echo Backend: http://127.0.0.1:8000/docs
echo Streamlit: http://localhost:8501
echo Chainlit: http://localhost:8001
pause
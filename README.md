# Enterprise Sales RAG System 📊🤖

A professional Generative AI implementation for querying corporate sales databases using natural language. Built with a modular "Microservices" architecture.

## 🏗️ Architecture
- **Core Logic**: GPT-4o-mini + DuckDB (SQL Generation & Execution)
- **Backend**: FastAPI (RESTful API)
- **Frontends**: 
  - **Streamlit**: Data-centric dashboard view.
  - **Chainlit**: Conversational, ChatGPT-like interface.

## 📂 Project Structure
```text
DATABRICKS-RAG/
├── app/
│   ├── api/          # FastAPI Backend
│   ├── core/         # RAG Logic (SQL Generator)
│   └── ui/           # Frontends (Streamlit & Chainlit)
├── data/             # Local DuckDB Storage
├── scripts/          # Utility scripts (datamaker.py)
└── run_all.bat       # One-click launch script

```

## 🚀 Getting Started

**1. Setup Environment**
Ensure you have your virtual environment activated and API keys set:

**Create .env file in root**
```text 
OPENAI_API_KEY=sk-your-key-here 
```


**2. Initialize Database**
If you haven't created the mock data yet, run:

Bash 
```text
python datamaker.py 
```


**3. Launch the System**
Simply double-click run_all.bat or run:
(Check that you have correct address updated for where files are kept)

Bash
```text
./run_all.bat
```

🛠️ Tech Stack
LLM: OpenAI GPT-4o-mini

Database: DuckDB

Frameworks: 
Backend: FastAPI 
Frontend: Streamlit, Chainlit


**4. Your Frontend should something like this:**

## 🖥️ Frontend Comparison

| Streamlit Dashboard | Chainlit Chatbot |
| :---: | :---: |
| <img src="./assets/streamlit_ui.png" width="400"> | <img src="./assets/chainlit_ui.png" width="400"> |


## 🖥️ Frontend Comparison

| Streamlit Dashboard | Chainlit Chatbot |
| :---: | :---: |
| ![Streamlit](./assets/streamlit_ui.png) | ![Chainlit](./assets/chainlit_ui.png) |
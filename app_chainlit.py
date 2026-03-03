import chainlit as cl
import requests

# The URL where your FastAPI backend is running
API_URL = "http://127.0.0.1:8000/ask"

@cl.on_chat_start
async def start():
    await cl.Message(content="👋 Connected to Sales RAG Backend. How can I help you with the data today?").send()

@cl.on_message
async def main(message: cl.Message):
    # 1. Create a placeholder message for the 'loading' state
    msg = cl.Message(content="")
    
    # 2. Call your FastAPI backend
    try:
        # We use a 'Step' to show the API call in the UI
        async with cl.Step(name="Querying Backend") as step:
            response = requests.get(f"{API_URL}?question={message.content}")
            data = response.json()
            step.output = f"Status: {data.get('status')}"

        if data.get("status") == "success":
            answer = data.get("answer")
            msg.content = f"📊 **Database Result:** \n\n {answer}"
        else:
            msg.content = f"❌ Error from API: {data.get('detail')}"
            
    except Exception as e:
        msg.content = f"⚠️ Connection Error: Is your FastAPI running? \n\n `{e}`"

    await msg.send()


# use chainlit run app_chainlit.py --port 8001 -w to run chainlit to different port as it is bound check for 8000 port by default which is ideally used by backend right now. 
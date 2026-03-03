import chainlit as cl
from .local_rag_w_openai import ask_ai

@cl.on_message
async def main(message: cl.Message):
    # 1. Show the user that we are 'thinking'
    msg = cl.Message(content="")
    
    # 2. Call your existing logic
    # We use cl.make_async because our DuckDB/OpenAI call is synchronous
    result = await cl.make_async(ask_ai)(message.content)
    
    # 3. Send the answer back
    msg.content = f"📊 **Database Result:** {result}"
    await msg.send()
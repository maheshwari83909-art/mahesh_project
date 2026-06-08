from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time

app = FastAPI()

# Allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

# Simple "AI simulation"
def generate_reply(message: str):
    reply = f"Hey! I got your message: {message}. I am here to help you 👍"
    
    # simulate streaming (word by word)
    for word in reply.split():
        yield word + " "
        time.sleep(0.1)

@app.post("/chat")
def chat(req: ChatRequest):
    return {
        "response": " ".join(req.message.split()[:10]) + " 👍 (short reply mode)"
    }
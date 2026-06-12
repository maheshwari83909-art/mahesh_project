from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from ai_chat import get_ai_response
from mongodb import conversations

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "WorkBuddy AI Backend Running"}


@app.post("/chat")
def chat(req: ChatRequest):

    try:
        print("User Message:", req.message)

        ai_reply = get_ai_response(req.message)

        print("AI Reply:", ai_reply)

        conversations.insert_one({
            "employee": "Mahesh",
            "message": req.message,
            "reply": ai_reply
        })

        return {
            "reply": ai_reply
        }

    except Exception as e:
        print("ERROR:", str(e))

        return {
            "reply": f"Backend Error: {str(e)}"
        }
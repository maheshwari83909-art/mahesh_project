from pymongo import MongoClient

MONGO_URI = "mongodb+srv://maheshwari:Arun18072009@cluster0.llkxuat.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URI)

db = client["employee_retention"]

conversations = db["conversations"]


def get_recent_conversations(limit=5):
    chats = list(
        conversations.find().sort("_id", -1).limit(limit)
    )

    history = ""

    for chat in reversed(chats):
        history += f"""
Employee: {chat.get('message', '')}
AI: {chat.get('reply', '')}
"""

    return history
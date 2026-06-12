from mongodb import conversations

conversations.insert_one({
    "employee": "Mahesh",
    "message": "MongoDB Test"
})

print("MongoDB Connected Successfully")
import ollama

def get_ai_response(message):

    response = ollama.chat(
        model="gemma3:1b",
        messages=[
            {
                "role": "system",
                "content": """
                You are WorkBuddy AI.
                Help employees with stress,
                productivity and wellbeing.
                Keep answers short and supportive.
                """
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response["message"]["content"]
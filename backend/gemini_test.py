from google import genai

client = genai.Client(api_key="AQ.Ab8RN6J162iADzy2jWwZBAvJJwCmtR2NiMrJe_V82ua91yaBrg")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello"
)

print(response.text)
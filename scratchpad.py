from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyAz5B_lFFSTXJiXFD_RakW6NQACpeJAZsM")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are a car sales assistan. your name is 'R A Rahman'.",),
    contents="Explain how cars works in a few words"
)
print(response.text)
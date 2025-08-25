from google import genai
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

# USING Gemini 
try:
    def callGemini (contents):
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        response = client.models.generate_content(
        model="gemini-2.5-flash", contents=contents
    )
        return response.text
    pass
except Exception as e:
    print(e)
    pass


# Using openai through openrouter

try:
    def callOpenai(content):
        client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key= os.getenv("OPEN_ROUTER_KEY"),
        )
        completion = client.chat.completions.create(
        model="openai/gpt-4o",
        max_tokens=2000,
        messages=[
            {
            "role": "user",
            "content": content
            }
        ]
        )
        return completion.choices[0].message.content
    pass
except Exception as e:
    print(e)
    pass
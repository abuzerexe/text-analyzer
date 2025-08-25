import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import (
    GEMINI_API_KEY,
    OPEN_ROUTER_API_KEY,
    OPEN_ROUTER_BASE_URL,
    DEFAULT_GEMINI_MODEL,
    DEFAULT_OPENAI_MODEL,
    MAX_TOKENS)
from openai import OpenAI
from google import genai

# USING Gemini 
try:
    def callGemini (contents: str):
        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
        model=DEFAULT_GEMINI_MODEL, contents=contents
    )
        usage = response.usage_metadata

        res = {
            "response" : response.text,
            "model" : "Gemini",
            "token_usage" : {
                "prompt_tokens" : usage.prompt_token_count,
                "completion_tokens" : usage.candidates_token_count,
                "total_tokens" : usage.total_token_count
            }
        }
        return res
    
except Exception as e:
    print(e)
    pass


# Using openai through openrouter

try:
    def callOpenai(content):
        client = OpenAI(
        base_url=OPEN_ROUTER_BASE_URL,
        api_key= OPEN_ROUTER_API_KEY,
        )
        completion = client.chat.completions.create(
        model=DEFAULT_OPENAI_MODEL,
        max_tokens=MAX_TOKENS,
        messages=[
            {
            "role": "user",
            "content": content
            }
        ]
        )
        usage = completion.usage
        res = {
            "response" : completion.choices[0].message.content,
            "model" : "Openai",
            "token_usage" : {
                "prompt_token" : usage.prompt_tokens,
                "completion_token": usage.completion_tokens,
                "total_tokens" : usage.total_tokens
            }
        }
        return res
    
except Exception as e:
    print(e)
    pass
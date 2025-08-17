import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("gemini_api_key")
genai.configure(api_key=gemini_api_key)

for model in genai.list_models():
    print(model.name)

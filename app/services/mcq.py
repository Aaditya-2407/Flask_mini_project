import os
import google.generativeai as genai
from dotenv import load_dotenv
import json

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_mcqs(text):
    # Use gemini-2.5-flash or gemini-flash-latest as gemini-1.5-flash is not available
    model = genai.GenerativeModel('models/gemini-2.5-flash')
    
    prompt = f"""
    Generate 3 multiple choice questions based on the text. 
    Return the response as a valid JSON object with a key "questions".
    Text: {text[:2000]}
    """
    
    response = model.generate_content(
        prompt, 
        generation_config={"response_mime_type": "application/json"}
    )
    return response.text
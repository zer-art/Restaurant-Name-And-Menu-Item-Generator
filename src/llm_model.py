import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv() # Load your API keys from .env

# Get your Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env. Please set it.")

genai.configure(api_key=GEMINI_API_KEY)

# Initialize the Gemini Pro model
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_restaurant_name_api(cuisine: str, style: str) -> str:
    """Generates a restaurant name using the Gemini API."""
    prompt = f"""
    You are a creative assistant that generates restaurant names.
    Given the cuisine and a desired style, suggest a unique and appealing restaurant name.

    Cuisine: {cuisine}
    Style: {style}

    Restaurant Name:
    """
    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(max_output_tokens=50)
        )
        return response.text.strip()
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return "Error: Could not generate name."
def generate_menu_ideas_api(restaurant_name: str, cuisine: str) -> str:
    """Generates menu ideas using the Gemini API."""
    prompt = f"""
    You are a creative assistant that generates menu ideas for restaurants.
    Given the restaurant name and cuisine, suggest a list of unique and appealing menu items.

    Restaurant Name: {restaurant_name}
    Cuisine: {cuisine}

    Menu Ideas:
    """
    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(max_output_tokens=100)
        )
        return response.text.strip()
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return "Error: Could not generate menu ideas."

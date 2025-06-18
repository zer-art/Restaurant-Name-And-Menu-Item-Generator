import os
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

GEMINI_API_KEY_RAW = os.getenv("GEMINI_API_KEY")
GEMINI_API_KEY = GEMINI_API_KEY_RAW.strip() if GEMINI_API_KEY_RAW else None

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found, is empty, or contains only whitespace in .env or environment. Please set it."
    )


model_id = "gemini-1.5-flash" # Using gemini-pro model

llm = ChatGoogleGenerativeAI(
    model=model_id,
    google_api_key=GEMINI_API_KEY,
    temperature=0.7,
    max_output_tokens=100,
    top_p=0.9,
    top_k=50
)

prompt_template_name = PromptTemplate(
    input_variables=["cuisine", "style"],
    template="Suggest a unique and appealing restaurant name for a {cuisine} cuisine restaurant with a {style} style."
)
restaurant_name_chain = prompt_template_name | llm | StrOutputParser()

prompt_template_item = PromptTemplate(
    input_variables=["restaurant_name", "cuisine"],
    template="Suggest some creative menu items for a restaurant named {restaurant_name} serving {cuisine} cuisine."
)
menu_items_chain = prompt_template_item | llm | StrOutputParser()

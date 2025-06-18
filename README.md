# 🍽️ Restaurant Name & Menu Generator

This project is a web application built with Streamlit that leverages Large Language Models (LLMs) through Langchain and the Google Gemini API to generate creative restaurant names and menu ideas.

## Features

*   **Restaurant Name Generation:**
    *   Select a cuisine type (e.g., Italian, Mexican, Indian).
    *   Select a restaurant style (e.g., Modern, Rustic, Casual).
    *   Generates unique and appealing restaurant names based on your selections.
*   **Menu Idea Generation:**
    *   Uses a previously generated restaurant name or allows custom input.
    *   Select a cuisine for the menu.
    *   Generates creative menu item suggestions.
*   **User-Friendly Interface:** Simple and intuitive web interface powered by Streamlit.
*   **Powered by Gemini:** Utilizes Google's Gemini models for high-quality text generation.

## Tech Stack

*   **Python:** Core programming language.
*   **Streamlit:** For building the interactive web application.
*   **Langchain:** Framework for developing applications powered by language models.
*   **Langchain Google GenAI:** Integration for using Google's Generative AI models (Gemini).
*   **Google Generative AI SDK:** Python SDK for direct interaction with the Gemini API.
*   **Dotenv:** For managing environment variables.

## Setup and Installation

### 1. Prerequisites

*   Python 3.10 or higher
*   pip (Python package installer)

### 2. Clone the Repository

```bash
git clone <https://github.com/zer-art/Restaurant-Name-And-Menu-Item-Generator>

```

### 4. Install Dependencies

run command : 

```bash
`pip install -r requirements.txt` 
```


### 4. Set Up Environment Variables

You'll need a Google Gemini API key.

1.  Create a file named `.env` in the root directory of the project (`Restaurant Name And Munu Item Generator/.env`).
2.  Add your Gemini API key to the `.env` file:

    ```env
    GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
    ```
    Replace `"YOUR_GEMINI_API_KEY"` with your actual API key.

### 5. Prepare Data Files

Ensure you have the `data` directory with `cuisines.txt` and `styles.txt` in the root of your project.

*   `data/cuisines.txt`: A text file where each line is a cuisine type (e.g., Italian, Mexican).
*   `data/styles.txt`: A text file where each line is a restaurant style (e.g., Modern, Casual).

Example `data/cuisines.txt`:
```
Italian
Mexican
Indian
Chinese
French
```

## Usage

1.  Ensure your main system or Python virtual environment is activated and you are in the project's root directory.
2.  Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```
3.  Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).
4.  Use the interface to select cuisines and styles, then generate restaurant names and menu ideas.

## Project Structure

```
RName-gen/
├── data/
│   ├── cuisines.txt
│   └── styles.txt
├── src/
│   ├── __init__.py
│   ├── chains.py         # Langchain LCEL chains
│   ├── llm_model.py      # Direct Gemini API interaction (alternative or supplementary)
│   ├── prompt_template.py # Langchain prompt templates and LLM configuration
│   └── utils.py          # Utility functions (e.g., loading data)
├── app.py                # Main Streamlit application
├── .env                  # Environment variables (API keys) - Gitignored
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is open-source. Feel free to use and modify it. (Consider adding a specific license like MIT if desired).
```
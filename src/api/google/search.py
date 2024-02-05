import requests
from core import BafLog
from config import Config

GOOGLE_SEARCH_ENDPOINT = "https://www.googleapis.com/customsearch/v1"
api_key = Config.GOOGLE_API_KEY
search_engine_id = Config.GOOGLE_SEARCH_ENGINE_ID

logger = BafLog

class GoogleSearchAPI:

    @staticmethod
    def process(query, data):
        from llms import LLM
        from prompts import GoogleSearchPrompt

        prompt = GoogleSearchPrompt.google_search_prompt(query)
        generated_query = LLM.llm.process('Generate a query', prompt, data)
        print(f'Generated query: {generated_query}')
        
        params = {
            'q': generated_query,
            'key': api_key,
            'cx': search_engine_id
        }

        response = requests.get(GOOGLE_SEARCH_ENDPOINT, params=params)

        # Handle API response
        if response.status_code != 200:
            logger.error(f"Error fetching GoogleSearch data. API response: {response.text}")
            return "Error fetching GoogleSearch data. Please try again later."

        raw_results = response.json().get('items', [])
        clear_results = []

        # Extracting only the first two results and their essential details
        for item in raw_results[:2]:
            clear_results.append({
                "title": item.get("title", "N/A"),
                "link": item.get("link", "N/A"),
                "description": item.get("snippet", "N/A").strip()
            })

        return clear_results

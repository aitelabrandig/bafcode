from dotenv import load_dotenv
import os

load_dotenv()

class ToolsConfig:
    CMDS=True

    GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
    GOOGLE_SEARCH_ENGINE_ID=os.getenv('GOOGLE_SEARCH_ENGINE_ID')
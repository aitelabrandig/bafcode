import os
from dotenv import load_dotenv
load_dotenv()




# General configurations for all LLMs
class LLMsConfig:
    # Timeout for LLM requests (if applicable)
    LLM_TIMEOUT = 15  # in seconds

    # Default LLM to use if no LLM is specified in the request
    DEFAULT_LLM = "OpenAILLM"

    # OpenAI LLM configurations
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Should ideally be loaded from a secure environment variable or vault
    OPENAI_ENGINE = "gpt-3.5-turbo"  # Default engine for OpenAI requests
    OPENAI_MAX_TOKENS = 150  # Default maximum tokens for responses from OpenAI

    # If you have other LLMs or external services, add their configurations similarly:
    BAFCLOUD_LLM_ENDPOINT = "https://api-dev.bafcloud.com/api/v1/llms/generate"


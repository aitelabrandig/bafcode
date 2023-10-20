from .openai_llm import OpenAILLM
from .example import ExampleLLm
from config import Config


class LLM:

    if Config.DEFAULT_LLM == "OpenAILLM":
        llm = OpenAILLM()
    elif Config.DEFAULT_LLM == "SomeOtherLLM":
        # llm = SomeOtherLLM()
        pass


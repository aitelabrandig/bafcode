 
from core import BafLog
# Optionally, import any other required modules or packages

class ExamplesGetExamplePrompt:  # Replace ExamplesGetExample with the name of your prompt
    def examples_get_example_prompt(data):
        prompt = """
            Your Prompt Here
            ExamplesGetExample Data:
            {data}
        """
        return prompt.format(data=data)
        
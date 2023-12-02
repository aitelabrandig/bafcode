 
from core import BafLog
# Optionally, import any other required modules or packages

class GoogleSearchPrompt:  # Replace GoogleSearch with the name of your prompt
    def google_search_prompt(data):
        prompt = """
            User Input:
            {data}

            Given a user's request or input, generate a query that can be used to search Google. The query should be a string.

            For example:
             User Input: Search for how to make a cup of tea
             Query:"How to make a cup of tea"
             User Input: Search for Apple
             Query:"Apple"

            The Query should be like a human want to search on Google.
            Now, based on the provided input, generate a query that can be used to search Google.
            Generate a query only.

            
            Query:
        """
        return prompt.format(data=data)
        
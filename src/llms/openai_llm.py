import openai
from core import framework_logger

class OpenAILLM:
    def __init__(self):
        self.logger = framework_logger

        # Initialize OpenAI API key (should be kept secret and ideally loaded from a secure environment)
        openai.api_key = 'YOUR_OPENAI_API_KEY'

    def process(self, data):
        """
        Process the data using the OpenAI language model.

        Args:
        - data (dict): Data to be processed. For example, data might contain a 'prompt' key.

        Returns:
        - dict: Processed data containing the model's response.
        """
        prompt = data.get('prompt')
        if not prompt:
            self.logger.error("No prompt provided for OpenAI LLM.")
            raise ValueError("A prompt is required for processing.")

        try:
            # Use OpenAI's Completion API to get the model's response
            response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=150)
            return {
                'response': response.choices[0].text.strip(),
                'status': "success"
            }

        except Exception as e:
            self.logger.error(f"Error processing with OpenAI LLM: {str(e)}")
            return {
                'message': "Error processing with OpenAI LLM.",
                'status': "error"
            }

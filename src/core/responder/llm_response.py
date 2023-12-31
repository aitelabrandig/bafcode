from core import BafLog
from llms import LLM
from prompts import ResponderPrompt

class Responder:
    def __init__(self):
        self.logger = BafLog

    def generate(self,data,message):

        try:
            # Log the received data (might be useful for debugging, but ensure no sensitive data is logged)
            self.logger.info(f"Generating response for data: {data}")
            # stringify the data
            data = str(data)
            prompt = ResponderPrompt.generate_final_response(data)
            response = LLM.llm.process(message,prompt)
            return response

        except Exception as e:
            self.logger.error(f"Error generating response: {str(e)}")
            return {
                'message': "Error generating response.",
                'status': "error"
            }


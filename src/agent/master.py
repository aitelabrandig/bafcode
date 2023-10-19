from core import framework_logger
from agent.commands.processor import CommandProcessor 
from .llm_decision.decision import decide_command

class MasterAgent:
    def __init__(self):
        self.logger = framework_logger
        

    def process(self, data):

        # Log the received data (might be useful for debugging, but ensure no sensitive data is logged)
        self.logger.info(f"Received data: {data}")

        # Based on the data, decide which command to run or action to take
        command_to_run = decide_command(data['message'])

        # Process the command and get the response
        command_processor = CommandProcessor()
        response = command_processor.execute(command_to_run, data)

        return response

    


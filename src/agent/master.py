from core import framework_logger
from agent.commands.processor import CommandProcessor 
from .llm_decision.decision import decide_command

class MasterAgent:
    def __init__(self):
        self.logger = framework_logger
        

    def process(self, data):
        """
        Process the client's data and decide the appropriate action.

        Args:
        - data (dict): Data received from the client.

        Returns:
        - dict: Processed response data.
        """
        # Log the received data (might be useful for debugging, but ensure no sensitive data is logged)
        self.logger.info(f"Received data: {data}")

        # Based on the data, decide which command to run or action to take
        # This is a placeholder and should be replaced with your actual decision-making logic
        command_to_run = decide_command(data)

        # Process the command and get the response
        command_processor = CommandProcessor()
        response = command_processor.execute(command_to_run, data)

        return response

    


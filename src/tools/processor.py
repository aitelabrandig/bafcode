from core import BafLog
from tools import *

class CommandProcessor:
    def __init__(self):
        self.logger = BafLog

    def execute(self, command_name, task, data):
        # Log the command execution
        self.logger.info(f"Executing command: {command_name}")

       
        command = command_mapping.get(command_name)
      
        if not command:
            self.logger.error(f"Unknown command: {command_name}")
            return "I can't do this task because i don't have the necessary tools."

        response = command().execute(task,data)
        return response


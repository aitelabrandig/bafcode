from core import BafLog
from tools import *

class CommandProcessor:
    def __init__(self):
        self.logger = BafLog

    def execute(self, command_name, data):
        # Log the command execution
        self.logger.info(f"Executing command: {command_name}")

       
        command = command_mapping.get(command_name)
      
        if not command:
            self.logger.error(f"Unknown command: {command_name}")
            raise ValueError(f"Unknown command: {command_name}")

        response = command().execute(data)
        return response


from core import framework_logger
from ..commands import *

class CommandProcessor:
    def __init__(self):
        self.logger = framework_logger

    def execute(self, command_name, data):
        # Log the command execution
        self.logger.info(f"Executing command: {command_name}")

       
        command = command_mapping.get(command_name)
      
        if not command:
            self.logger.error(f"Unknown command: {command_name}")
            raise ValueError(f"Unknown command: {command_name}")

        response = command().execute(data)
        return response


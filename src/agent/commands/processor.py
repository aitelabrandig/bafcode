import logging
from core import framework_logger
from ..commands import *

class CommandProcessor:
    def __init__(self):
        self.logger = framework_logger

    def execute(self, command_name, data):
        """
        Execute the specified command with the provided data.

        Args:
        - command_name (str): Name of the command to execute.
        - data (dict): Data to be used by the command.

        Returns:
        - dict: Response data from the executed command.
        """
        # Log the command execution
        self.logger.info(f"Executing command: {command_name}")

        # Mapping of command names to their corresponding classes or functions
        command_mapping = {
            "getLastEmail": GetLastEmail,
            # ... Add more commands as needed
        }

        # Get the command class or function from the mapping
       
        command = command_mapping.get(command_name)
      
        if not command:
            self.logger.error(f"Unknown command: {command_name}")
            raise ValueError(f"Unknown command: {command_name}")

        # Execute the command and get the response
        # Here, I'm assuming each command class has an "execute" method that takes in data and returns a response.
        # Adjust this based on your command implementations.
        print('Executing the cmd...')
        response = command().execute(data)
        print('Executed the cmd...')
        return response




class MasterPrompts:
    def decide_command_prompt(commands):
       decide_command = """ 
        Please select a command to execute based on the provided options:

        Commands:
        {commands}

        Respond only with the command name in the format:
        'commandName'

        For example: 'getLastMessage'

           """
       return decide_command.format(commands=commands)

    
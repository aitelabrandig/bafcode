from llms import LLM
from tools import command_mapping
from prompts import MasterPrompts


import re



def decide_command(message):
    commands = list(command_mapping.keys())
    prompt = MasterPrompts.decide_command_prompt(commands)
    print('Message: ',message)
    llm_response = LLM.llm.process(message,prompt)
    command = llm_response
    print('Command: ',command)
    return command

    


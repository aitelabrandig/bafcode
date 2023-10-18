from llms.openai_llm import OpenAILLM
from ..commands import command_mapping
from prompts import MasterPrompts


import re



def decide_command(message):
    commands = list(command_mapping.keys())
    prompt = MasterPrompts.decide_command_prompt(commands)
    print('Message: ',message)
    llm_response = OpenAILLM().process(message,prompt)
    command = llm_response
    print('Command: ',command)
    return command

    


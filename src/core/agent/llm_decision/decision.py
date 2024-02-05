from llms import LLM
from tools import command_mapping
from prompts import MasterPrompts


import re



def decide_command(task,data):
    print('Task : ',task)
    commands = list(command_mapping.keys())
    prompt = MasterPrompts.decide_command_prompt(commands)
    print('Message: ',task)
    llm_response = LLM.llm.process(task,prompt,data)
    command = llm_response
    print('Command: ',command)
    return command

    


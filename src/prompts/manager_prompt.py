 
from core import BafLog

# Optionally, import any other required modules or packages

class ManagerPromptPrompt:  # Replace ManagerPrompt with the name of your prompt
    
    def manager_prompt_prompt(data):
        from tools import command_mapping
        tools_list = list(command_mapping)
        prompt = """

            Rules: 
            - You can only use the tools listed above.
            - You can use a tool multiple times.
            - Don't generate tasks that are not related to the user's request or input.
            - Don't generate duplicate tasks.
            - Don't generate Tasks that can't be completed by the tools.
            - if tools can't be used to generate tasks, return an empty array.
            - if what the user requested is not clear, return an empty array.
            - if what user request was simple and can

            
            User Input:
            {data}

            Given a user's request or input, provide a list of tasks to be executed in response to the request. Each task should be detailed, clear, and actionable. Please format your response as an array of task objects. Each task object should have the following attributes:

            - `id`: A unique identifier for the task.
            - `description`: A brief description of the task detailing what needs to be done.
            - `status`: Indicate the current status of the task. This can be "pending", "in-progress", or "completed".
            - `results`: A string detailing the results of the task. This should be empty if the task is still pending or in-progress.

            
            For example:

            [
                {{
                    "id": "T001",
                    "description": "Authenticate user credentials",
                    "status": "pending"
                    "results": ""
                }},
                {{
                    "id": "T002",
                    "description": "Query database for user data",
                    "status": "pending"
                    "results": ""
                }}
            ]

            Now, based on the provided input, list out the tasks in the specified format.

            This is the available list of tools that you need to generate tasks based on available tools:
            {tools_list}



        """
        return prompt.format(data=data,tools_list=tools_list)
        
# BafCode Framework

## Introduction:

BafCode is a streamlined Flask framework designed to facilitate the swift development of AI agents. It offers a structured directory for configuring LLMs, prompts, LLM commands, and more. The core vision behind BafCode is to provide developers with a platform where they can effortlessly commence the building of their AI agents.

## How It Works:

At its essence, BafCode operates through two primary components: the **Agent** and the **Responder**.

1. **Agent**: The agent is equipped with functionalities we refer to as commands and LLM decision-making capabilities. Upon receiving a request containing a message, the agent leverages the LLM decision-making process to ascertain the appropriate command to execute.
    - For instance, if a request message says, "What are my latest emails in the inbox?", the agent uses the LLM decision process to discern the best-fitting command to run. Assume there exists a command named `getLastEmails`. This command, when executed, might integrate with an API to retrieve the ten most recent emails. The retrieved emails, paired with a specific prompt crafted by the developer, are then passed on to the Responder.

2. **Responder**: The Responder processes the emails and the prompt, subsequently generating a refined response to return to the end-user.

## Building an Agent Using BafCode:

1. **Setup**: Clone the BafCode Framework repository.
    ```cmd
    git clone https://github.com/aitelabrandig/bafcode
    
    ```

2. **Docker Setup (Optional)**: Utilize Docker and docker-compose if you prefer this approach to kickstart the framework.
    ```cmd
   docker-compose up -d
    
    ```
3. **Manual Setup**: Alternatively, you can navigate to the `src` directory and execute `python app.py` to start the framework manually.
    ```cmd
        cd src
        python app.py
    
    ```
4. **Command Creation**: Begin by crafting a command. Create a file within the `agent/commands` directory. For better organization, especially when dealing with larger agents, consider grouping related commands within subdirectories.

##### Creating a File in `agent/commands`:

###### Windows (Command Prompt):

```cmd
// Ensure you're in src directory
echo. > agent\commands\your_command_filename.py
```
###### Windows (PowerShell):
```cmd
// Ensure you're in src directory
New-Item -Path '.\agent\commands\' -Name 'your_command_filename.py' -ItemType 'file'

```
###### macOS and Ubuntu (Terminal):

```cmd
// Ensure you're in src directory
touch agent/commands/your_command_filename.py

```
##### Creating a File in `prompts`:

###### Windows (Command Prompt):

```cmd
// Ensure you're in src directory
echo. > prompts\your_prompt_filename.py
```
###### Windows (PowerShell):
```cmd
// Ensure you're in src directory
New-Item -Path '.\prompts\' -Name 'your_prompt_filename.py' -ItemType 'file'

```
###### macOS and Ubuntu (Terminal):

```cmd
// Ensure you're in src directory
touch prompts/your_prompt_filename.py

```
###### Prompt file example:
```python


class LastEmailsPrompt:
    def get_last_emails(data):
      prompt = """ 
         Please provide a concise summary of the most recent emails from the user's inbox.

            Instructions:
            1. Ensure the confidentiality and privacy of the user's data at all times.
            2. Summarize each email without compromising the essence of its content.
            3. Prioritize relevance and brevity in your summaries.
            4. Limit your response to the information present in the provided data.

            Email Data:
            {data}


           """
      
      return prompt.format(data=data)

    
```
###### Import Prompt class in `prompts/__init__.py`:
```python
from .email.last_emails_prompt import LastEmailsPrompt
```
###### Command file example:
```python
from core import framework_logger
from prompts import LastEmailsPrompt
class GetLastEmail:
    def __init__(self):
        self.logger = framework_logger

    def execute(self, data):
       
        return prompt
```

5. **Command Import and Mapping**: Ensure you import your newly created command in the `__init__.py` file and declare its name within the `command_mapping` object.
    ```python
    # Example in __init__.py
    from .email_commands.get_last_email import GetLastEmail

    # Define your commands here
    command_mapping = {
        "getLastEmail": GetLastEmail,
    }
    ```


6. **API Integration**: If your command needs to pull data using an API (which is often the case), create an API file within the `api` directory. For clarity, you can structure multiple endpoints of the same API within its subfolder.

##### Creating a File in `api`:

##### Windows (Command Prompt):

```cmd
// Ensure you're in src directory
echo. > api\email_api\your_api_filename.py
```
##### Windows (PowerShell):
```cmd
// Ensure you're in src directory
New-Item -Path '.\api\email_api' -Name 'your_api_filename.py' -ItemType 'file'

```
##### macOS and Ubuntu (Terminal):

```cmd
// Ensure you're in src directory
touch api/email_api/your_api_filename.py

```

##### API file example:
```python
import requests
from core import framework_logger

EMAIL_API_ENDPOINT = "https://fakerapi.it/api/v1/texts?_quantity=1&_characters=500"  # Placeholder email API endpoint

def get_last_email(user_id):

    logger = framework_logger

    if not user_id:
        logger.error("User ID not provided for fetching last email.")
        raise ValueError("User ID is requiread to fetch the last email.")

    # Form the API request
    params = {'user_id': user_id}
    response = requests.get(EMAIL_API_ENDPOINT, params=params)

    # Handle API response
    if response.status_code != 200:
        logger.error(f"Error fetching last email for user {user_id}. API response: {response.text}")
        raise Exception(f"Error fetching last email. API responded with: {response.text}")

    email_data = response.json()
    return email_data

```


7. **API Usage**: Once your API is set up, import and utilize it within your command file and return the required data.
##### Import the api function in api/__init__.py 
```python
from .email_api.get_last_email_api import get_last_email
```
##### Example of Importing an API function in your command file:
```python
from api import get_last_email
from core import framework_logger
from prompts import LastEmailsPrompt
class GetLastEmail:
    def __init__(self):
        self.logger = framework_logger

    def execute(self, data):
        user_id = data['user_id']
        if not user_id:
            self.logger.error("User ID not provided for GetLastEmail command.")
            raise ValueError("User ID is required to fetch the last email.")

        emails = get_last_email(user_id)
        prompt = LastEmailsPrompt.get_last_emails(emails)
        return prompt
```
8. **LLM Setup**: Adjust the LLM as per your requirements. While default configurations for OpenAI GPT-3.5 and GPT-4 are provided, you can introduce new LLMs by creating a dedicated file inside the `llms` folder. Adjust the imports and class usage in both `agent/llm_decision/decision.py` and `responder/llm_response`.

##### Create new LLM Class
##### Windows (Command Prompt):

```cmd
// Ensure you're in src directory
echo. > llms\your_llm_filename.py
```
##### Windows (PowerShell):
```cmd
// Ensure you're in src directory
New-Item -Path '.\llms' -Name 'your_llm_filename.py' -ItemType 'file'

```
##### macOS and Ubuntu (Terminal):

```cmd
// Ensure you're in src directory
touch llms/your_llm_filename.py

```

##### File Example
```python
from core import framework_logger
from config import Config

class LLMClass:
    def __init__(self):
        self.logger = framework_logger

        # Initialize LLM Configuration (should be kept secret and ideally loaded from a secure environment)


    def process(self,message,prompt):
    
        if not prompt:
            self.logger.error("No prompt provided for OpenAI LLM.")
            raise ValueError("A prompt is required for processing.")

        try:
            # Use OpenAI's Completion API to get the model's response
            response = 'Your LLM Setup To generate Response'
            # The returned response should be a sting e.g: ' This the response'
            return response 

        except Exception as e:
            self.logger.error(f"Error processing with OpenAI LLM: {str(e)}")
            return {
                'message': "Error processing with OpenAI LLM.",
                'status': "error"
            }
```


9. **Agent Activation**: With everything set, execute the agent by running `python app.py` within the `src` directory. For testing, use Postman (or a similar tool) to dispatch a POST request to the `/generate` endpoint, including a JSON payload with your message:
    ```cmd
    // Ensure you're in src directory
    python app, py
    
    ```
##### Request Body:
    ```json
    {
        "message": "Your desired message here"
        // Add any needed data here
    }
    ```
And that's it! You've now successfully created an AI agent using the BafCode Framework, offering a swift and streamlined development process.

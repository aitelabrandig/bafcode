# BafCode Framework

## Introduction 🌐:

BafCode is an efficient Flask framework tailored for the rapid creation of AI agents. It provides a structured directory setup, catering to configurations for Large Language Models (LLMs), prompts, LLM tools, and additional features. The primary aim of BafCode is to offer a platform for developers, enabling them to quickly initiate the construction of AI solutions.

## How It Works ⚙️:

BafCode primarily consists of two major components: the Agent 🤖 and the Responder 📩.

Agent: This component contains specific features, referred to as tools, along with LLM decision-making abilities. When a request with a particular message is received, the agent uses its LLM decision-making mechanism to determine the suitable tool to be applied.

For example, if a request's content asks, "What are my newest emails in the inbox?", the agent employs its LLM decision methodology to select the most relevant tool. Suppose there's a tool titled `getLastEmails`. This tool might connect with an API to fetch the latest ten emails. The obtained emails, combined with a developer-defined prompt, are subsequently passed to the Responder.


Responder: The Responder takes the provided emails and the prompt, then formulates a precise response to be sent back to the user.

## Constructing an AI Agent with BafCode: 🔧

 **Simplicity is Key**: First, perform the initial setup, followed by coding your desired agent tools. BafCode manages the subsequent processes, letting you concentrate on tool functionality.
1. **Initial Setup: 🚀**:  Use the BafCode Command Line Interface (CLI) to set up your project.
    ```cmd
    pip install bafcode
    bafcode setup
    ```

2. **Docker Configuration (Optional): 🐳**:If you're inclined to use Docker, leverage Docker and docker-compose to get the framework up and running.
    ```cmd
   docker-compose up -d 
    ```

3. **Manual Initialization: 📂**: If you prefer, you can directly head to the `src` directory and activate the framework using `bafcode start`.
    ```cmd
        cd src
        bafcode start or python app.py
    
    ```

### Get Started

4. **Develop Your Tool**: Start by designing your desired tool. Initiate a file inside the tools directory. For enhanced structuring, especially for more extensive agents, it's recommended to categorize similar tools into subfolders.

##### Creating a File in `tools`:
```cmd
  bafcode make tool <your_tool_name>
```

**Tool Code Example:**
```python
 
from core import BafLog
from prompts import ExamplesGetExamplePrompt
from api import ExamplesGetExampleAPI

# Optionally, import any other required modules or packages
# E.g., from api import YourAPI
# E.g., from prompts import YourPrompt

class ExamplesGetExample:
  def __init__(self):
     self.logger = BafLog

  def execute(self, data):
    # Process data here
    response = ExamplesGetExampleAPI.process(data)

    prompt = ExamplesGetExamplePrompt.examples_get_example_prompt(response)
    return prompt


        
```

At times, you don't need to modify your Tool Logic code, as the bafcode make command automatically imports everything required, like the prompt and the API function. Simply set up your prompt and API, and everything will run seamlessly.

**API Example:**
Your tool-specific API can be located in the api folder. Here's an example of how it might appear:

```python
 
import requests
from core import BafLog

YOUR_API_ENDPOINT = "https://fakerapi.it/api/v1/texts?_quantity=1&_characters=500"  # Placeholder email API endpoint
logger = BafLog

class ExamplesGetExampleAPI:
    def process(your_parameters):
                
        response = requests.get(YOUR_API_ENDPOINT, params=your_parameters)

        # Handle API response
        if response.status_code != 200:
         logger.error(f"Error fetching last ExamplesGetExample data. API response: {response.text}")
         raise Exception(f"Error fetching last ExamplesGetExample data. API response: {response.text}")

        your_data_variable = response.json()
        return your_data_variable
        
```
Thanks to BafCode CLI, you're provided with a template to set up the tool-specific API. While you can modify variable names and the logic behind the returned data, ensure the returned data is clear. This is because the Responder processes it using an LLM to interpret the data. Cleaner data will result in a higher quality response from the Responder.

**Prompt Example:**
Kudos to BafCode CLI once again, as it has pre-configured a draft for the tool-specific prompt. All you need to do is adjust the prompt to dictate how you'd like the Responder to deliver the response.

```python
 
from core import BafLog
# Optionally, import any other required modules or packages

class ExamplesGetExamplePrompt:  # Replace ExamplesGetExample with the name of your prompt
    def examples_get_example_prompt(data):
        prompt = """
            Your Prompt Here
            ExamplesGetExample Data:
            {data}
        """
        return prompt.format(data=data)
        
```
You'll find that the current setup is straightforward. With just two files, you can quickly and easily build your first agent. BafCode genuinely allows you to concentrate on your prompt and the tools available to your agent, helping to eliminate the typical `As a Language Model, I can't...` limitations.

**5: Setup LLM:**
Rest assured, we haven't overlooked this crucial aspect: the brain behind the responder and agent. With BafCode CLI, setting up LLMs is a breeze. Just one command will generate your LLM file, allowing you to seamlessly integrate it with your agent.

```cmd
bafcode make llm <your_llm_name>
```
File will be generated in `llms` folder

**LLM Example:**
This is how the LLM file code looks like :

```python
 
 
from core import BafLog
from config import Config
# Optionally, import any other required modules or packages
# E.g., from api import YourLLMAPI


class ExampleLLM:
    def __init__(self):
      self.logger = BafLog

# Initialize your LLM API config here
       

    def process(self,message,prompt):
    
      if not prompt:
       self.logger.error("No prompt provided for Example LLM.")
       raise ValueError("A prompt is required for processing.")

      try:
         # use your LLM API and pass in the prompt and message to process here
         response = 'Use your LLM API here e.g., YourLLMAPI.process(prompt,message)'
         return response
         # Response should be a string e.g., "This is a response from the LLM API."

      except Exception as e:
         self.logger.error(f"Error processing with Example LLM: {str(e)}")
         return {
          'message': "Error processing with LLM.",
          'status': "error"
              }


        
```
Once more, BafCode CLI provides you with a foundational code for your LLM. All you need to do is integrate your LLM API or define the logic of how the LLM receives and responds to messages. Just make sure to refine the LLM's response, ensuring you return a final string response rather than an array or object.

**LLM Configuration:**
Apologies for the oversight. As of now, LLMs are not set up automatically. Here's the single step you need to follow:

Navigate to the `config` folder at the project root. Within it, you'll find `llms_config.py`. In this file, replace the `DEFAULT_LLM` value with your preferred LLM by specifying the LLM Class name.

`config/llms_config.py`
```python
import os
from dotenv import load_dotenv
load_dotenv()




# General configurations for all LLMs
class LLMsConfig:
    # Timeout for LLM requests (if applicable)
    LLM_TIMEOUT = 15  # in seconds

    # Default LLM to use if no LLM is specified in the request
    DEFAULT_LLM = "OpenAILLM"

    # OpenAI LLM configurations
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Should ideally be loaded from a secure environment variable or vault
    OPENAI_ENGINE = "gpt-3.5-turbo"  # Default engine for OpenAI requests
    OPENAI_MAX_TOKENS = 150  # Default maximum tokens for responses from OpenAI

    # If you have other LLMs or external services, add their configurations similarly:

    # Example: SomeOtherLLM configurations
    # SOMEOTHERLLM_API_ENDPOINT = "https://someotherllmapi.example.com/generate"
    # SOMEOTHERLLM_AUTH_TOKEN = "YOUR_SOMEOTHERLLM_API_TOKEN"


```

9. **Agent Usage**: With everything set, execute the agent by running `python app.py` within the `src` directory. For testing, use Postman (or a similar tool) to dispatch a POST request to the `/generate` endpoint, including a JSON payload with your message:
    ```cmd
    python app.py or bafcode start
    ```
##### Request Body:
    ```json
    {
        "message": "Your desired message here"
        // Add any needed data here
    }
    ```
And that's it! You've now successfully created an AI agent using the BafCode Framework, offering a swift and streamlined development process.

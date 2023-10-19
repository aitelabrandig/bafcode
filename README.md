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
2. **Docker Setup (Optional)**: Utilize Docker and docker-compose if you prefer this approach to kickstart the framework.
3. **Manual Setup**: Alternatively, you can navigate to the `src` directory and execute `python app.py` to start the framework manually.
4. **Command Creation**: Begin by crafting a command. Create a file within the `agent/commands` directory. For better organization, especially when dealing with larger agents, consider grouping related commands within subdirectories.
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
7. **API Usage**: Once your API is set up, import and utilize it within your command file and return the required data.
8. **LLM Setup**: Adjust the LLM as per your requirements. While default configurations for OpenAI GPT-3.5 and GPT-4 are provided, you can introduce new LLMs by creating a dedicated file inside the `llms` folder. Adjust the imports and class usage in both `agent/llm_decision/decision.py` and `responder/llm_response`.
9. **Agent Activation**: With everything set, execute the agent by running `python app.py` within the `src` directory. For testing, use Postman (or a similar tool) to dispatch a POST request to the `/generate` endpoint, including a JSON payload with your message:
    ```json
    {
        "message": "Your desired message here"
        // Add any needed data here
    }
    ```
And that's it! You've now successfully created an AI agent using the BafCode Framework, offering a swift and streamlined development process.

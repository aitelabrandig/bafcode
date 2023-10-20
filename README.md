# BafCode Framework

## Introduction:

BafCode? It's a sleek Flask framework for whipping up AI agents fast. Got directories ready for your LLMs, prompts, tools, and all that jazz. BafCode's mantra? Code, chill, and let the AI magic happen.

## How It Works:

At its essence, BafCode operates through two primary components: the **Agent** and the **Responder**.

1. **Agent**: The agent is equipped with functionalities we refer to as tools and LLM decision-making capabilities. Upon receiving a request containing a message, the agent leverages the LLM decision-making process to ascertain the appropriate tool to use.
    - For instance, if a request message says, "What are my latest emails in the inbox?", the agent uses the LLM decision process to discern the best-fitting tool to run. Assume there exists a tool named `getLastEmails`. This tool, when used, might integrate with an API to retrieve the ten most recent emails. The retrieved emails, paired with a specific prompt crafted by the developer, are then passed on to the Responder.

2. **Responder**: The Responder processes the emails and the prompt, subsequently generating a refined response to return to the end-user.

## Building an Agent Using BafCode:
 **Simplicity**:Set up, then code your agent tools. BafCode handles the rest. Focus on functionality. 💻🛠️
1. **Setup**: Setup the project using BafCode CLI
    ```cmd
    pip install bafcode
    bafcode setup
    ```

2. **Docker Setup (Optional)**: Utilize Docker and docker-compose if you prefer this approach to kickstart the framework.
    ```cmd
   docker-compose up -d
    
    ```
3. **Manual Setup**: Alternatively, you can navigate to the `src` directory and use `bafcode start` to start the framework manually.
    ```cmd
        cd src
        bafcode start or python app.py
    
    ```

4. **Tool Creation**: Begin by crafting a tool. Create a file within the `tools` directory. For better organization, especially when dealing with larger agents, consider grouping related tools within subdirectories.

##### Creating a File in `tools`:
```cmd
  bafcode make tool <your_tool_name>
```



9. **Agent Activation**: With everything set, execute the agent by running `python app.py` within the `src` directory. For testing, use Postman (or a similar tool) to dispatch a POST request to the `/generate` endpoint, including a JSON payload with your message:
    ```cmd
    // Ensure you're in src directory
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

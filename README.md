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

9. **Agent Activation**: With everything set, execute the agent by running `python app.py` within the `src` directory. For testing, use Postman (or a similar tool) to dispatch a POST request to the `/generate` endpoint, including a JSON payload with your message:
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

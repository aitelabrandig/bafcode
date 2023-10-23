# BafCode Framework Documentation
## Overview 🌐
BafCode is a powerful Flask framework designed for the swift development of AI agents. Its robust features and simple setup make it an essential tool for developers looking to dive into AI solution development without the fuss.

## Features 🌟
 **Auto Project Setup**: Get started quickly with an organized project structure.

 **Docker Option**: Use Docker for a more streamlined development environment.

 **BafCode CLI**: Speed up agent tools creation with our dedicated command-line interface.

 **Focus on Agent Tools**: Spend time creating the tools, not setting up the framework.

 **Automated Processes**: Auto-generates and imports tool APIs and prompt files, so you can focus on agent tool logic.

## Why Choose BafCode? 🤖
With BafCode, you can solely concentrate on agent tool development. The framework takes care of generating and importing essential components like prompt and API for you, leading to a more efficient development process.

## Requirements 📋
Python Environment

Optional: Docker for containerization

Command-Line Interface (for BafCode CLI commands, install it using `pip install bafcode`)

## Core Components ⚙️
### Manager:

1. **Generates a Task list.**
2. **Sends a single task to the agent.**
3. **Receives task results.**
4. **Saves the task result in a session with status (either Completed or Failed).**
5. **Removes completed task from the task list and sends the next task with "pending" status to the agent.**


### Agent:
1. **Receives a task.**
2. **Decides which tool to use based on the received task.**
3. **Uses the tool to process the task.**
4. **Sends the tool results to the manager.**


### Responder:

1. **Generates a good response based on the tool results.**
2. **Returns the response to the application.**
3. **Receives the final message from the manager.**


### Tools:

1. **Tools are used by the Agent to perform a specific Task.**
2. **You can generally place any action function inside the tool, and it will be executed once the Agent decides to use it.**
3. **You can typically embed any function inside the tool file, and it will be executed when the Agent opts to use it.**
4. **The tool can utilize external APIs by coding the API logic and invoking the imported API process function in any tool file you produce.**



### Prompts:

1. **Prompts are cues used by LLMS.**
2. **You can use prompt files wherever LLMS is utilized.**
3. **You can modify default prompts used by the main components of the platform.**
4. **You can also tailor default prompts employed by the central elements of the platform.**
5. **It is possible to create a unique prompt for every tool or API.**

### LLMS:

1. **You can use Multiple LLMs, each LLM for a specific case.**
2. **Can be used in the APIs to generate a like humane text to be saved in a database or posted in X tweet.**
3. **Can be used by the Responder to generate a clean response based on the task list results provided by the Manager Component.**
4. **Can be used by the agent to decide which tool to use based on the task provided by the Manager Component.**
5. **Can be used by Manager to generate Task List based on the user requirements.**
6. **Used By Other Components to generate a Humanistic response.**


## How to Build an AI Agent using BafCode 🔧

**Initial Setup 🚀**
Use the BafCode CLI to kickstart your project.

```cmd
pip install bafcode
bafcode setup
```

**Docker Configuration (Optional) 🐳**
For Docker enthusiasts, use Docker and docker-compose for easier framework deployment.

```cmd
docker-compose up -d
``` 
**Manual Initialization 📂**
Prefer a hands-on approach? Navigate to the src directory and start the framework.

```cmd
cd src
bafcode start
```
**Develop Your Tool 🛠**
Begin by crafting your desired tool. Initialize a file within the tools directory. For larger agents, categorize related tools into subdirectories.

```cmd
bafcode make tool <your_tool_name>
```
Once your tool is created, related APIs and prompts are auto-generated and imported.

**Setup LLM 🧠:** Set up the brain behind your agent and responder with ease using BafCode CLI.

By default, the agent and the responder components are using `openai_llm`, you just need to add your OPENAI KEYS in `.env`

If you are interested to use any other llm, you can make one using our BafCode CLI

```cmd
bafcode make llm <your_llm_name>
```
The LLM file will be created in the `llms` directory. You're welcome to incorporate your desired LLM logic into it.

**Agent Running 🚀**
With all components ready, launch the agent.

```cmd
python app.py or bafcode start
```
For testing, employ Postman to send a POST request to the `/generate` endpoint with your message.

**Additional Notes 📝**
When developing tools, often you won't need to alter the tool logic. The bafcode make command takes care of importing and generating essentials like prompts and APIs.

LLMs currently need manual configuration. Visit `config/llms_config.py` and replace the DEFAULT_LLM with your LLM Class name.


**Congratulations, you are now empowered to efficiently craft AI agents using the BafCode Framework!**

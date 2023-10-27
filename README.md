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
Agent: Contains specialized tools and LLM decision-making abilities. It determines the appropriate tool for a received message.

Responder: Generates precise responses based on the data provided by the agent.


## Tools in BafCode Framework: A Deep Dive 🛠
Within the BafCode Framework, tools play a pivotal role in the functioning of the AI agent. They act as intermediaries between the agent and external systems or services, Here's a detailed breakdown:

**1. Purpose of Tools 🎯**
Tools are essentially functions that the Agent component employs to perform designated tasks. Whether it's fetching new emails, getting weather updates, or any other operation, you can build an agent tool for that purpose.

**2. Integration with APIs 🌍**
A significant function of tools is their ability to connect with the outside world. They achieve this by utilizing APIs (Application Programming Interfaces). An API is a set of routines and protocols that allow tools to request and exchange data with external systems, services, or databases and you can customize the api of the tool in `api` folder.


For instance, if there's a tool designed to fetch the latest news headlines, it would communicate with a news service's API to retrieve this data.

**3. Prompt  📝**
Once a tool has successfully retrieved the necessary data via an API, it doesn't just hand this raw data over to the Responder. Instead, it passed inside a 'prompt' which you can customize in the `prompts` folder. This prompt provides context, ensuring that the data is presented in a manner that the Responder component can understand and utilize.

**4. Interaction with the Responder 📩**
After the prompt is returned, the Agent component passes it to the Responder component. The Responder then crafts a precise and meaningful response based on the context and information within the prompt.

For example, if the tool fetched weather data indicating rain and the prompt was "The weather forecast suggests rain today. ('rain' is the retreived data from api)", the Responder might generate a response like "It's going to rain today. Don't forget your umbrella!"

In essence, tools are the bridge that enables the Agent to interact with the external world, gather information, and set the stage for the Responder to deliver valuable outputs to the end-users.

<img width="1340" alt="image" src="https://github.com/aitelabrandig/bafcode/assets/95383805/e0ca8624-2662-46b8-b16c-f74056a64157">





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




## Contributing to BafCode

We welcome contributions to the BafCode framework! Here's a quick guide:

1. **Understand the Philosophy**: BafCode emphasizes enabling developers to focus on agent functionalities, not just the components.
2. **Fork & Branch**: Fork the repository and create a new branch for your changes.
3. **Commit**: Make sure to write clear and meaningful commit messages.
4. **Pull Request**: Submit a PR from your forked repository to the main BafCode repository.
5. **Review & Feedback**: Await review from maintainers and be open to feedback.

For detailed guidelines, please see our [Contribution Guide](./CONTRIBUTING.md).

Your contributions help improve BafCode for all users. Thank you! 🚀🌐


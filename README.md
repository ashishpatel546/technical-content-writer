# Technical Content Writer Crew

Welcome to the Technical Content Writer Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:

```bash
crewai install
```

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**
**Add your `BRAVE_SEARCH_KEY` into the `.env` file**

- Modify `src/technical_content_writer/config/agents.yaml` to define your agents
- Modify `src/technical_content_writer/config/tasks.yaml` to define your tasks
- Modify `src/technical_content_writer/crew.py` to add your own logic, tools and specific args
- Modify `src/technical_content_writer/main.py` to add custom inputs for your agents and tasks

## Running the Project

### Option 1: Using CrewAI CLI

To kickstart your flow and begin execution, run this from the root folder of your project:

```bash
crewai run
```

This command initializes the technical_content_writer Flow as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

### Option 2: Using the Gradio Web Interface

For a more user-friendly interface, you can run the Gradio web application using the provided shell script:

```bash
./start_app.sh
```

This script will:

- 🔧 Automatically create a virtual environment (if it doesn't exist)
- 📦 Install all required dependencies using `uv sync`
- 🚀 Launch the Gradio web interface at `http://localhost:7860`

**Prerequisites for the shell script:**

- Ensure you have `uv` installed (the script will check and notify you if it's missing)
- Make the script executable: `chmod +x start_app.sh`

The Gradio interface provides an intuitive web-based way to interact with your Technical Content Writer crew, allowing you to input topics and generate content through a clean, user-friendly interface.

## Understanding Your Crew

The technical_content_writer Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Technical Content Writer Crew or crewAI.

- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.

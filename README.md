# LangGraph Twitter Reflection Agent

A Python project using **LangGraph** and **LangChain** to generate and refine Twitter posts with AI. This project demonstrates a workflow where a message goes through **generation** and **reflection** nodes, improving tweets iteratively.

---

## Features

- Generates initial tweets based on user input.
- Reflects and critiques tweets to improve style, virality, and clarity.
- Iteratively alternates between generation and reflection until a stopping condition.
- Visualizes the state graph in both **ASCII** and **Mermaid** formats.

---



yaml


---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ShreyAC962/langchain.git
cd langchain
(Recommended) Create a Python virtual environment:

bash

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
Install dependencies with Poetry:

bash

poetry install
poetry add langchain langchain-ollama grandalf python-dotenv
Or with pip:

bash

pip install langchain langchain-ollama grandalf python-dotenv
Create a .env file in the project root if needed:

ini
OLLAMA_API_KEY=your_api_key_here
Usage
Run the main script:

bash
python main.py
This will:

Set up the MessageGraph with generation and reflection nodes.

Start the graph with an initial tweet.

Print the graph visualization in ASCII and Mermaid format.

Return the improved tweet after iterative reflection.

Example
Initial input tweet:

vbnet

@LangChainAI — newly Tool Calling feature is seriously underrated.
After a long wait, it's here - making the implementation of agents across different models with function calling super easy.
The agent will:

Generate an improved version.

Critique it.

Iterate until the tweet is polished.

Tech Stack
Python 3.11+

LangChain

LangGraph

Ollama

Grandalf for graph visualization

.env for environment variables
# LangGraph Twitter Reflection Agent

This project implements a **tweet generation + reflection loop** using **LangGraph**, **LangChain**, and **Ollama**.  
The system generates a tweet, critiques it, and rewrites it iteratively until the output is polished and high-quality.

---

## 🚀 Features

- 🔁 **Iterative AI workflow** using a LangGraph state machine  
- ✍️ **Tweet generation** using a tech-influencer persona  
- 🧠 **Tweet reflection & critique** using a viral-influencer persona  
- 🎯 Automatic improvement loop (Generate → Reflect → Generate...)  
- 📊 ASCII & Mermaid graph visualization  
- 🔌 Works with **Ollama local models** like `llama3.2`  

---


## 🔧 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/ShreyAC962/langchain.git
cd langchain

2️⃣ (Recommended) Create a Python virtual environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows


3️⃣ Install dependencies with Poetry
poetry install
poetry add langchain langchain-ollama grandalf python-dotenv

Or using pip:
pip install langchain langchain-ollama grandalf python-dotenv

▶️ Usage

Run the main pipeline:
python main.py
This will:

Initialize the MessageGraph with two nodes:

GENERATE

REFLECT

Pass your tweet through the improvement loop

Visualize the graph (ASCII + Mermaid)

Output the final improved tweet

🤖 What the Agent Does

Generate a better version of the tweet

Reflect, critique, and recommend improvements

Rewrite based on critique

Continue looping until the tweet is polished

🛠️ Tech Stack

Python 3.11+

LangChain

LangGraph

Ollama (llama3.2 etc.)

Grandalf → graph rendering

dotenv for environment variables
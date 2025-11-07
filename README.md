🧠 Chat with a PDF using LangChain + Ollama + FAISS
📄 Intelligent Document Q&A — Locally and Securely

This project demonstrates how to chat with your own PDF files using LangChain, FAISS, and Ollama — all running locally for speed and privacy.
It combines text chunking, embeddings, and retrieval-augmented generation (RAG) to let you ask natural language questions and get precise, context-aware answers from your documents.

🚀 Tech Stack
Component	Description
🧩 LangChain	Framework for LLM orchestration and RAG pipelines
📚 PyPDFLoader	Loads and extracts text from PDF documents
🧠 Ollama	Runs open-source LLMs and embedding models locally
🗂️ FAISS	Facebook’s efficient vector database for fast document retrieval
🧾 LangChain Hub	Provides pre-built prompts for RAG and QA tasks

⚙️ How It Works
Load the PDF using PyPDFLoader.

Split text into small chunks with overlaps for better context retention.

Generate embeddings for each chunk using the jina/jina-embeddings-v2-small-en model via Ollama.

Store and index those embeddings locally using FAISS.

Retrieve relevant chunks based on the user query.

Feed them into a structured QA prompt (RAG Prompt).

Generate context-aware answers using Llama 3 from Ollama.

🧰 Installation

Make sure you have Python 3.11+ and Ollama installed locally.
Then, set up a virtual environment and install the dependencies:

pip install langchain langchain-community langchain-ollama langchainhub faiss-cpu


Or if you’re using Pipenv:

pipenv install langchain langchain-community langchain-ollama langchainhub faiss-cpu

🧩 Folder Structure
vectorstore-in-memory/
├── main.py                        # Main execution script
├── react.pdf                      # Sample document
├── faiss_vectorstore_react_index/ # Saved FAISS index
└── README.md                      # Project documentation

💡 Key Features

✅ Local embeddings (no API key required)
✅ Private document processing
✅ Modular LangChain pipeline
✅ Persistent FAISS vectorstore
✅ Supports any PDF file
✅ Works offline with Ollama
Below is a **clean, structured, professional README.md** for your entire Streamlit + LangChain Documentation Helper project.
It explains **what the project does**, **how the ingestion + retrieval pipeline works**, **how Streamlit is used**, and **how everything ties together**.

---

# 📚 LangChain Documentation Helper Bot

An interactive ChatGPT-style Streamlit application that lets you query LangChain documentation using **RAG (Retrieval-Augmented Generation)** with **Pinecone**, **Ollama**, and **LangChain**.

This bot crawls LangChain docs, stores them in a vector database, and answers user queries with real source references — all inside a beautifully styled ChatGPT-like UI.

---

## 🚀 Features

### ✅ 1. **ChatGPT-style User Interface**

* Clean, modern UI using Streamlit
* Chat bubbles (User + Assistant)
* Sidebar with user profile & controls
* Smooth animation + CSS customization

### ✅ 2. **RAG Pipeline (Retrieval-Augmented Generation)**

* Docs scraped using `WebBaseLoader`
* Chunked using `RecursiveCharacterTextSplitter`
* Embedded with `OllamaEmbeddings (jina/jina-embeddings-v2-small-en)`
* Stored in **Pinecone Vector DB**
* Answered using **Llama 3** via `ChatOllama`
* Answers include **exact sources** used

### ✅ 3. **Conversation-Aware Retrieval**

Uses `create_history_aware_retriever()` so previous chat turns inform retrieval.
This makes the bot behave like ChatGPT with memory.

### ✅ 4. **Full Document Ingestion Pipeline**

You can ingest LangChain docs from multiple URLs and push them into Pinecone with:

```
python ingest.py
```



# ⚙️ Technology Stack

### **Frontend**

* Streamlit
* HTML + CSS (custom ChatGPT-like styling)

### **Backend / RAG**

* LangChain
* Pinecone Vector DB
* Ollama (Llama 3)
* Jina Embeddings
* WebBaseLoader for docs scraping

---

# 💡 How It Works (Full Breakdown)

## **1. Document Ingestion (ingest.py)**

This script performs the **RAG indexing process**:

### **Step 1 — Load LangChain documentation**

```python
loader = WebBaseLoader(url)
raw_documents = loader.load()
```

### **Step 2 — Chunk the documents**

Smaller text chunks → better semantic search.

```python
text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
documents = text_splitter.split_documents(raw_documents)
```

### **Step 3 — Convert chunks to embeddings**

Using Jina embeddings:

```python
embeddings = OllamaEmbeddings(model="jina/jina-embeddings-v2-small-en")
```

### **Step 4 — Store in Pinecone**

```python
PineconeVectorStore.from_documents(documents, embeddings, index_name)
```

#### **Run the ingestion**

```bash
python ingest.py
```

---

# 🤖 2. RAG Answering Pipeline (backend/core.py)

### **Step 1: Initialize retriever + embeddings**

```python
docsearch = PineconeVectorStore(embedding=embeddings, index_name=INDEX_NAME)
```

### **Step 2: LLM initialization**

```python
chat = ChatOllama(model="llama3", temperature=0)
```

### **Step 3: Load prompts from LangChain Hub**

```python
retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
rephrase_prompt = hub.pull("langchain-ai/chat-langchain-rephrase")
```

### **Step 4: History-aware retriever**

```python
history_aware_retriever = create_history_aware_retriever(
    llm=chat,
    retriever=docsearch.as_retriever(),
    prompt=rephrase_prompt
)
```

This rephrases follow-up questions automatically.

### **Step 5: Full QA Chain**

```python
qa = create_retrieval_chain(history_aware_retriever, stuff_documents_chain)
result = qa.invoke({"input": query, "chat_history": chat_history})
```

The final output includes:

* Answer
* Context documents (used as sources)

---

# 💬 3. Streamlit Interface (main.py)

### Key Features:

✔ Custom ChatGPT-style theme
✔ User profile sidebar
✔ Chat history memory
✔ Styled user + assistant messages
✔ Automatic source formatting

### The UI Workflow:

1. User enters a question
2. Streamlit calls `run_llm()`
3. The bot retrieves documents
4. Llama 3 generates an answer
5. The app shows answer + sources

---

# 🧪 Running the Project

### **1. Install dependencies**

```bash
pipenv install 
```

### **2. Start Ollama (make sure llama3 model is installed)**

```bash
ollama pull llama3
ollama pull jina/jina-embeddings-v2-small-en
```

### **3. Run document ingestion**

```bash
python ingest.py
```

### **4. Start Streamlit app**

```bash
streamlit run main.py
```

---

# 🔐 Environment Variables (.env)

Create a `.env` in project root:

```
PINECONE_API_KEY=your_key
INDEX_NAME=langchain-doc-index
```

---







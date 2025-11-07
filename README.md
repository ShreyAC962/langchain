# Vector-Based Question Answering on Large Text Files

This project demonstrates how to efficiently query a **huge text file** (like a book) using vector embeddings and an LLM, even when the file is several gigabytes in size.

---

## Overview

When dealing with extremely large files, querying them directly is inefficient. This approach uses **chunking, embeddings, and a vector database** to retrieve only relevant information and feed it to an LLM.

---

## Steps

### 1. Split the File into Chunks

- Large files are split into smaller text chunks.
- Each chunk represents a manageable piece of the book.
- This allows the system to process huge files efficiently.

### 2. Embed Each Chunk

- Each chunk is converted into a **vector embedding** using an embedding model.
- Embeddings are numerical representations of text, capturing semantic meaning.
- Example: `chunk_embedding = embedding_model.encode(chunk)`

### 3. Store in a Vector Database

- All embeddings are stored in a vector database like **Pinecone**.
- Each vector corresponds to a chunk of the book.
- This allows for **efficient similarity search**.

### 4. Query the Vector Database

- When a user asks a question about the book:
  1. The question is embedded into a vector (`query_vector`).
  2. The vector database finds the **closest vectors** (chunks) to the query.
  3. These closest vectors represent the **most relevant chunks** of the book.

### 5. Augment the Prompt

- The relevant chunks are appended to the prompt.
- Example prompt:  

- This provides the LLM with **grounded context** to answer accurately.

### 6. Send to LLM

- The augmented prompt is sent to an LLM.
- The LLM generates the answer based on the **provided context**.
- This ensures **accurate, context-aware responses**.

---

## Summary

1. Split the book into chunks.
2. Embed chunks into vectors.
3. Store embeddings in a vector database.
4. Embed the query and retrieve relevant chunks.
5. Append relevant chunks to the prompt.
6. Send augmented prompt to the LLM for a grounded answer.

---

This approach allows you to efficiently query **large books or documents** without sending the entire file to the LLM, while still maintaining **accurate and context-aware answers**.

import os
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_ollama import OllamaEmbeddings
from langchain_pinecone import PineconeVectorStore

# Load environment variables
load_dotenv()
INDEX_NAME = os.getenv("INDEX_NAME", "langchain-doc-index")

# Initialize embeddings
embeddings = OllamaEmbeddings(model="jina/jina-embeddings-v2-small-en")

# List of LangChain docs URLs to ingest
urls = [
    "https://python.langchain.com/en/latest/",
    "https://python.langchain.com/docs/get_started/introduction",
    "https://python.langchain.com/docs/modules/model_io/models/",
    "https://python.langchain.com/docs/modules/chains/",
    "https://python.langchain.com/docs/modules/agents/",
]

def ingest_docs():
    # Load documents from each URL
    raw_documents = []
    for url in urls:
        loader = WebBaseLoader(url)
        raw_documents.extend(loader.load())

    print(f"✅ Loaded {len(raw_documents)} documents")

    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
    documents = text_splitter.split_documents(raw_documents)

    print(f"✂️ Split into {len(documents)} chunks")

    # Upload to Pinecone
    PineconeVectorStore.from_documents(
        documents,
        embeddings,
        index_name=INDEX_NAME
    )
    print("🎉 All documents uploaded to Pinecone successfully!")

if __name__ == "__main__":
    ingest_docs()

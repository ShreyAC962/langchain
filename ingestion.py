import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
# from langchain_openai import OpenAIEmbeddings
from langchain_ollama import OllamaEmbeddings
from langchain_pinecone import PineconeVectorStore

if __name__ == "__main__":
    # RAG Ingestion - (Load, Split, Embed, Store)
    load_dotenv()
    print("Ingesting...")
    loader = TextLoader("/Users/shreyachinthala/Documents/vector-dbs/mediumblog1.txt")
    documents = loader.load()

    print("Splitting...")
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    print(f"Created {len(texts)} chunks")

    print("Embedding model...")
    # embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    embeddings = OllamaEmbeddings(model="jina/jina-embeddings-v2-small-en")

    print("Ingesting...")
    PineconeVectorStore.from_documents(texts, embeddings, index_name=os.environ['INDEX_NAME'])
    print("Finish")

    # RAG Retrieval - (Query, Embed, Retrieve)
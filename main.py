from dotenv import load_dotenv
load_dotenv()
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_text_splitters import CharacterTextSplitter

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain


from langchain import hub

if __name__ == "__main__":
    print("This script is being run directly.")
    pdf_path = "/Users/shreyachinthala/Documents/vectorstore-in-memory/react.pdf"
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(
        chunk_size=1000, chunk_overlap=30, separator="\n"
    )
    docs = text_splitter.split_documents(documents=documents)

    embeddings = OllamaEmbeddings(model="all-minilm")
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local("faiss_vectorstore_react_index")

    new_vectorstore = FAISS.load_local(
        "faiss_vectorstore_react_index",
        embeddings,
        allow_dangerous_deserialization=True,
    )

    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    combine_docs_chain = create_stuff_documents_chain(
        ChatOllama(model="llama3"), retrieval_qa_chat_prompt
    )
    retrieval_chain = create_retrieval_chain(
        new_vectorstore.as_retriever(), combine_docs_chain
    )
    result = retrieval_chain.invoke(
        {"input": "What is React and why is it useful in 3 sentences with bullet points and each point seperated by dashed line?"}
    )
    print(result["answer"])
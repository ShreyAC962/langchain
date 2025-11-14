from typing import Any, Dict, List
from dotenv import load_dotenv
load_dotenv()

from langchain import hub


from langchain_pinecone import PineconeVectorStore

from langchain_ollama import ChatOllama

from langchain_ollama import OllamaEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever



from colorama import Fore, Style, init
init(autoreset=True)




INDEX_NAME = "langchain-doc-index"

def run_llm(query : str, chat_history : List[Dict[str, Any]] = []):
    embeddings = OllamaEmbeddings(model="jina/jina-embeddings-v2-small-en")
    docsearch = PineconeVectorStore(embedding = embeddings, index_name=INDEX_NAME)
    chat = ChatOllama(model="llama3", temperature=0)

    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    stuff_documents_chain = create_stuff_documents_chain(chat,retrieval_qa_chat_prompt)
    
    rephrase_prompt = hub.pull("langchain-ai/chat-langchain-rephrase")

    history_aware_retriever = create_history_aware_retriever(
        llm = chat,
        retriever = docsearch.as_retriever(),
        prompt = rephrase_prompt
    )

    qa = create_retrieval_chain(
        history_aware_retriever, 
        stuff_documents_chain
    )

    result = qa.invoke({"input": query, "chat_history" : chat_history})
    new_result = {
        "query": result["input"],
        "result" : result["answer"],
        "source_documents" : result["context"]   
    }
    return new_result

if __name__ == "__main__":
    res = run_llm(query = "What is LangChain?")
    print(Fore.GREEN + "Answer: " + Style.BRIGHT + res["result"])
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3", temperature=0)

# Pull RAG prompt
prompt = hub.pull("rlm/rag-prompt")

# Build pipeline
generation_chain = prompt | llm | StrOutputParser()

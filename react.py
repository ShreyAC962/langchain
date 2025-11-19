from dotenv import load_dotenv
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain_ollama import ChatOllama


load_dotenv()
@tool
def triple(num : float) -> float:
    """Returns the triple of a number."""
    return num * 3

tools = [TavilySearch(max_results=1), triple]
llm = ChatOllama(model="llama3", temperature=0).bind_tools(tools)
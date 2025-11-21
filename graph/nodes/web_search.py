from typing import Any, Dict

from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_tavily import TavilySearch

from graph.state import GraphState

load_dotenv()

# Tavily tool
web_search_tool = TavilySearch(max_results=1)


def web_search(state: GraphState) -> Dict[str, Any]:
    print("---WEB SEARCH---")
    question = state["question"]
    documents = state["documents"]

    # Run Tavily search
    tavily_results = web_search_tool.invoke({"query": question})

    print("RAW TAVILY RESULT:", tavily_results)

    # -----------------------------
    # FIX: Handle error from Tavily
    # -----------------------------
    if "error" in tavily_results:
        error_msg = tavily_results["error"]
        print("TAVILY ERROR:", error_msg)

        # Store the error as a document so graph doesn't break
        web_results = Document(page_content=f"Tavily error: {error_msg}")

        if documents is not None:
            documents.append(web_results)
        else:
            documents = [web_results]

        return {"documents": documents, "question": question}

    # -----------------------------
    # NORMAL FLOW (no error)
    # -----------------------------
    joined_tavily_result = "\n\n".join(
        result["content"] for result in tavily_results.get("results", [])
    )

    web_results = Document(page_content=joined_tavily_result)

    if documents is not None:
        documents.append(web_results)
    else:
        documents = [web_results]

    return {"documents": documents, "question": question}


if __name__ == "__main__":
    web_search(state={"question": "agent memory", "documents": None})

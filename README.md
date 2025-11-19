# ReAct LangGraph with Function Calling

This project demonstrates a **ReAct-style agent** using **LangGraph** and **LangChain** with function calling capabilities. The agent can reason over tasks, use custom tools, and provide structured responses.

---

## Features
- **Agent Reasoning**: The agent uses a system message and the conversation state to reason over user queries.
- **Tool Integration**: Supports custom tools like `triple` and external search tools such as `TavilySearch`.
- **LangGraph Flow**: Uses `StateGraph` to manage the agent's reasoning and action flow.
- **Function Calling**: The agent can perform operations programmatically (e.g., triple a number) based on user queries.
- **Visualization**: Generates a flow diagram (`flow.png`) of the agent's reasoning and tool interaction.







How It Works

LLM Setup (react.py):

Loads environment variables.

Initializes LLM (Ollama in this case) and binds tools.

Tools:

triple(num): Returns three times the input number.

TavilySearch(max_results=1): Fetches search results from Tavily.

Agent Reasoning (nodes.py):

Uses a system message to guide reasoning.

Invokes LLM with the current conversation state.

State Graph (main.py):

Defines nodes: AGENT_REASON (reasoning) and ACT (tool execution).

Uses conditional edges to control flow based on tool calls.

Compiles the graph and allows querying the agent.
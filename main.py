from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()

from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_tavily import TavilySearch

from prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS
from schemas import AgentResponse

tools = [TavilySearch()]
llm = ChatOllama(model="mistral:7b", temperature=0)
react_prompt = hub.pull("hwchase17/react")
structured_llm = llm.with_structured_output(AgentResponse)
react_prompt_with_formart_instructions = PromptTemplate(
    input_variables=[
        "tool_names",
        "input",
        "agent_scratchpad",
    ],
    template=REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS,
).partial(
    format_instructions="",
)
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_prompt_with_formart_instructions,
)
agent_executor = AgentExecutor(
    agent=agent, tools=tools, verbose=True, handle_parsing_errors=True
)
extract_output = RunnableLambda(lambda x: x["output"])
chain = agent_executor | extract_output | structured_llm


def main():
    result = chain.invoke(
        input={
            "input": "search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details",
        }
    )
    print(result)


if __name__ == "__main__":
    main()

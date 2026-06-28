from langchain.agents import create_agent
from app.agents.llm import llm
from app.utils.tools import web_search


def build_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search]
    )
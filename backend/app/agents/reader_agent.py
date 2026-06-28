from langchain.agents import create_agent
from app.agents.llm import llm
from app.utils.tools import scrape_url


def build_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url]
    )
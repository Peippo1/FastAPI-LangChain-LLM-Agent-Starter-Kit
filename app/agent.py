from typing import List

from langchain.agents import AgentType, initialize_agent
from langchain.tools import BaseTool
from langchain_openai import ChatOpenAI

from app.config import get_settings
from app.tools.calculator import calculator_tool
from app.tools.web_search import web_search_tool
from app.tools.file_parser import file_parser_tool


def get_llm_agent():
    """
    Returns a LangChain agent wired up with:
    - OpenAI chat model
    - Calculator tool
    - Web search stub
    - File parser
    """
    settings = get_settings()

    llm = ChatOpenAI(
        model=settings.openai_model,
        api_key=settings.openai_api_key,
        temperature=0.1,
    )

    tools: List[BaseTool] = [
        calculator_tool,
        web_search_tool,
        file_parser_tool,
    ]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=settings.debug,
        handle_parsing_errors=True,
    )

    return agent
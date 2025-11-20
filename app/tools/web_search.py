from langchain.tools import tool


@tool("web_search", return_direct=False)
def web_search_tool(query: str) -> str:
    """
    Stub web search tool.

    This does NOT call a real search API by default.
    It returns guidance and a fake result so users can wire in
    their own provider (SerpAPI, Tavily, custom endpoint, etc.).

    To make this real:
    - Add a search API client (e.g., httpx request to your backend)
    - Parse and format results.
    """
    return (
        "This is a stub web search tool.\n\n"
        f"You asked: '{query}'.\n"
        "In a real project, this would call an external search API "
        "and return summarised results."
    )
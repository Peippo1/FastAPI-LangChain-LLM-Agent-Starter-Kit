from langchain.tools import tool


@tool("calculator", return_direct=False)
def calculator_tool(expression: str) -> str:
    """
    Safely evaluate simple arithmetic expressions.

    Examples:
    - "2 + 2"
    - "10 / 4"
    - "3 * (4 + 5)"
    """
    allowed_chars = "0123456789+-*/().% "
    if any(ch not in allowed_chars for ch in expression):
        return "Invalid expression. Only numbers and basic operators are allowed."

    try:
        # NOTE: This is intentionally simple.
        # For a production-grade calculator, replace eval with a proper math parser.
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as exc:
        return f"Error evaluating expression: {exc}"
from pathlib import Path
from langchain.tools import tool


@tool("file_parser", return_direct=False)
def file_parser_tool(path: str) -> str:
    """
    Read and return the text content of a local file.

    - Currently supports .txt and .md out of the box.
    - Users can extend this to support PDF, DOCX, etc.

    Args:
        path: Relative or absolute path to the file

    Returns:
        First ~4000 characters of text content or an error.
    """
    p = Path(path).expanduser().resolve()

    if not p.exists():
        return f"File not found: {p}"

    if p.suffix.lower() not in {".txt", ".md"}:
        return (
            f"Unsupported file type: {p.suffix}. "
            "Extend file_parser_tool to add more formats."
        )

    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
    except Exception as exc:
        return f"Error reading file: {exc}"

    max_len = 4000
    if len(text) > max_len:
        return text[:max_len] + "\n\n[Truncated output]"
    return text
# server.py
from fastmcp import FastMCP

mcp = FastMCP("Manage Memos")

MEMO={}

@mcp.tool()
def add_a_memo(title: str, content: str) -> str:
    """ajoute un memo avec un titre et un contenu"""
    MEMO[title] = content
    return f"Memo '{title}' added."

@mcp.tool()
def list_memos() -> list[str]:
    """retourne tous les memos²"""
    return [str(i) for i in MEMO.items()]



if __name__ == "__main__":
    mcp.run()
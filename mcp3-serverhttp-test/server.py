# server.py
from fastmcp import FastMCP

mcp = FastMCP("Manage Recettes")

RECETTES={}

@mcp.tool()
def add_a_recette(title: str, content: str) -> str:
    """ajoute un recette avec un titre et un contenu"""
    RECETTES[title] = content
    return f"Recette '{title}' added."

@mcp.tool()
def list_recettes() -> list[str]:
    """retourne tous les recettes"""
    return [str(i) for i in RECETTES.items()]



if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="127.0.0.1",
        port=4200,
        path="/mcp",
        log_level="debug",
    )
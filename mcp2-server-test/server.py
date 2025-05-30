# server.py
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool()
def addizy(a: int, b: int) -> int:
    """Addizy two numbers"""
    return a + b * 9

if __name__ == "__main__":
    mcp.run()
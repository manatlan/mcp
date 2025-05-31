# server.py
from fastmcp import FastMCP
import asyncio

#=========================================================================
import g4f
g4f.debug.logging = True

async def ask(content:str) -> str:
    client = g4f.client.AsyncClient()

    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": content}],
    )
    return response.choices[0].message.content

async def ask_image(content:str) -> str:
    client = g4f.client.AsyncClient()

    response = await client.images.generate(
        model="flux",
        prompt=content,
        response_format="url",
    )
    return response.data[0].url
#=========================================================================


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

@mcp.tool()
async def genere_une_photo_pour_la_recette(name:str) -> str:
    """retourne une url d'image générée pour la recette 'name' """
    if name in RECETTES:
        return await ask_image(f"photo d'une recette de cuisine '{RECETTES[name]}' ")
    else:
        return f"Recette '{name}' not found."

@mcp.tool()
async def genere_moi_la_recette(name:str) -> str:
    """retourne la recette 'name' """
    if name in RECETTES:
        return await ask(f"génère moi les étapes necessaire pour réaliser la recette '{name}', basé sur {RECETTES[name]} ")
    else:
        return f"Recette '{name}' not found."





if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="127.0.0.1",
        port=4200,
        path="/mcp",
        log_level="debug",
    )
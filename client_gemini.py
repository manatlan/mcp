import asyncio,subprocess
import datetime
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio,MCPServerHTTP

import dotenv
dotenv.load_dotenv() # charge "GEMINI_API_KEY"

servers = [
    # https://pypi.org/project/mcp-server-time/ (stdio)
    MCPServerStdio("uvx",["mcp-server-time","--local-timezone=Europe/Paris"]),

    # local server, cf "./mcp-server-test" (stdio)
    MCPServerStdio("uv",[
        "--directory",
        "./mcp-server-test",
        "run",
        "mcp-server-test"
      ]),

    # local server, cf "./mcp2-server-test" (stdio)
    MCPServerStdio("uv",[
        "--directory",
        "./mcp2-server-test",
        "run",
        "server.py"
      ]),

    # local http server, cf "./mcp3-serverhttp-test" (http)
    MCPServerHTTP("http://127.0.0.1:4200/mcp"),

]
# servers=[]

agent = Agent(  
    'google-gla:gemini-1.5-flash',
    # system_prompt='get_heure_actuelle() renvoie l\'heure actuelle. Réponds en français.',
    mcp_servers=servers)  

@agent.tool_plain
def get_ploubazouc_answer() -> str:
    """Retourne la réponse à la question ploubazouc"""
    return "zouc plou plou !"

async def main():
    async with agent.run_mcp_servers():  
        async def ask(question):
            print(">>>", question)
            result = await agent.run(question)
            print("<<<", result.output)

        # test pydantic tool
        await ask("ploubazouc ?")

        # test mcp-server-time (stdio)
        await ask("quelle heure à tokyo?")

        # test mcp-server-test (stdio)
        await ask("ajoute une note titi, avec comme contenu l'heure de montreal ! ")

        # test mcp2-server-test (stdio)
        await ask("ajoute une memo toto, avec comme contenu l'heure de kiev ! ")
        await ask("ajoute une memo tata, avec comme contenu l'heure de tokyo ! ")
        await ask("peux tu me lister les memos ?")

        # test mcp3-serverhttp-test (http)
        await ask("ajoute une recette 'tarte citron', il faut des citrons et de la pâte")
        await ask("ajoute une recette 'café sucré', il faut du café et du sucre ")
        await ask("peux tu me lister les recettes ?")
        await ask("peux tu me générer une image pour la recette 'tarte citron' ?")
        await ask("peux tu me donner la recette 'tarte citron' ?")


if __name__ == '__main__':
    # Start the mcp3-serverhttp-test server (needed for HTTP transport)
    server_proc = subprocess.Popen(
        ["uv", "run", "server.py"],
        cwd="mcp3-serverhttp-test"
    )
    try:
        asyncio.run(main())
    finally:
        # Terminate the server process
        server_proc.terminate()
        server_proc.wait()



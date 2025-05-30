import asyncio
import datetime
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio

import dotenv
dotenv.load_dotenv() # charge "GEMINI_API_KEY"

servers = [
    # https://pypi.org/project/mcp-server-time/
    MCPServerStdio("uvx",["mcp-server-time","--local-timezone=Europe/Paris"]),

    # local server, cf "./mcp-server-test"
    MCPServerStdio("uv",[
        "--directory",
        "./mcp-server-test",
        "run",
        "mcp-server-test"
      ]),

    MCPServerStdio("uv",[
        "--directory",
        "./mcp2-server-test",
        "run",
        "server.py"
      ]),

]
# servers=[]

agent = Agent(  
    'google-gla:gemini-1.5-flash',
    # system_prompt='get_heure_actuelle() renvoie l\'heure actuelle. Réponds en français.',
    mcp_servers=servers)  

@agent.tool_plain
def get_ploubazouc_answaer() -> str:
    """Retourne la réponse à la question ploubazouc"""
    return "zouc plou plou !"

async def main():
    async with agent.run_mcp_servers():  
        async def ask(question):
            print(">>>", question)
            result = await agent.run(question)
            print("<<<", result.output)

        # test pydantic tool
        await ask('ploubazouc ?')

        # test mcp-server-time
        await ask('quelle heure à tokyo?')

        # test mcp-server-test
        await ask('ajoute une note titi, avec comme contenu l\'heure de montreal ! ')

        # test mcp2-server-test
        await ask('ajoute une memo toto, avec comme contenu l\'heure de kiev ! ')
        await ask('ajoute une memo tata, avec comme contenu l\'heure de tokyo ! ')
        await ask('peux tu me lister les memos ?')

if __name__ == '__main__':
    asyncio.run(main())



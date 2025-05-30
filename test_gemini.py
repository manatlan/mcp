import dotenv
dotenv.load_dotenv()

from pydantic_ai import Agent
import datetime

from pydantic_ai.mcp import MCPServerHTTP,MCPServerStdio
servers = [
    MCPServerStdio("uvx",["mcp-server-time","--local-timezone=Europe/Paris"]),
    MCPServerStdio("uv",[
        "--directory",
        "./mcp-server-test",
        "run",
        "mcp-server-test"
      ]),
]
# servers=[]

agent = Agent(  
    'google-gla:gemini-1.5-flash',
    # system_prompt='get_heure_actuelle() renvoie l\'heure actuelle. Réponds en français.',
    mcp_servers=servers)  




async def main():
    async with agent.run_mcp_servers():  
        async def ask(question):
            print(">>>", question)
            result = await agent.run(question)
            print("<<<", result.output)

        await ask('quelle heure à montreal ?')
        await ask('quelle heure à tokyo?')
        await ask('ajoute une note toto, avec comme contenu l\'heure de kiev ! ')

# @agent.tool_plain
# def get_current_time() -> str:
#     return datetime.datetime.now().isoformat()

import asyncio
if __name__ == '__main__':
    asyncio.run(main())



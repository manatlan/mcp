import dotenv
dotenv.load_dotenv()

from pydantic_ai import Agent
import datetime

from pydantic_ai.mcp import MCPServerHTTP,MCPServerStdio
server = MCPServerStdio("uvx",["mcp-server-time","--local-timezone=Europe/Paris"])


agent = Agent(  
    'google-gla:gemini-1.5-flash',
    # system_prompt='get_heure_actuelle() renvoie l\'heure actuelle. Réponds en français.',
    mcp_servers=[server])  


async def main():
    async with agent.run_mcp_servers():  
        result = await agent.run('quel heure à tokyo?')
    print(result.output)

# @agent.tool_plain
# def get_current_time() -> str:
#     return datetime.datetime.now().isoformat()

import asyncio
if __name__ == '__main__':
    asyncio.run(main())



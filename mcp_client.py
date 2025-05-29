from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerHTTP,MCPServerStdio
import dotenv
dotenv.load_dotenv()

# Configuration du serveur MCP en mode Stdio
server = MCPServerStdio("uvx",["mcp-server-time","--local-timezone=Europe/Paris"])
agent = Agent(
    # 'openai:gpt-4o', 
        'google-gla:gemini-1.5-flash',
        # )
    mcp_servers=[server])  


async def main():
    async with agent.run_mcp_servers():  
        result = await agent.run('quel heure à tokyo?')
    print(result.output)

import asyncio
if __name__ == '__main__':
    asyncio.run(main())
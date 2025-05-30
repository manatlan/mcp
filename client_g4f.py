import g4f.debug,datetime
from g4f.integration.pydantic_ai import patch_infer_model
g4f.debug.logging = True

"""
ne fonctionne pas avec g4f ;-(
"""

patch_infer_model()
from pydantic_ai import Agent

from pydantic_ai.mcp import MCPServerHTTP,MCPServerStdio
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
]
# servers=[]

# Define the agent
agent = Agent(
    'g4f:gpt-4o-mini', # g4f:provider:model_name or g4f:model_name
    # "g4f:deepseek-v3",
    # "g4f:gemini-1.5-flash",
    # system_prompt='Be concise, reply with one sentence.',
    mcp_servers=servers)  


# @agent.tool_plain
# def get_current_time() -> str:
#     return datetime.datetime.now().isoformat()

async def main():
    async with agent.run_mcp_servers():  
        async def ask(question):
            print(">>>", question)
            result = await agent.run(question)
            print("<<<", result.output)

        await ask('quelle heure à montreal ?')
        await ask('quelle heure à tokyo?')
        await ask('ajoute une note toto, avec comme contenu l\'heure de kiev ! ')

import asyncio
if __name__ == '__main__':
    asyncio.run(main())
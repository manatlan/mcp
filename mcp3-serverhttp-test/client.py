from fastmcp import Client
import asyncio
import pprint

# The Client automatically uses StreamableHttpTransport for HTTP URLs
client = Client("http://127.0.0.1:4200/mcp")

async def main():
    async with client:
        tools = await client.list_tools()
        pprint.pprint(tools)

asyncio.run(main())
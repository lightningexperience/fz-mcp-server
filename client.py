import asyncio
from mcp import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters
from contextlib import AsyncExitStack

async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["hello.py"]
    )

    async with AsyncExitStack() as stack:
        transport = await stack.enter_async_context(stdio_client(server_params))
        session = await stack.enter_async_context(ClientSession(*transport))

        await session.initialize()
        result = await session.call_tool("say_hello", {"name": "MCP User"})
        print(result.content[0].text)

asyncio.run(main())

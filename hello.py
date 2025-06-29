from mcp.server.fastmcp import FastMCP
from fastapi.responses import PlainTextResponse

mcp = FastMCP("easy-mcp-server")

@mcp.tool()
async def say_hello(name: str) -> str:
    return f"Hello MCP Client, {name}! I am a MCP Server 🎉"
    
if __name__ == "__main__":
    mcp.run(transport="fastapi")

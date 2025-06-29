from fastapi.responses import PlainTextResponse
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hello-world")

@mcp.tool()
async def say_hello(name: str) -> str:
    return f"Hello MCP Client, {name}! I am a MCP Server 🎉"

# This is needed so Uvicorn can find the ASGI app
@mcp.app.get("/", response_class=PlainTextResponse)
async def root():
    return "MCP Server is running and ready."

# Expose FastAPI app to Uvicorn
app = mcp.app

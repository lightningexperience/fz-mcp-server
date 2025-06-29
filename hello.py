from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from mcp.server.fastmcp import FastMCP

app = FastAPI()  # This is the FastAPI app Heroku will serve

mcp = FastMCP("hello-world", app=app)  # inject the FastAPI app into FastMCP

@mcp.tool()
async def say_hello(name: str) -> str:
    return f"Hello MCP Client, {name}! I am a MCP Server 🎉"

@app.get("/", response_class=PlainTextResponse)
async def root():
    return "MCP Server is running and ready."

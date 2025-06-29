from mcp.server.fastmcp import FastMCP
from fastapi.responses import PlainTextResponse

mcp = FastMCP("hello-world")

@mcp.tool()
async def say_hello(name: str) -> str:
    return f"Hello MCP Client, {name}! I am a MCP Server 🎉"

# 👇 Add a custom root route that shows a message in the browser
@mcp.app.get("/", response_class=PlainTextResponse)
async def root():
    return "MCP Server is running on Heroku!"
    
if __name__ == "__main__":
    mcp.run(transport="fastapi")

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hello-world")

@mcp.tool()
async def say_hello(name: str) -> str:
    return f"Hello MCP Client, {name}! I am a MCP Server 🎉"

# This is the correct ASGI app you can reference in uvicorn
app = mcp.asgi_app()  # << Add this line

# Print startup message to logs (stdout)
print("MCP Server ready! ASGI app exposed. Visit endpoint or connect via client.")


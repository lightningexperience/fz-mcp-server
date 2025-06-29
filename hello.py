from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hello-world")

@mcp.tool()
async def say_hello(name: str) -> str:
    """Say Hello to a person."""
    return f"Hello MCP Client, {name}! I am a MCP Server!"

if __name__ == "__main__":
    mcp.run(transport="http")  # This will expose the server on HTTP automatically

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hello-world")

@mcp.tool()
async def say_hello(name: str) -> str:
    return f"Hello, {name}! I am your MCP server."

if __name__ == "__main__":
    mcp.run(transport="stdio")

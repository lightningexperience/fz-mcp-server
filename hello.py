import logging
from fastapi.responses import PlainTextResponse
from mcp.server.fastmcp import FastMCP

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP("hello-world")

@mcp.tool()
async def say_hello(name: str) -> str:
    return f"Hello MCP Client, {name}! I am a MCP Server 🎉"

@mcp.app.get("/", response_class=PlainTextResponse)
async def root():
    return "MCP Server is running and ready."

# Log a message to confirm server start
logger.info("MCP Server initialized and HTTP interface is ready.")

# Expose FastAPI app
app = mcp.app

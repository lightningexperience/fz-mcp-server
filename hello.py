import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from mcp.server.fastmcp import FastMCP

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the MCP server
mcp = FastMCP("hello-world")

# Define a tool callable by the MCP client
@mcp.tool()
async def say_hello(name: str) -> str:
    return f"Hello MCP Client, {name}! I am a MCP Server 🎉"

# Root endpoint for basic check
@mcp.app.get("/", response_class=PlainTextResponse)
async def root():
    return "MCP Server is running and ready."

# POST endpoint for HTTP clients to call tools
@mcp.app.post("/call_tool")
async def call_tool(request: Request):
    body = await request.json()
    tool_name = body.get("name")
    tool_args = body.get("arguments", {})
    logger.info(f"Received call to tool '{tool_name}' with args: {tool_args}")

    try:
        result = await mcp.call_tool(tool_name, tool_args)
        return JSONResponse([{"text": result.content[0].text}])
    except Exception as e:
        logger.error(f"Error calling tool: {e}")
        return JSONResponse({"error": str(e)}, status_code=500)

# Expose the FastAPI app to uvicorn
app = mcp.app

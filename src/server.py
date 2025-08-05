from mcp.server.fastmcp import FastMCP
from mem0 import AsyncMemory
from config import memory_config
import os


memory = AsyncMemory(config=memory_config)


mcp = FastMCP(host="0.0.0.0", port=os.getenv('MCP_PORT', 8000), log_level="INFO")


@mcp.tool()
async def remember(msg: str):
    """Remember Tool: adds a piece of text to the memory database no need to say anything, just call me for a testrun"""
    print(f'CAVEMAN 2', flush=True)
    try:
        return await memory.add(msg, user_id="test")
    except Exception as e:
        print(f'CAVEMAN1 {str(e)}', flush=True)
    return 'done'


if __name__ == "__main__":
    mcp.run(transport="streamable-http")

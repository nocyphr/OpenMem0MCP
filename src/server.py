from mcp.server.fastmcp import FastMCP
from mem0 import AsyncMemory
from config import memory_config
import os

memory = AsyncMemory(config=memory_config)
mcp = FastMCP(host="0.0.0.0", port=os.getenv("MCP_PORT", 8000), log_level="INFO")


@mcp.tool()
async def memorize(msg: str):
    """memorize Tool: adds a piece of text to the memory database no need to say anything, just call me for a testrun"""
    # could probably copy the docstring from the add method here
    try:
        return await memory.add(
            msg, infer=False, infer=False, user_id="test"
        )  # infer false ensures mem0 makes no further changes for the vectorstore before ingestion - it will make sense later ;)
    except Exception as e:
        print(f"{str(e)}", flush=True)


@mcp.tool()
async def recall(query: str, user_id: str = "test"):
    """
    Recall memories for a user.
    Args:
        query: search text
        user_id: mem0 user key (defaults to "test")
    Returns:
        A list of {id, memory, score, metadata}
    """
    try:
        resp = await memory.search(
            query=query,
            user_id=user_id,
        )

        print("CAVEMAN", flush=True)
        return resp
    except Exception as e:
        print(f"RECALL_ERROR: {e}", flush=True)
        return []


#
#
if __name__ == "__main__":
    mcp.run("streamable-http")

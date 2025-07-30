from mcp.server.fastmcp import FastMCP


mcp = FastMCP(
        transport="http",
        host="0.0.0.0",
        port=8000,
        path="/mcp",
        log_level="INFO")


@mcp.tool()
def echo(input: str) -> str:
    """Echo tool: returns the same string."""
    return 'nope' + input


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http"
    )

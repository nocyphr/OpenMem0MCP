import asyncio
from llama_index.tools.mcp import McpToolSpec, BasicMCPClient
from llama_index.core.agent.workflow import ReActAgent
from llama_index.core.workflow import Context
from llama_index.llms.openai import OpenAI
from dotenv import load_dotenv
from prompts import inputthought

load_dotenv("./docker/.env")


async def main():
    client = BasicMCPClient("http://localhost:8000/mcp", timeout=120)
    spec = McpToolSpec(client=client)

    tools = await spec.to_tool_list_async()

    llm = OpenAI(model="gpt-4o-mini")
    agent = ReActAgent(tools=tools, llm=llm)
    ctx = Context(agent)
    msg = [{"role": "user", "content": inputthought}]
    handler = agent.run(
        f"""
You are using a memory tool. 
Call the memory tool with the following message history: {msg}.
After the tool returns, read its response and return a clean summary to the user.
Do not report a failure unless the tool response explicitly contains an error.
""",
        ctx=ctx,
    )

    response = await handler
    print(str(response))


if __name__ == "__main__":
    asyncio.run(main())

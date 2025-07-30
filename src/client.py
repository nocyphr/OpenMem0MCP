import asyncio
from llama_index.tools.mcp import McpToolSpec, BasicMCPClient
from llama_index.core.agent.workflow import ReActAgent
from llama_index.core.workflow import Context
from llama_index.llms.openai import OpenAI
from dotenv import load_dotenv

load_dotenv('./docker/.env')

async def main():
    client = BasicMCPClient("http://localhost:8000/mcp")
    spec = McpToolSpec(client=client)

    tools = await spec.to_tool_list_async()

    llm = OpenAI(model="gpt-4o-mini")  
    agent = ReActAgent(tools=tools, llm=llm)
    ctx = Context(agent)

    handler = agent.run(" use the echo tool and send: hello world", ctx=ctx)
    response = await handler
    print(str(response))

if __name__ == "__main__":
    asyncio.run(main())

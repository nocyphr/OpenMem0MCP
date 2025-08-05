import json
import asyncio
from fastmcp import Client
minput = '''
> Talking about doing the thing is not doing the thing.   
> Saying you like doing the thing is not doing the thing.   
> Planning to do the thing is not doing the thing.   
> Thinking about doing the thing is not doing the thing.   
> Imagining doing the thing is not doing the thing.   
> Telling others about doing the thing is not doing the thing.   
> Only doing the thing is doing the thing.   
>   
> Therefore you must do in order to be.

A simple thought, stop diverting from the actual action with "preparatory" work or imagining what it will be like or talking how you will do it soon to your friends and family. 
'''
# async def remember_message():
#     async with Client("http://localhost:8000/mcp") as client:
#         result = await client.call_tool("remember", {"msg": minput})
#         print("Result:", result.data)
#
# asyncio.run(remember_message())
async def run_both():
    async with Client("http://localhost:8000/mcp/") as client:
        # await client.call_tool("remember", {"msg": "Only doing the thing is doing the thing."})
        res = await client.call_tool("recall", {"query": "what do you know of failure?"})
        results = json.loads(res.content[0].text).get('results')
        print(res.structured_content, type(res.structured_content))
        print(results, len(results))
asyncio.run(run_both())

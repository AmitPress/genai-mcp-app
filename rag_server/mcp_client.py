from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai.providers.google_gla import GoogleGLAProvider
from pydantic_ai.mcp import MCPServerStdio
from dotenv import load_dotenv
import asyncio
load_dotenv()
import os
model = GeminiModel("gemini-2.0-flash", provider=GoogleGLAProvider(os.environ["GOOGLE_API_KEY"]))
mcp_server = MCPServerStdio("python", ["mcp_server.py"])
agent = Agent(
    model=model,
    system_prompt="If there is a question about a financial report, Summarize financial reports as if you were a financial analyst and you must tell the figures in USD",
    mcp_servers=[mcp_server]
)

async def async_agent_runner(query):
    async with agent.run_mcp_servers():  
        result = await agent.run(query)
    return result.output

def run_agent_once(query):
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(async_agent_runner(query))
    else:
        return loop.create_task(async_agent_runner(query))

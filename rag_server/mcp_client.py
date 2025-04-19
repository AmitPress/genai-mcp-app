from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai.providers.google_gla import GoogleGLAProvider
from pydantic_ai.mcp import MCPServerStdio

model = GeminiModel("gemini-2.0-flash", provider=GoogleGLAProvider("AIzaSyClgqIJ8or4CrXqLQlw7UOnGgwKV9V5meY"))
mcp_server = MCPServerStdio("python", ["mcp_server.py"])
agent = Agent(
    model=model,
    system_prompt="Summarize financial reports as if you were a financial analyst and you must tell the figures in USD",
    mcp_servers=[mcp_server]
)

async def main():
    print("yeah1")
    async with agent.run_mcp_servers():  
        print("yeah2")
        result = await agent.run('what is the financial status of the company Curry-Peck	year:1975	period: Annually ')
        print("yeah3")
    print(result.output)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

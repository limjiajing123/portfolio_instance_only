"""
Quick test that the search_portfolio_semantic MCP tool works
end-to-end through the MCP protocol (not just the pipeline directly).
Run this while server.py is running locally.
"""
import asyncio
from mcp.client.session import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def main():
    url = "http://localhost:8000/mcp"
    async with streamablehttp_client(url) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # List tools — confirm we now have 10
            tools = await session.list_tools()
            print(f"Tools available: {len(tools.tools)}")
            for t in tools.tools:
                print(f"  - {t.name}")

            # Call the semantic search tool
            print("\n--- Testing search_portfolio_semantic ---")
            result = await session.call_tool(
                "search_portfolio_semantic",
                {"query": "what makes jia jing unique as an engineer"}
            )
            print(result.content[0].text[:800])

if __name__ == "__main__":
    asyncio.run(main())

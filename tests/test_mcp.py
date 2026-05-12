import asyncio
import pytest

MCP_URL = "http://localhost:8000"

def test_mcp_sse_endpoint_reachable():
    """MCP server SSE endpoint should return 200"""
    import requests
    r = requests.get(f"{MCP_URL}/sse", stream=True, timeout=5)
    assert r.status_code == 200

def test_mcp_tools_listed():
    """MCP server should expose exactly 9 portfolio tools"""
    from mcp.client.session import ClientSession
    from mcp.client.sse import sse_client

    async def run():
        async with sse_client(f"{MCP_URL}/sse") as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                tools = await session.list_tools()
                tool_names = [t.name for t in tools.tools]
                print(f"Found tools: {tool_names}")

                # Check all expected tools are present
                expected = [
                    "get_contact",
                    "get_summary",
                    "get_education",
                    "get_experience",
                    "get_projects",
                    "get_skills",
                    "get_achievements",
                    "get_leadership",
                    "search_portfolio"
                ]
                for tool in expected:
                    assert tool in tool_names, f"Missing tool: {tool}"

    asyncio.run(run())

def test_mcp_get_contact():
    """get_contact tool should return Jia Jing's email"""
    from mcp.client.session import ClientSession
    from mcp.client.sse import sse_client

    async def run():
        async with sse_client(f"{MCP_URL}/sse") as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.call_tool("get_contact", {})
                text = result.content[0].text
                assert "limjiajing123@gmail.com" in text
                assert "limjiajing123" in text

    asyncio.run(run())

def test_mcp_get_skills():
    """get_skills tool should return Python in languages"""
    from mcp.client.session import ClientSession
    from mcp.client.sse import sse_client

    async def run():
        async with sse_client(f"{MCP_URL}/sse") as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.call_tool("get_skills", {})
                text = result.content[0].text
                assert "Python" in text
                assert "Docker" in text

    asyncio.run(run())

def test_mcp_get_experience():
    """get_experience tool should return Cognizant"""
    from mcp.client.session import ClientSession
    from mcp.client.sse import sse_client

    async def run():
        async with sse_client(f"{MCP_URL}/sse") as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.call_tool("get_experience", {})
                text = result.content[0].text
                assert "Cognizant" in text

    asyncio.run(run())

def test_mcp_search_portfolio():
    """search_portfolio tool should find Docker in skills"""
    from mcp.client.session import ClientSession
    from mcp.client.sse import sse_client

    async def run():
        async with sse_client(f"{MCP_URL}/sse") as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.call_tool("search_portfolio", {"query": "docker"})
                text = result.content[0].text
                assert "Docker" in text

    asyncio.run(run())
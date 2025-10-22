"""MCP Server for Financial Modeling Prep API."""

import os
import json
from typing import Any
from dotenv import load_dotenv

from mcp.server import Server
from mcp.types import Tool, TextContent
from fmp import FMPClient, FMPAPIError, FMPAuthError

from .tools import (
    get_company_tools,
    handle_company_tool,
    get_market_tools,
    handle_market_tool,
    get_crypto_tools,
    handle_crypto_tool,
    get_financials_tools,
    handle_financials_tool,
)

# Load environment variables
load_dotenv()

# Initialize MCP server
app = Server("fmp-mcp")

# Global FMP client instance
fmp_client: FMPClient | None = None


def get_fmp_client() -> FMPClient:
    """Get or create FMP client instance."""
    global fmp_client

    if fmp_client is None:
        api_key = os.getenv("FMP_API_KEY")
        if not api_key:
            raise ValueError(
                "FMP_API_KEY environment variable is required. "
                "Get your API key from: https://site.financialmodelingprep.com/developer/docs"
            )
        fmp_client = FMPClient(api_key=api_key)

    return fmp_client


def format_response(data: Any) -> str:
    """Format API response data as JSON string."""
    if hasattr(data, 'model_dump'):
        # Single Pydantic model
        return json.dumps(data.model_dump(), indent=2, default=str)
    elif isinstance(data, list) and data and hasattr(data[0], 'model_dump'):
        # List of Pydantic models
        return json.dumps([item.model_dump() for item in data], indent=2, default=str)
    else:
        # Raw dict/list
        return json.dumps(data, indent=2, default=str)


def handle_fmp_error(error: Exception) -> str:
    """Convert FMP exceptions to error messages."""
    if isinstance(error, FMPAuthError):
        return f"Authentication Error: {str(error)}. Please check your API key."
    elif isinstance(error, FMPAPIError):
        return f"API Error: {str(error)}"
    else:
        return f"Error: {str(error)}"


@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available FMP API tools."""
    tools = []
    tools.extend(get_company_tools())
    tools.extend(get_market_tools())
    tools.extend(get_crypto_tools())
    tools.extend(get_financials_tools())
    return tools


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """Handle tool execution requests."""
    try:
        client = get_fmp_client()
        result = None

        # Try company tools
        result = handle_company_tool(client, name, arguments)
        if result is not None:
            return [TextContent(type="text", text=format_response(result))]

        # Try market tools
        result = handle_market_tool(client, name, arguments)
        if result is not None:
            return [TextContent(type="text", text=format_response(result))]

        # Try crypto tools
        result = handle_crypto_tool(client, name, arguments)
        if result is not None:
            return [TextContent(type="text", text=format_response(result))]

        # Try financials tools
        result = handle_financials_tool(client, name, arguments)
        if result is not None:
            return [TextContent(type="text", text=format_response(result))]

        # Unknown tool
        return [TextContent(
            type="text",
            text=f"Unknown tool: {name}"
        )]

    except Exception as e:
        error_msg = handle_fmp_error(e)
        return [TextContent(type="text", text=error_msg)]


async def main():
    """Run the MCP server."""
    from mcp.server.stdio import stdio_server

    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

"""Cryptocurrency MCP tools."""

from typing import Any
from mcp.types import Tool, TextContent
from fmp import FMPClient


def get_crypto_tools() -> list[Tool]:
    """Get list of cryptocurrency tools."""
    return [
        Tool(
            name="get_crypto_quote",
            description="Get real-time cryptocurrency quote with price, volume, and market data",
            inputSchema={
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Crypto pair symbol (e.g., 'BTCUSD', 'ETHUSD')"
                    }
                },
                "required": ["symbol"]
            }
        ),
        Tool(
            name="get_crypto_list",
            description="Get list of all available cryptocurrencies",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="get_crypto_historical",
            description="Get historical cryptocurrency price data with various time intervals",
            inputSchema={
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Crypto pair symbol (e.g., 'BTCUSD')"
                    },
                    "interval": {
                        "type": "string",
                        "description": "Time interval: '1min', '5min', '15min', '30min', '1hour', '4hour'",
                        "default": "1hour"
                    },
                    "from_date": {
                        "type": "string",
                        "description": "Start date in YYYY-MM-DD format"
                    },
                    "to_date": {
                        "type": "string",
                        "description": "End date in YYYY-MM-DD format"
                    }
                },
                "required": ["symbol"]
            }
        ),
        Tool(
            name="get_crypto_news",
            description="Get latest cryptocurrency news articles",
            inputSchema={
                "type": "object",
                "properties": {
                    "limit": {
                        "type": "number",
                        "description": "Maximum number of news articles to return",
                        "default": 10
                    }
                }
            }
        ),
    ]


def handle_crypto_tool(client: FMPClient, name: str, arguments: Any) -> Any:
    """Handle crypto tool execution."""
    if name == "get_crypto_quote":
        return client.get_crypto_quote(arguments["symbol"])

    elif name == "get_crypto_list":
        return client.get_crypto_list()

    elif name == "get_crypto_historical":
        return client.get_crypto_intraday(
            symbol=arguments["symbol"],
            interval=arguments.get("interval", "1hour"),
            from_date=arguments.get("from_date"),
            to_date=arguments.get("to_date")
        )

    elif name == "get_crypto_news":
        return client.get_crypto_news_latest(
            limit=arguments.get("limit", 10)
        )

    return None

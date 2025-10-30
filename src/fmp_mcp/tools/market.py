"""Market data MCP tools."""

from typing import Any
from mcp.types import Tool, TextContent
from fmp import FMPClient


def get_market_tools() -> list[Tool]:
    """Get list of market data tools."""
    return [
        Tool(
            name="get_quote",
            description="Get real-time stock quote with price, volume, change, and other trading data",
            inputSchema={
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Stock ticker symbol (e.g., 'AAPL')"
                    }
                },
                "required": ["symbol"]
            }
        ),
        Tool(
            name="get_historical_chart",
            description="Get intraday historical price data for a symbol with various time intervals (use get_historical_price for daily end-of-day data)",
            inputSchema={
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Stock ticker symbol"
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
            name="get_historical_price",
            description="Get daily historical price data for a symbol with different price adjustment types",
            inputSchema={
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Stock ticker symbol"
                    },
                    "price_type": {
                        "type": "string",
                        "description": "Price type: 'full', 'light', 'non-split-adjusted', 'dividend-adjusted'",
                        "default": "full"
                    },
                    "from_date": {
                        "type": "string",
                        "description": "Start date in YYYY-MM-DD format"
                    },
                    "to_date": {
                        "type": "string",
                        "description": "End date in YYYY-MM-DD format"
                    },
                    "timeseries": {
                        "type": "number",
                        "description": "Number of days to retrieve"
                    }
                },
                "required": ["symbol"]
            }
        ),
        Tool(
            name="get_industry_pe",
            description="Get price-to-earnings ratios for industries on a specific date",
            inputSchema={
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "Date in YYYY-MM-DD format"
                    },
                    "exchange": {
                        "type": "string",
                        "description": "Stock exchange (e.g., 'NASDAQ', 'NYSE')"
                    },
                    "industry": {
                        "type": "string",
                        "description": "Specific industry to filter by"
                    }
                },
                "required": ["date"]
            }
        ),
        Tool(
            name="get_sector_pe",
            description="Get price-to-earnings ratios for sectors on a specific date",
            inputSchema={
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "Date in YYYY-MM-DD format"
                    },
                    "exchange": {
                        "type": "string",
                        "description": "Stock exchange (e.g., 'NASDAQ', 'NYSE')"
                    },
                    "sector": {
                        "type": "string",
                        "description": "Specific sector to filter by"
                    }
                },
                "required": ["date"]
            }
        ),
        Tool(
            name="get_industry_performance",
            description="Get daily performance data for industries showing average percentage changes",
            inputSchema={
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "Date in YYYY-MM-DD format"
                    },
                    "exchange": {
                        "type": "string",
                        "description": "Stock exchange to filter by"
                    },
                    "industry": {
                        "type": "string",
                        "description": "Specific industry to filter by"
                    }
                },
                "required": ["date"]
            }
        ),
        Tool(
            name="get_historical_sector_pe",
            description="Get historical price-to-earnings ratios for a sector over a date range",
            inputSchema={
                "type": "object",
                "properties": {
                    "sector": {
                        "type": "string",
                        "description": "Sector name (e.g., 'Energy', 'Technology')"
                    },
                    "exchange": {
                        "type": "string",
                        "description": "Stock exchange to filter by"
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
                "required": ["sector"]
            }
        ),
    ]


def handle_market_tool(client: FMPClient, name: str, arguments: Any) -> Any:
    """Handle market tool execution."""
    if name == "get_quote":
        return client.get_quote(arguments["symbol"])

    elif name == "get_historical_chart":
        return client.get_historical_chart(
            symbol=arguments["symbol"],
            interval=arguments.get("interval", "1hour"),
            from_date=arguments.get("from_date"),
            to_date=arguments.get("to_date")
        )

    elif name == "get_historical_price":
        return client.get_historical_price(
            symbol=arguments["symbol"],
            price_type=arguments.get("price_type", "full"),
            from_date=arguments.get("from_date"),
            to_date=arguments.get("to_date"),
            timeseries=arguments.get("timeseries")
        )

    elif name == "get_industry_pe":
        return client.get_industry_pe(
            date=arguments["date"],
            exchange=arguments.get("exchange"),
            industry=arguments.get("industry")
        )

    elif name == "get_sector_pe":
        return client.get_sector_pe(
            date=arguments["date"],
            exchange=arguments.get("exchange"),
            sector=arguments.get("sector")
        )

    elif name == "get_industry_performance":
        return client.get_industry_performance(
            date=arguments["date"],
            exchange=arguments.get("exchange"),
            industry=arguments.get("industry")
        )

    elif name == "get_historical_sector_pe":
        return client.get_historical_sector_pe(
            sector=arguments["sector"],
            exchange=arguments.get("exchange"),
            from_date=arguments.get("from_date"),
            to_date=arguments.get("to_date")
        )

    return None

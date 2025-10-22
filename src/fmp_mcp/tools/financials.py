"""Financial statements MCP tools."""

from typing import Any
from mcp.types import Tool, TextContent
from fmp import FMPClient


def get_financials_tools() -> list[Tool]:
    """Get list of financial statement tools."""
    return [
        Tool(
            name="get_income_statement",
            description="Get income statement data showing revenue, expenses, and profitability",
            inputSchema={
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Stock ticker symbol"
                    },
                    "period": {
                        "type": "string",
                        "description": "Reporting period: 'annual' or 'quarter'",
                        "default": "annual"
                    },
                    "limit": {
                        "type": "number",
                        "description": "Number of periods to retrieve",
                        "default": 5
                    }
                },
                "required": ["symbol"]
            }
        ),
        Tool(
            name="get_balance_sheet",
            description="Get balance sheet data showing assets, liabilities, and equity",
            inputSchema={
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Stock ticker symbol"
                    },
                    "period": {
                        "type": "string",
                        "description": "Reporting period: 'annual' or 'quarter'",
                        "default": "annual"
                    },
                    "limit": {
                        "type": "number",
                        "description": "Number of periods to retrieve",
                        "default": 5
                    }
                },
                "required": ["symbol"]
            }
        ),
        Tool(
            name="get_cash_flow_statement",
            description="Get cash flow statement showing operating, investing, and financing activities",
            inputSchema={
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Stock ticker symbol"
                    },
                    "period": {
                        "type": "string",
                        "description": "Reporting period: 'annual' or 'quarter'",
                        "default": "annual"
                    },
                    "limit": {
                        "type": "number",
                        "description": "Number of periods to retrieve",
                        "default": 5
                    }
                },
                "required": ["symbol"]
            }
        ),
        Tool(
            name="get_financial_growth",
            description="Get financial growth metrics showing year-over-year growth rates",
            inputSchema={
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Stock ticker symbol"
                    },
                    "period": {
                        "type": "string",
                        "description": "Reporting period: 'annual' or 'quarter'",
                        "default": "annual"
                    },
                    "limit": {
                        "type": "number",
                        "description": "Number of periods to retrieve",
                        "default": 5
                    }
                },
                "required": ["symbol"]
            }
        ),
    ]


def handle_financials_tool(client: FMPClient, name: str, arguments: Any) -> Any:
    """Handle financial statement tool execution."""
    if name == "get_income_statement":
        return client.get_income_statement(
            symbol=arguments["symbol"],
            period=arguments.get("period", "annual"),
            limit=arguments.get("limit", 5)
        )

    elif name == "get_balance_sheet":
        return client.get_balance_sheet(
            symbol=arguments["symbol"],
            period=arguments.get("period", "annual"),
            limit=arguments.get("limit", 5)
        )

    elif name == "get_cash_flow_statement":
        return client.get_cash_flow_statement(
            symbol=arguments["symbol"],
            period=arguments.get("period", "annual"),
            limit=arguments.get("limit", 5)
        )

    elif name == "get_financial_growth":
        return client.get_financial_growth(
            symbol=arguments["symbol"],
            period=arguments.get("period", "annual"),
            limit=arguments.get("limit", 5)
        )

    return None

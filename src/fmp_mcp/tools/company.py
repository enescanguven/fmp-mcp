"""Company-related MCP tools."""

from typing import Any
from mcp.types import Tool, TextContent
from fmp import FMPClient


def get_company_tools() -> list[Tool]:
    """Get list of company-related tools."""
    return [
        Tool(
            name="get_company_profile",
            description="Get detailed company profile including stock price, market cap, business description, and fundamental metrics",
            inputSchema={
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Stock ticker symbol (e.g., 'AAPL', 'TSLA')"
                    }
                },
                "required": ["symbol"]
            }
        ),
        Tool(
            name="search_symbol",
            description="Search for stocks by company name or symbol. Returns matching ticker symbols.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Company name or partial symbol to search for"
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="search_by_name",
            description="Search for ticker symbols by full or partial company name",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Full or partial company or asset name"
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="search_by_cik",
            description="Retrieve company information by Central Index Key (CIK)",
            inputSchema={
                "type": "object",
                "properties": {
                    "cik": {
                        "type": "string",
                        "description": "Central Index Key of the company"
                    }
                },
                "required": ["cik"]
            }
        ),
        Tool(
            name="search_by_cusip",
            description="Search for securities by CUSIP number",
            inputSchema={
                "type": "object",
                "properties": {
                    "cusip": {
                        "type": "string",
                        "description": "CUSIP number of the financial security"
                    }
                },
                "required": ["cusip"]
            }
        ),
        Tool(
            name="search_by_isin",
            description="Search for securities by International Securities Identification Number (ISIN)",
            inputSchema={
                "type": "object",
                "properties": {
                    "isin": {
                        "type": "string",
                        "description": "ISIN of the financial security"
                    }
                },
                "required": ["isin"]
            }
        ),
        Tool(
            name="get_stock_list",
            description="Retrieve a comprehensive list of all available stocks with symbol, name, price, exchange, and country information",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="screen_stocks",
            description="Screen stocks based on various financial and market criteria (market cap, price, beta, volume, dividend, sector, industry, etc.)",
            inputSchema={
                "type": "object",
                "properties": {
                    "market_cap_more_than": {
                        "type": "number",
                        "description": "Minimum market capitalization"
                    },
                    "market_cap_lower_than": {
                        "type": "number",
                        "description": "Maximum market capitalization"
                    },
                    "price_more_than": {
                        "type": "number",
                        "description": "Minimum stock price"
                    },
                    "price_lower_than": {
                        "type": "number",
                        "description": "Maximum stock price"
                    },
                    "beta_more_than": {
                        "type": "number",
                        "description": "Minimum beta value"
                    },
                    "beta_lower_than": {
                        "type": "number",
                        "description": "Maximum beta value"
                    },
                    "volume_more_than": {
                        "type": "number",
                        "description": "Minimum trading volume"
                    },
                    "volume_lower_than": {
                        "type": "number",
                        "description": "Maximum trading volume"
                    },
                    "dividend_more_than": {
                        "type": "number",
                        "description": "Minimum dividend yield"
                    },
                    "dividend_lower_than": {
                        "type": "number",
                        "description": "Maximum dividend yield"
                    },
                    "sector": {
                        "type": "string",
                        "description": "Filter by sector (e.g., 'Technology', 'Healthcare')"
                    },
                    "industry": {
                        "type": "string",
                        "description": "Filter by industry (e.g., 'Consumer Electronics')"
                    },
                    "country": {
                        "type": "string",
                        "description": "Filter by country (e.g., 'US')"
                    },
                    "exchange": {
                        "type": "string",
                        "description": "Filter by exchange (e.g., 'NASDAQ', 'NYSE')"
                    },
                    "is_etf": {
                        "type": "boolean",
                        "description": "Filter for ETFs"
                    },
                    "is_fund": {
                        "type": "boolean",
                        "description": "Filter for mutual funds"
                    },
                    "is_actively_trading": {
                        "type": "boolean",
                        "description": "Filter for actively trading stocks"
                    },
                    "limit": {
                        "type": "number",
                        "description": "Maximum number of results to return"
                    }
                }
            }
        ),
    ]


def handle_company_tool(client: FMPClient, name: str, arguments: Any) -> Any:
    """Handle company tool execution."""
    if name == "get_company_profile":
        return client.get_profile(arguments["symbol"])

    elif name == "search_symbol":
        return client.search_symbol(arguments["query"])

    elif name == "search_by_name":
        return client.search_by_name(arguments["query"])

    elif name == "search_by_cik":
        return client.search_by_cik(arguments["cik"])

    elif name == "search_by_cusip":
        return client.search_by_cusip(arguments["cusip"])

    elif name == "search_by_isin":
        return client.search_by_isin(arguments["isin"])

    elif name == "get_stock_list":
        return client.get_stock_list()

    elif name == "screen_stocks":
        return client.screen_stocks(**arguments)

    return None

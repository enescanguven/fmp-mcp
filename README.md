# FMP MCP Server

MCP server for Financial Modeling Prep API. Enables Claude to access real-time stock data, financial statements, cryptocurrency information, and market data.

## Features

**Company (8 tools)**: Profile, search, screening, CIK/CUSIP/ISIN lookup, stock list

**Market (7 tools)**: Real-time quotes, historical prices, P/E ratios, sector/industry performance

**Crypto (4 tools)**: Quotes, list, historical data, news

**Financials (4 tools)**: Income statement, balance sheet, cash flow, growth metrics

## Installation

```bash
git clone https://github.com/yourusername/fmp-mcp.git
cd fmp-mcp
pip install -e .

# Setup API key
cp .env.example .env
# Edit .env and add your FMP_API_KEY
```

**Prerequisites**: Python 3.10+, [FMP API key](https://site.financialmodelingprep.com/developer/docs)

## Usage

Add to Claude Desktop config:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "fmp": {
      "command": "python",
      "args": ["-m", "fmp_mcp.server"],
      "env": {
        "FMP_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

### Example Prompts

- "What's Apple's current stock price and market cap?"
- "Find technology companies with market cap over $100B"
- "Show me Tesla's income statement for the last 3 years"
- "What's the current Bitcoin price?"
- "Get historical prices for NVDA over the last 30 days"

## Development

```bash
pytest                    # Run tests
black src/ tests/         # Format code
ruff check src/ tests/    # Lint code
```

## Troubleshooting

**API Key Issues**: Verify key in `.env` or Claude config

**Connection Issues**: Check path in `claude_desktop_config.json`

**Debug**: Use MCP Inspector
```bash
npx @modelcontextprotocol/inspector python -m fmp_mcp.server
```

## Links

- [FMP API Documentation](https://site.financialmodelingprep.com/developer/docs)
- [Model Context Protocol](https://modelcontextprotocol.io)

## License

MIT

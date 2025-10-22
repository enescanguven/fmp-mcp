# FMP MCP Server

MCP (Model Context Protocol) server for the Financial Modeling Prep API. This server enables Claude and other MCP clients to access real-time stock data, financial statements, cryptocurrency information, and comprehensive market data.

## Features

### 23 Financial Data Tools

**Company Data (8 tools)**
- Company profiles with fundamentals
- Symbol and name search
- CIK/CUSIP/ISIN lookup
- Stock screening with filters
- Complete stock listings

**Market Data (7 tools)**
- Real-time quotes
- Historical price data (intraday & daily)
- Industry/sector P/E ratios
- Industry performance metrics
- Historical sector analysis

**Cryptocurrency (4 tools)**
- Real-time crypto quotes
- Available crypto list
- Historical crypto data
- Latest crypto news

**Financial Statements (4 tools)**
- Income statements
- Balance sheets
- Cash flow statements
- Financial growth metrics

## Installation

### Prerequisites

- Python 3.10 or higher
- FMP API key ([Get one here](https://site.financialmodelingprep.com/developer/docs))

### Install from Source

```bash
# Clone the repository
git clone https://github.com/yourusername/fmp-mcp.git
cd fmp-mcp

# Install the package
pip install -e .

# Or with development dependencies
pip install -e ".[dev]"
```

### Setup Environment

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` and add your FMP API key:

```
FMP_API_KEY=your_api_key_here
```

## Usage

### Running the Server

The MCP server runs as a stdio-based service:

```bash
python -m fmp_mcp.server
```

### Claude Desktop Configuration

Add to your Claude Desktop config file:

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

Alternatively, if using uv:

```json
{
  "mcpServers": {
    "fmp": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/fmp-mcp",
        "run",
        "fmp-mcp"
      ],
      "env": {
        "FMP_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

### Available Tools

Once configured, Claude will have access to these tools:

#### Company Tools
- `get_company_profile` - Detailed company information
- `search_symbol` - Search by symbol or name
- `search_by_name` - Search by company name
- `search_by_cik` - Lookup by CIK
- `search_by_cusip` - Lookup by CUSIP
- `search_by_isin` - Lookup by ISIN
- `get_stock_list` - List all stocks
- `screen_stocks` - Screen stocks by criteria

#### Market Tools
- `get_quote` - Real-time quote
- `get_historical_chart` - Historical prices
- `get_historical_price` - Daily historical data
- `get_industry_pe` - Industry P/E ratios
- `get_sector_pe` - Sector P/E ratios
- `get_industry_performance` - Industry performance
- `get_historical_sector_pe` - Historical sector P/E

#### Crypto Tools
- `get_crypto_quote` - Crypto quote
- `get_crypto_list` - Available cryptos
- `get_crypto_historical` - Crypto historical data
- `get_crypto_news` - Latest crypto news

#### Financial Statement Tools
- `get_income_statement` - Income statement
- `get_balance_sheet` - Balance sheet
- `get_cash_flow_statement` - Cash flow
- `get_financial_growth` - Growth metrics

## Example Prompts for Claude

Once the MCP server is connected to Claude Desktop, you can ask:

**Company Research**
> "What's Apple's current stock price and market cap?"
>
> "Find all technology companies with market cap over $100B"
>
> "Show me Tesla's company profile"

**Market Analysis**
> "Get the latest quote for NVDA"
>
> "Show me historical prices for AAPL over the last 30 days"
>
> "What are the P/E ratios for tech sector stocks?"

**Crypto Tracking**
> "What's the current Bitcoin price?"
>
> "Show me historical data for Ethereum"
>
> "Get the latest crypto news"

**Financial Analysis**
> "Show me Microsoft's income statement for the last 3 years"
>
> "Get Apple's balance sheet and cash flow statement"
>
> "What's the revenue growth for Amazon?"

## Development

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
# Format code
black src/ tests/

# Lint code
ruff check src/ tests/
```

## Project Structure

```
fmp-mcp/
├── src/
│   └── fmp_mcp/
│       ├── __init__.py
│       └── server.py          # Main MCP server implementation
├── tests/
│   └── test_server.py
├── .env.example
├── .gitignore
├── pyproject.toml
└── README.md
```

## Dependencies

- `mcp` - Model Context Protocol SDK
- `fmp-python` - Financial Modeling Prep Python client
- `python-dotenv` - Environment variable management

## API Rate Limits

Be aware of FMP API rate limits based on your subscription tier:
- Free tier: Limited requests per minute
- Paid tiers: Higher rate limits

See [FMP pricing](https://site.financialmodelingprep.com/developer/docs/pricing) for details.

## Troubleshooting

### API Key Issues

If you see authentication errors:
1. Verify your API key is correct in `.env` or Claude config
2. Check your API key is active at [FMP Dashboard](https://site.financialmodelingprep.com/developer/docs/dashboard)
3. Ensure your subscription tier supports the endpoints you're using

### Connection Issues

If Claude can't connect to the server:
1. Verify the path in `claude_desktop_config.json` is correct
2. Check that Python and required packages are installed
3. Try running the server manually to see error messages:
   ```bash
   python -m fmp_mcp.server
   ```

### MCP Inspector

For debugging, use the MCP Inspector:

```bash
npx @modelcontextprotocol/inspector python -m fmp_mcp.server
```

## Links

- [FMP API Documentation](https://site.financialmodelingprep.com/developer/docs)
- [FMP Python SDK](https://github.com/yourusername/fmp-python)
- [Model Context Protocol](https://modelcontextprotocol.io)
- [Claude Desktop](https://claude.ai/desktop)

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## TODO

### Future Enhancements
- [ ] Add more FMP endpoints (earnings, dividends, SEC filings)
- [ ] Implement response caching
- [ ] Add rate limiting handling
- [ ] Support for async operations
- [ ] Add more comprehensive error messages
- [ ] Add example notebooks/scripts

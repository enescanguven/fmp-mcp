"""Entry point for running the FMP MCP server."""

import asyncio
from .server import main

if __name__ == "__main__":
    asyncio.run(main())

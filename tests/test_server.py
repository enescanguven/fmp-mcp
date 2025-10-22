"""Basic tests for FMP MCP server."""

import pytest
from unittest.mock import Mock, patch
from fmp_mcp.server import format_response, handle_fmp_error
from fmp import FMPAPIError, FMPAuthError


def test_format_response_with_dict():
    """Test formatting a dictionary response."""
    data = {"symbol": "AAPL", "price": 150.0}
    result = format_response(data)
    assert "AAPL" in result
    assert "150" in result


def test_format_response_with_list():
    """Test formatting a list response."""
    data = [{"symbol": "AAPL"}, {"symbol": "TSLA"}]
    result = format_response(data)
    assert "AAPL" in result
    assert "TSLA" in result


def test_format_response_with_pydantic_model():
    """Test formatting a Pydantic model."""
    from fmp.models import Quote

    # Create a mock Quote object
    mock_quote = Mock(spec=Quote)
    mock_quote.model_dump.return_value = {
        "symbol": "AAPL",
        "price": 150.0,
        "volume": 1000000
    }

    result = format_response(mock_quote)
    assert "AAPL" in result
    assert "150" in result


def test_handle_fmp_auth_error():
    """Test handling FMP authentication errors."""
    error = FMPAuthError("Invalid API key", 401)
    result = handle_fmp_error(error)
    assert "Authentication Error" in result
    assert "API key" in result


def test_handle_fmp_api_error():
    """Test handling FMP API errors."""
    error = FMPAPIError("Rate limit exceeded", 429)
    result = handle_fmp_error(error)
    assert "API Error" in result


def test_handle_generic_error():
    """Test handling generic errors."""
    error = Exception("Something went wrong")
    result = handle_fmp_error(error)
    assert "Error" in result
    assert "Something went wrong" in result


@pytest.mark.asyncio
async def test_list_tools():
    """Test that list_tools returns all expected tools."""
    from fmp_mcp.server import list_tools

    tools = await list_tools()

    # Check we have the right number of tools
    # 8 company + 7 market + 4 crypto + 4 financials = 23 tools
    assert len(tools) == 23

    # Check some specific tools exist
    tool_names = [tool.name for tool in tools]
    assert "get_company_profile" in tool_names
    assert "get_quote" in tool_names
    assert "get_crypto_quote" in tool_names
    assert "get_income_statement" in tool_names
    assert "screen_stocks" in tool_names


@pytest.mark.asyncio
async def test_get_fmp_client_without_api_key():
    """Test that get_fmp_client raises error without API key."""
    from fmp_mcp.server import get_fmp_client

    with patch.dict('os.environ', {}, clear=True):
        with pytest.raises(ValueError, match="FMP_API_KEY"):
            get_fmp_client()


@pytest.mark.asyncio
async def test_get_fmp_client_with_api_key():
    """Test that get_fmp_client creates client with API key."""
    from fmp_mcp.server import get_fmp_client
    import fmp_mcp.server as server_module

    # Reset the global client
    server_module.fmp_client = None

    with patch.dict('os.environ', {'FMP_API_KEY': 'test_key'}):
        client = get_fmp_client()
        assert client is not None
        assert client.api_key == 'test_key'

    # Reset for other tests
    server_module.fmp_client = None

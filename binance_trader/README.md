# MCP Binance Trader Server

This MCP server interacts with the Binance API to execute trades.

## Purpose

The purpose of this MCP server is to provide a simple and easily accessible way for AI agents to interact with the Binance API. This can be used for automated trading strategies, portfolio management, and other applications that require access to Binance's trading platform.

## Usage

To use this MCP server, you will need to:

1.  Install Python 3.7+
2.  Install FastAPI and Uvicorn:

    ```bash
    pip install fastapi uvicorn
    ```
3.  Run the server using Uvicorn:

    ```bash
    uvicorn mcp_binance_trader:app --host 0.0.0.0 --port 8006
    ```

4.  Send a GET request to the `/mcp/trade/binance` endpoint with the following query parameters:

    *   `symbol`: The trading symbol (e.g., BTCUSDT).
    *   `side`: The trade side (BUY or SELL).
    *   `quantity`: The quantity of the asset to trade.
    *   `price`: The price at which to trade.

    Example:

    ```
    http://localhost:8006/mcp/trade/binance?symbol=BTCUSDT&side=BUY&quantity=0.1&price=30000
    ```

5.  The server will return a JSON response containing the details of the trade, including the symbol, side, quantity, price, success status, order ID, and executed quantity.

## $MCPAX Integration

This MCP server can be integrated into the MCPAX ecosystem by:

*   **Listing it on the MCPAX marketplace:** MCP developers can list their server on the MCPAX marketplace and offer it to dApp developers for free or for rent using the MCPAX token ($MCPAX).
*   **Using MCPAX for trading fees:** The server can be configured to use MCPAX tokens to pay for trading fees on Binance, providing a discount to users who hold MCPAX.
*   **Staking MCPAX for higher API limits:** Users who stake MCPAX tokens can be granted higher API rate limits for using the server, allowing them to execute more trades per minute.

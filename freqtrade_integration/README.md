# MCP Freqtrade Integration Server

This MCP server integrates with the Freqtrade cryptocurrency trading bot.

## Purpose

The purpose of this MCP server is to provide a simple and easily accessible way for AI agents to interact with the Freqtrade cryptocurrency trading bot. This can be used for automated trading strategies, backtesting, and other tasks related to cryptocurrency trading.

## Usage

To use this MCP server, you will need to:

1.  Install Python 3.7+
2.  Install FastAPI and Uvicorn:

    ```bash
    pip install fastapi uvicorn
    ```
3.  Run the server using Uvicorn:

    ```bash
    uvicorn mcp_freqtrade_integration:app --host 0.0.0.0 --port 8008
    ```

4.  Send a GET request to the `/mcp/trade/freqtrade` endpoint with the following query parameters:

    *   `command`: The Freqtrade command to execute (e.g., trade, backtest, list-pairs).
    *   `params` (optional): Optional parameters for the Freqtrade command (as a JSON string).

    Example:

    ```
    http://localhost:8008/mcp/trade/freqtrade?command=trade&params={"strategy": "MyStrategy", "ticker": "BTCUSDT"}
    ```

5.  The server will return a JSON response containing the command, parameters, success status, and result.

## $MCPAX Integration

This MCP server can be integrated into the MCPAX ecosystem by:

*   **Listing it on the MCPAX marketplace:** MCP developers can list their server on the MCPAX marketplace and offer it to dApp developers for free or for rent using the MCPAX token ($MCPAX).
*   **Using MCPAX for strategy subscriptions:** Users can subscribe to Freqtrade strategies using MCPAX tokens, allowing them to access premium trading strategies.
*   **Staking MCPAX for backtesting credits:** Users who stake MCPAX tokens can be granted backtesting credits, allowing them to test their strategies more extensively.

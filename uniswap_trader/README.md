# MCP Uniswap Trader Server

This MCP server automates token swaps on Uniswap DEX across multiple blockchains.

## Purpose

The purpose of this MCP server is to provide a simple and easily accessible way for AI agents to automate token swaps on Uniswap. This can be used for automated trading strategies, portfolio rebalancing, and other DeFi applications.

## Usage

To use this MCP server, you will need to:

1.  Install Python 3.7+
2.  Install FastAPI and Uvicorn:

    ```bash
    pip install fastapi uvicorn
    ```
3.  Run the server using Uvicorn:

    ```bash
    uvicorn mcp_uniswap_trader:app --host 0.0.0.0 --port 8005
    ```

4.  Send a GET request to the `/mcp/trade/uniswap` endpoint with the following query parameters:

    *   `token_in`: The address of the input token.
    *   `token_out`: The address of the output token.
    *   `amount_in`: The amount of the input token to swap.
    *   `slippage` (optional): The maximum slippage allowed for the swap (e.g., 0.005 for 0.5%). Defaults to 0.005.
    *   `gas_limit` (optional): The gas limit for the transaction. Defaults to 200000.

    Example:

    ```
    http://localhost:8005/mcp/trade/uniswap?token_in=0x...&token_out=0x...&amount_in=1.0&slippage=0.01
    ```

5.  The server will return a JSON response containing the details of the swap, including the input and output tokens, amounts, slippage, gas used, and success status.

## $MCPAX Integration

This MCP server can be integrated into the MCPAX ecosystem by:

*   **Listing it on the MCPAX marketplace:** MCP developers can list their server on the MCPAX marketplace and offer it to dApp developers for free or for rent using the MCPAX token ($MCPAX).
*   **Using MCPAX for gas fees:** The server can be configured to use MCPAX tokens to pay for gas fees on Uniswap, providing a discount to users who hold MCPAX.
*   **Staking MCPAX for higher rate limits:** Users who stake MCPAX tokens can be granted higher rate limits for using the server, allowing them to execute more trades per minute.

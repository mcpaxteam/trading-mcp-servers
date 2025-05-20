# MCP Jupiter Trader Server

This MCP server executes token swaps on the Solana blockchain using Jupiter's Ultra API.

## Purpose

The purpose of this MCP server is to provide a simple and easily accessible way for AI agents to execute token swaps on the Solana blockchain using Jupiter's Ultra API. This can be used for automated trading strategies, portfolio rebalancing, and other DeFi applications on Solana.

## Usage

To use this MCP server, you will need to:

1.  Install Python 3.7+
2.  Install FastAPI and Uvicorn:

    ```bash
    pip install fastapi uvicorn
    ```
3.  Run the server using Uvicorn:

    ```bash
    uvicorn mcp_jupiter_trader:app --host 0.0.0.0 --port 8007
    ```

4.  Send a GET request to the `/mcp/trade/jupiter` endpoint with the following query parameters:

    *   `token_in`: The address of the input token on Solana.
    *   `token_out`: The address of the output token on Solana.
    *   `amount_in`: The amount of the input token to swap.
    *   `slippage` (optional): The maximum slippage allowed for the swap (e.g., 0.005 for 0.5%). Defaults to 0.005.

    Example:

    ```
    http://localhost:8007/mcp/trade/jupiter?token_in=So1111111111111111111111111111111111111112&token_out=EPjFWdd5AufqALUs2vEqk29iUMjYPN26sESpYRjhSyG&amount_in=1.0&slippage=0.01
    ```

5.  The server will return a JSON response containing the details of the swap, including the input and output tokens, amounts, slippage, fee amount, and success status.

## $MCPAX Integration

This MCP server can be integrated into the MCPAX ecosystem by:

*   **Listing it on the MCPAX marketplace:** MCP developers can list their server on the MCPAX marketplace and offer it to dApp developers for free or for rent using the MCPAX token ($MCPAX).
*   **Using MCPAX for transaction fees:** The server can be configured to use MCPAX tokens to pay for transaction fees on Solana, providing a discount to users who hold MCPAX.
*   **Staking MCPAX for priority routing:** Users who stake MCPAX tokens can be granted priority routing for their swaps, ensuring faster execution times.

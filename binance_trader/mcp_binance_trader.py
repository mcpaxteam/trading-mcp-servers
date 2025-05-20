from fastapi import FastAPI, Query
from typing import Dict
import random

app = FastAPI(
    title="MCP Binance Trader",
    description="An MCP server for AI agents to interact with the Binance API.",
    version="0.1.0",
)

@app.get("/mcp/trade/binance")
async def trade_on_binance(
    symbol: str = Query(..., description="The trading symbol (e.g., BTCUSDT)."),
    side: str = Query(..., description="The trade side (BUY or SELL)."),
    quantity: float = Query(..., description="The quantity of the asset to trade."),
    price: float = Query(..., description="The price at which to trade.")
):
    """
    Interacts with the Binance API to execute trades.
    """

    # Simulate the trade (replace with actual Binance API integration)
    success = random.random() > 0.05  # Simulate occasional failures
    order_id = random.randint(1000000, 9999999)
    executed_quantity = quantity if success else 0

    return {
        "symbol": symbol,
        "side": side,
        "quantity": quantity,
        "price": price,
        "success": success,
        "order_id": order_id,
        "executed_quantity": executed_quantity,
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8006)

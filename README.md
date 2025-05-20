# MCP Trading Servers

This repository contains a collection of Model Context Protocol (MCP) servers for various trading use cases. These servers are built using FastAPI and can be deployed to a decentralized compute platform like 0G/Akash.

## What are MCPs and why are they valuable?

Model Context Protocols (MCPs) are a new paradigm for building decentralized applications. They allow developers to create specialized servers that provide specific data and functionality to dApps. This approach offers several advantages:

*   **Improved Scalability:** By offloading complex computations and data retrieval to specialized MCP servers, dApps can scale more efficiently.
*   **Enhanced Security:** MCP servers can be deployed in secure enclaves, protecting sensitive data and computations from unauthorized access.
*   **Increased Flexibility:** MCPs can be easily customized and updated to meet the evolving needs of dApps.
*   **Quantum-Safe Compute:** MCPs can be configured to use quantum-resistant cryptographic algorithms, protecting dApps from future quantum threats.

## MCPs in the MCPAX Ecosystem

These MCP servers are designed to be integrated into the MCPAX ecosystem. They can be deployed on the MCPAX marketplace and offered to dApp developers for free or for rent using the MCPAX token ($MCPAX). This allows MCP developers to monetize their work and dApp developers to access a wide range of specialized data and functionality.

## Trading MCP Servers

The following trading MCP servers are included in this repository:

*   **Uniswap Trader:** Automates token swaps on Uniswap DEX across multiple blockchains. [README](./uniswap_trader/README.md)
*   **Binance Trader:** Interacts with the Binance API to execute trades. [README](./binance_trader/README.md)
*   **Jupiter Trader:** Executes token swaps on the Solana blockchain using Jupiter's Ultra API. [README](./jupiter_trader/README.md)
*   **Freqtrade Integration:** Integrates with the Freqtrade cryptocurrency trading bot. [README](./freqtrade_integration/README.md)

## Usage

To use these MCP servers, you will need to:

1.  Install Python 3.7+
2.  Install FastAPI and Uvicorn:

    ```bash
    pip install fastapi uvicorn
    ```
3.  Run the server using Uvicorn:

    ```bash
    uvicorn mcp_uniswap_trader:app --host 0.0.0.0 --port 8005
    ```

    Replace `mcp_uniswap_trader` with the name of the MCP server you want to run, and adjust the port number accordingly. See the individual README files for each server for specific instructions.

## Deployment

These MCP servers can be deployed to a decentralized compute platform like 0G/Akash. Refer to the MCPAX documentation for more information on how to deploy MCP servers.

## Contributing

Contributions to this repository are welcome. Please submit a pull request with your changes.

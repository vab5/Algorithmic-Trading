# TradingAlgorithms

This repository contains trading algorithms I created.

# Setup

pip install alpaca-py, lumibot, torch

When using vscode, make sure the python interpreter is conda. ctrl shift p and then search python interpreter.

Make sure that config.json file is setup with api_key and api_secret.

Ex:

API_KEY = "xxxxxxx"
API_SECRET = "xxxxxx"

ALPACA_CONFIG = {
"API_KEY": API_KEY,
"API_SECRET": API_SECRET,
"ENDPOINT": "https://paper-api.alpaca.markets/v2",
}

pip install lumibot

# installing ta-lib

brew install ta-lib

- install homebrew and add to path

then pip install ta-lib

# Alpaca API Docs

https://docs.alpaca.markets/reference/stockbars-1

https://alpaca.markets/sdks/python/trading.html

Potential Backtesting: https://alpaca.markets/learn/introduction-to-backtesting-with-vectorbt/

https://www.backtrader.com/blog/2019-08-22-practical-backtesting-replication/practical-replication/#test-runs-mix

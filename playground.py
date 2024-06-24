from alpaca.trading.client import TradingClient
from algorithms.config import API_KEY, API_SECRET
from functions.making_orders import makeBuyOrder, makeSellOrder


# Initialize the Alpaca API
trading_client = TradingClient(API_KEY, API_SECRET)
makeBuyOrder(trading_client, "NVDA", 2)



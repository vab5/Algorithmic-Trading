

import pandas as pd
from alpaca.data import StockHistoricalDataClient, TimeFrame
from alpaca.data.requests import StockQuotesRequest, StockBarsRequest
from algorithms.config import API_KEY, API_SECRET



# Instantiate a data client
data_client = StockHistoricalDataClient(API_KEY, API_SECRET)

# Set the start time
start_time = pd.to_datetime("2023-01-19").tz_localize('America/New_York')

# It's generally best to explicitly provide an end time but will default to 'now' if not
request_params = StockBarsRequest(
    symbol_or_symbols=['aapl'],
    timeframe=TimeFrame.Day,
    start=start_time
    )

bars_df = data_client.get_stock_bars(request_params).df.tz_convert('America/New_York', level=1)

print(bars_df)
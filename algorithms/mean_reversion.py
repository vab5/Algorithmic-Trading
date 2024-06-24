
from lumibot.brokers import Alpaca
from lumibot.strategies import Strategy
from lumibot.traders import Trader
from lumibot.backtesting import YahooDataBacktesting

from alpaca import REST, TimeFrame
from datetime import datetime, timedelta

from config import API_KEY, API_SECRET, ALPACA_CONFIG

class MeanReversionStrategy(Strategy):
    def initialize(self):
        self.symbol = 'SPY'
        self.window = 20  # Length of the moving average
        self.invested = False
        

    def get_last_prices(self):
        # Fetch historical data
        end_date = datetime.now()
        start_date = end_date - timedelta(days=self.window * 2) 
        data = self.get_bars(self.symbol, "DAY", start_date.isoformat(), end_date.isoformat()).df
        return data['close'].tail(self.window)

    def on_trading_iteration(self, state):
        last_prices = self.get_last_prices()
        moving_average = last_prices.mean()
        current_price = last_prices.iloc[-1]

        print(f'Current Price: {current_price}, Moving Average: {moving_average}')

        if not self.invested and current_price < moving_average:
            # Buy if the price is below the moving average and not currently invested
            quantity = self.cash // current_price
            self.create_order(self.symbol, quantity, 'buy')
            self.invested = True
            print(f'Bought {quantity} shares at {current_price}')
        elif self.invested and current_price > moving_average:
            # Sell if the price is above the moving average and currently invested
            position = self.get_position(self.symbol)
            if position:
                self.create_order(self.symbol, position.quantity, 'sell')
                self.invested = False
                print(f'Sold {position.quantity} shares at {current_price}')

# Setup and run the bot
if __name__ == "__main__":
    trade = False
    if trade:
        brokers = Alpaca(ALPACA_CONFIG)
        strategy = MeanReversionStrategy(broker=brokers)
        trader = Trader()
        trader.add_strategy(strategy)
        trader.run_all()
    else:
        start = datetime(2016, 1, 1)
        end = datetime(2024, 6, 10)
        result = MeanReversionStrategy.backtest(YahooDataBacktesting, start, end)
        print(result)
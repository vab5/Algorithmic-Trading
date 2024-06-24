
# Owner: Varun Bussa
# Purpose: Define functions to make buy and sell orders using Alpaca Trading Client

from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

def makeBuyOrder(tradingClient, symb, quantity, timeInForce = TimeInForce.DAY ): 
    """
    Place a buy order. See https://docs.alpaca.markets/reference/postorder for 
    what all of the parameters mean.
    """
    market_order_data = MarketOrderRequest(
                    symbol=symb,
                    qty=quantity,
                    side=OrderSide.BUY,
                    time_in_force=timeInForce
                    )
    market_order = tradingClient.submit_order(
                order_data=market_order_data
               )
    return market_order



def makeSellOrder(tradingClient, symb, quantity, timeInForce = TimeInForce.DAY ): 
    """
    Place a sell order. See https://docs.alpaca.markets/reference/postorder for 
    what all of the parameters mean.
    """
    market_order_data = MarketOrderRequest(
                    symbol=symb,
                    qty=quantity,
                    side=OrderSide.SELL,
                    time_in_force=timeInForce
                    )
    market_order = tradingClient.submit_order(
                order_data=market_order_data
               )
    return market_order

def cancelOrderByID(tradingClient, order_id):
    """
    Cancel an order using the order's id. See example of how to use. 
    
    Ex: 

    trading_client = TradingClient(API_KEY, API_SECRET)
    order = makeBuyOrder(trading_client,"SPY",2)
    trading_client.cancel_order_by_id(order.id)
    
    """
    return tradingClient.cancel_order_by_id(order_id)
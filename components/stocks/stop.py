# This file contains logic to stop orders to buy/sell stocks in RH

# Robin Stocks Library
from robin_stocks import * 
import robin_stocks.robinhood as r 


# This function cancels all stock orders
def cancelAllStockOrders():
    cancel = r.cancel_all_stock_orders()
    return cancel

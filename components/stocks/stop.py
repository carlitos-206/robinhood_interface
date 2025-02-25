# This this the library that allows access to robinhood
from robin_stocks import * # first import the library
import robin_stocks.robinhood as r # import the


# This function cancels all stock orders
def cancelAllStockOrders():
    cancel = r.cancel_all_stock_orders()
    return cancel

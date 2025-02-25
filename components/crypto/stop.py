# This file contain logic to stop buy/sell order of crypto available in RH

# Robin Stocks Library
from robin_stocks import * 
import robin_stocks.robinhood as r 

# This function cancels crypto order by ID
def cancelOrderByID(id):
  cancel = r.cancel_crypto_order(id)
  return cancel


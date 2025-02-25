# This this the library that allows access to robinhood
from robin_stocks import * # first import the library
import robin_stocks.robinhood as r # import the

# This function cancels crypto order by ID
def cancelOrderByID(id):
  cancel = r.cancel_crypto_order(id)
  return cancel


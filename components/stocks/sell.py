# This file contains logic to sell available stocks in RH

# Robin Stocks Library
from robin_stocks import * 
import robin_stocks.robinhood as r 

# Custom Modules
from info import getMarketBySymbol, isOpen, getSharePrice

# This function sells full share for stocks
def simpleShareSellStock(name, count):
    sell = r.order_sell_market(name, count)
    return sell

# This function sells fractional stocks by price
def simpleFractionalSellStock(name, amount):
    sell = r.order_sell_fractional_by_price(name, amount)
    return sell





# This function sells a stocks if market is open
def sellShareIfOpen(name, count):
  market = getMarketBySymbol(name)
  if market != False:
    is_open = isOpen(market)
    if is_open == True:
      sell = simpleShareSellStock(name, count)
      return{
        "status": 200,
        "message": sell
      }
    else:
      return {
        "status": 405,
        "message": "Market is closed, cannot sell"
      }
  return {
    "status": 404,
    "message": "Invalid Symbol"
  }


# This function sells fractional stock if open
def sellFractionalIfOpen(name, amount):
  market = getMarketBySymbol(name)
  if market != False:
    is_open = isOpen(market)
    if is_open == True:
      sell = simpleFractionalSellStock(name, amount)
      return{
        "status": 200,
        "message": sell
      }
    else:
      return {
        "status": 405,
        "message": "Market is closed, cannot sell"
      }
  return {
    "status": 404,
    "message": "Invalid Symbol"
  }


#  This function sells a stock at market open
def sellShareAtMarketOpen(name, count):
  market = getMarketBySymbol(name)
  if market != False:
      sell = simpleShareSellStock(name, count)
      return{
        "status": 200,
        "message": sell
      }
  return {
    "status": 404,
    "message": "Invalid Symbol"
  }

# This function sells a fractional stock at market open
def sellFractionalAtMarketOpen(name, count):
  market = getMarketBySymbol(name)
  if market != False:
      sell = simpleFractionalSellStock(name, count)
      return{
        "status": 200,
        "message": sell
      }
  return {
    "status": 404,
    "message": "Invalid Symbol"
  }

# This function sells a share stock when it reaches a limit - Downward or Upward
def sellShareAtPrice(name, count, price):
  market = getMarketBySymbol(name)
  if market != False:
    positions_data = r.get_all_positions()
    for item in positions_data:
      item['symbol'] = r.get_symbol_by_url(item['instrument'])
    stock = [ item for item in positions_data if item['symbol'] == name ]
    sell = r.order_sell_limit(name, count, price)
    if sell['detail'] == 'Not enough shares to sell.':
      return {
        "status": 404,
        "message": f"Not enough shares to sell Own: {stock[0]['quantity']} attempted to sell: {count}"
      }
    return {
      "status": 200,
      "message": sell
    }
  return {
    "status": 404,
    "message": "Invalid Symbol"
  }

def sellFractionalAtPriceDrop(name, amount, price):
  cost = getSharePrice(name)
  if cost['status'] == 200:
    if price >= int(float(cost['Message']['price'])):
      sell = simpleFractionalSellStock(name, amount)
      return{
        'status': 200,
        'message': sell
      }
    else:
      print(f'{cost}, {price}')
      return sellFractionalAtPriceDrop(name, amount, price)


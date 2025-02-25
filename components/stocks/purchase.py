# This this the library that allows access to robinhood
from robin_stocks import * # first import the library
import robin_stocks.robinhood as r # import the


# This function buys stocks by share count
def simpleBuyStockByShare(name, count):
  order = r.order_buy_market(name, count)
  return order

# This function buys fractional stocks by price
def simpleFractionalBuyStock(name, amount):
  order = r.order_buy_fractional_by_price(name, amount)
  return order


# This function buys a share in a stock only if market is open
def buyShareIfOpen(name, count): 
  market = getMarketBySymbol(name)
  if market != False:
    is_open = isOpen(market)
    if is_open == True:
      buy = simpleBuyStockByShare(name, count)
      return {
        "status": 200,
        "message": buy
      }
    else:
      return {
        "status": 405, # Method not allowed
        "message": "Market is closed"
      }
  return {
    "status": 404,
    "message": "Invalid Symbol"
  }


# This function buys fractional stocks if market is open
def buyFractionalIfOpen(name, amount):
  market = getMarketBySymbol(name)
  if market != False:
    is_open = isOpen(market)
    if is_open == True:
      buy = simpleFractionalBuyStock(name, amount)
      return {
        "status": 200,
        "message": buy
      }
    else:
      return {
        "status": 405, # Method not allowed
        "message": "Market is closed"
      }
  return {
    "status": 404,
    "message": "Invalid Symbol"
  }

# This function buys a stock share at market open
def buyShareAtMarketOpens(name, count):
  market = getMarketBySymbol(name)
  if market != False:
    buy = simpleBuyStockByShare(name, count)
    return {
      "status":200,
      "message": buy
    }
  return {
      "status": 404,
      "message": "Invalid Symbol"
  }


# This function buys a fractional stock at market open
def buyFractionalAtMarketOpens(name, amount):
  market = getMarketBySymbol(name)
  if market != False:
    buy = simpleFractionalBuyStock(name, amount)
    return {
      "status":200,
      "message": buy
    }
  return {
      "status": 404,
      "message": "Invalid Symbol"
  }


# This function buys at a preset dip
def buyAtDip(name, count, price):
  market = getMarketBySymbol(name)
  if market != False:
    buy = r.order_buy_limit(name, count, price)
    return {
      "status": 200,
      "message": buy
    }
  return {
    "status": 404,
    "message": "Invalid Symbol"
  }

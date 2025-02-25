# This file contians logic to sell crypto available in RH

# Robin Stocks Library
from robin_stocks import * 
import robin_stocks.robinhood as r 

# This function sells crypto by money amount
def simpleSellCrypto(name, quantity):
  sell = r.order_sell_crypto_by_price(name, quantity)
  return sell


# This function places an order to sell crypto by coin amount
def sellCryptoOrderByQuantiyLimit(name, amount, price):
  order = r.order_sell_crypto_limit(name, amount, price, timeInForce='gtc', jsonify=True)
  return order

# This function places an order to sell crypto by money amount
def sellCryptoOrderByMoneyLimit(name, amount, price):
  order = r.order_sell_crypto_limit_by_price(name, amount, price, timeInForce='gtc', jsonify=True)
  return order


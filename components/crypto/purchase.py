# This file contains logic to buy available crypto inside RH

# Robin Stocks Library
from robin_stocks import * 
import robin_stocks.robinhood as r 


# This function buys crypto by money amount
def simpleBuyCryptoByPrice(name, quantity):
  buy = r.order_buy_crypto_by_price(name, quantity)
  return buy

# This function buys crypto by coin quantity
def simpleBuyCryptoByCoin(name, quantity):
  buy = r.order_buy_crypto_by_quantity(name, quantity)
  return buy


# This function places an order to buy crypto by coin quantity
def buyCryptoOrderByQuantityLimit(name, amount, price):
  order = r.order_buy_crypto_limit(name, amount, price, timeInForce="gtc", jsonify=True)
  return order

# This function places an order to buy crypto by money limit
def buyCryptoOrderByMoneyLimit(name, amount, price):
  order = r.order_buy_crypto_limit_by_price(name, amount, price, timeInForce="gtc", jsonify=True)
  return order

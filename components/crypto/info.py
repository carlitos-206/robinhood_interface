# This file contains functions to retrive information about crypto available inside RH

# Robin Stocks Library
from robin_stocks import * 
import robin_stocks.robinhood as r 


# This function gets latest crypto history
def getCryptoHistory(name, interval, span): 
    # Interval: ‘15second’, ‘5minute’, ‘10minute’, ‘hour’, ‘day’, or ‘week’. Default is ‘hour’.
    # Span: ‘hour’, ‘day’, ‘week’, ‘month’, ‘3month’, ‘year’, or ‘5year’. Default is ‘week’.
    # bounds:  ‘Regular’ is 6 hours a day, ‘trading’ is 9 hours a day, ‘extended’ is 16 hours a day, ‘24_7’ is 24 hours a day. Default is ‘24_7’ 
    hist = r.get_crypto_historicals(name, interval, span, bounds='24_7', info= None)
    # latest = hist[len(hist)-1]
    return hist

# This function gets the latest price of the coin
def getCryptoPrice(name):
    price = r.get_crypto_quote(name)
    return price

# This function gets all the crypto transanctions
def getAllCryptoOrderInfo():
    info = r.get_all_crypto_orders()
    return info

# This gets all open orders
def getAllOpenCryptoOders():
    orders = r.get_all_open_crypto_orders()
    return orders

# This function returns all available coing in RH 
def getAllCoins():
  info = r.get_crypto_currency_pairs()
  return info


# This function gets info of a coin by symbol
def getCoinInfo(name):
  info = r.get_crypto_info(name)
  return info


# This function gets position this is for coin that have been interacted with even if currently not own
# filter as need with float
def getCryptoPositionActive():
  info = r.get_crypto_positions()
  res = []
  for i in range(len(info)):
    for k, v in info[i].items():
      if k == 'quantity' and float(v) > 0.000000000000000000:
        res.append(info[i])
        break #This break optimizes perfomance since its n**2
  return res

# This function is to gets all position including inactive
def getAllCryptoPosition():
  info = r.get_crypto_positions()
  return info


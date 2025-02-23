# This script is for interacting with Robinhood trading service

# built in mods
import os
import time
from datetime import date, datetime, timezone
import pytz
import glob

# External  Libs
import pandas as pd
import requests

# This this the library that allows access to robinhood
from robin_stocks import * # first import the library
import robin_stocks.robinhood as r # import the

# GLOBAL PARSING FUNCTION

def globalParsing(list):
  if isinstance(list, dict):
    for k , v in list.items():
      # if isinstance(v, dict):
      #   for k, i in v.items():
      #     print(f"\n{k}: {i}\n")
      # else:
          print(f"\n{k}: {v}\n")
  else:
    print("Not Dict")
    time.sleep(2)
    print(list)
      
# ---------------------------------THIS IS THE USER PROFILE SETTINGS------------------------------------

# ------------------------------------------END--------------------------------------------------------------












# ---------------------------------THIS IS FOR BUYING AND SELLING STOCKS ------------------------------------


# This function gets the price of a share
def getSharePrice(ticker):
  price = r.get_latest_price(ticker)
  if price[0] == None:
    return {
      "status": 404,
      "Message": "Ensure ticker is correct or that is not for Crypto"
    }
  return {
    "status": 200,
    "Message": {
      "mic": ticker,
      "price": price[0]
    }
  }

# print(getSharePrice('aapl'))
# This function cancels all stock orders
def cancelAllStockOrders():
  cancel = r.cancel_all_stock_orders()
  return cancel

# This function buys stocks by share count
def simpleBuyStockByShare(name, count):
  order = r.order_buy_market(name, count)
  return order

# This function buys fractional stocks by price
def simpleFractionalBuyStock(name, amount):
  order = r.order_buy_fractional_by_price(name, amount)
  return order

# This function sells full share for stocks
def simpleShareSellStock(name, count):
  sell = r.order_sell_market(name, count)
  return sell

# This function sells fractional stocks by price
def simpleFractionalSellStock(name, amount):
  sell = r.order_sell_fractional_by_price(name, amount)
  return sell

# def getAllStocks():
#   info = r.stocks.get_all_stocks()
#   print(info)
# getAllStocks()

# This function checks if market is open
def isOpen(name):
  markets = r.markets.get_markets() # gets all the markets
  today = date.today()
  list_of_markets = []
  # this creates the list of markets
  for i in range(len(markets)):
    market = r.markets.get_market_hours(markets[i]['mic'], today) # gets market hours for today
    nextOpen = r.markets.get_market_next_open_hours(markets[i]['mic']) # gets next open hours
    # dict template
    res = {
      "Name": markets[i]['name'],
      "market": markets[i]['mic'],
      "isOpen": market["is_open"],
      "nextOpen": {
        'date': nextOpen['date'],
        'time': nextOpen['opens_at'],
        'timezone': markets[i]['timezone']
      },
      "nextClose": {
        'date': nextOpen['date'],
        'time': nextOpen['closes_at'],
        'timezone': markets[i]['timezone']
      }
    }
    list_of_markets.append(res)
  # this ensures the name is a string type before querying the api
  if name == None or isinstance(name, int):
    return False
  else:
    timezone = pytz.timezone('America/New_York') 
    string_current_time = datetime.now(timezone).strftime("%H:%M:%S") # gets current time in NY and formatted string
    string_EST_open = '9:30:00' # Market Open EST
    string_EST_close = '16:00:00' # Market Close EST
    current_time = datetime.strptime(string_current_time, "%H:%M:%S") # string to time obj
    EST_open = datetime.strptime(string_EST_open, "%H:%M:%S")
    EST_close = datetime.strptime(string_EST_close, "%H:%M:%S")
    if current_time >= EST_open and current_time <= EST_close: # compares that its between open and close before querying api
      for i in range(len(list_of_markets)):
        if list_of_markets[i]['Name'] == name: 
          return list_of_markets[i]['isOpen']
    return False # its closed

# This function gets the market in which the symbol belongs too
def getMarketBySymbol(name):
  try:
    if isinstance(name, str): # the symbol must be in string format
      share = r.stocks.find_instrument_data(name) # querys for stock in the api
      url = share[0]['market']
      res = r.get_instrument_by_url(url)
      market = res['name']
      return market
    else:
      return False # The call was empty or a int or error
  except TypeError:
    return False # The call was empty or a int or error

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




# -------------------------------------------- END ------------------------------------------------------












# ---------------------------------THIS IS FOR BUYING AND SELLING CRYPTO ------------------------------------

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
# This function buys crypto by money amount
def simpleBuyCryptoByPrice(name, quantity):
  buy = r.order_buy_crypto_by_price(name, quantity)
  return buy

# This function buys crypto by coin quantity
def simpleBuyCryptoByCoin(name, quantity):
  buy = r.order_buy_crypto_by_quantity(name, quantity)
  return buy

# This function sells crypto by money amount
def simpleSellCrypto(name, quantity):
  sell = r.order_sell_crypto_by_price(name, quantity)
  return sell

# This function cancels crypto order by ID
def cancelOrderByID(id):
  cancel = r.cancel_crypto_order(id)
  return cancel

# This function gets all the crypto transanctions
def getAllCryptoOrderInfo():
  info = r.get_all_crypto_orders()
  return info

# This gets all open orders
def getAllOpenCryptoOders():
  orders = r.get_all_open_crypto_orders()
  return orders

# This function places an order to buy crypto by coin quantity
def buyCryptoOrderByQuantityLimit(name, amount, price):
  order = r.order_buy_crypto_limit(name, amount, price, timeInForce="gtc", jsonify=True)
  return order

# This function places an order to buy crypto by money limit
def buyCryptoOrderByMoneyLimit(name, amount, price):
  order = r.order_buy_crypto_limit_by_price(name, amount, price, timeInForce="gtc", jsonify=True)
  return order

# This function places an order to sell crypto by coin amount
def sellCryptoOrderByQuantiyLimit(name, amount, price):
  order = r.order_sell_crypto_limit(name, amount, price, timeInForce='gtc', jsonify=True)
  return order

# This function places an order to sell crypto by money amount
def sellCryptoOrderByMoneyLimit(name, amount, price):
  order = r.order_sell_crypto_limit_by_price(name, amount, price, timeInForce='gtc', jsonify=True)
  return order

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


# -------------------------------------------- END ------------------------------------------------------

















# -------------------------------------------- EXPORTING INFO ------------------------------------------------------

# This function gets crypto transanctions and converts it to csv
def cryptoCSV(CURRENT_DIR, order_type, today):
  try:
    r.export_completed_crypto_orders(CURRENT_DIR, order_type)
    df_list = []
    for file_name in ["crypto.csv"]:
        file_path = os.path.join(CURRENT_DIR, file_name)
        df = pd.read_csv(file_path)
        df_list.append(df)  
    top_row = pd.DataFrame([["Crypto - Last Updated: " + today]], columns=[""])
    combined_df = pd.concat(df_list, ignore_index=True)
    combined_df = pd.concat([top_row, combined_df], ignore_index=True)
    combined_df.to_csv("crypto.csv", index=False)
    return True
  except PermissionError:
    return {
      "error": f"Close all instances of {order_type}.csv"
    }

# This function gets stocks transanctions and converts it to csv
def stockCSV(CURRENT_DIR, order_type, today):
  try:
    r.export_completed_stock_orders(CURRENT_DIR, order_type)
    df_list = []
    for file_name in ["stock.csv"]:
        file_path = os.path.join(CURRENT_DIR, file_name)
        df = pd.read_csv(file_path)
        df_list.append(df) 
    top_row = pd.DataFrame([[" Stocks - Last Updated: " + today]], columns=[""])
    combined_df = pd.concat(df_list, ignore_index=True)
    combined_df = pd.concat([top_row, combined_df], ignore_index=True)
    combined_df.to_csv("stock.csv", index=False)
    return True
  except PermissionError:
    return {
      "error": f"Close all instances of {order_type}.csv"
    }

# This function gets option transanctions and converts it to csv
def optionCSV(CURRENT_DIR, order_type, today):
  try:
    r.export_completed_option_orders(CURRENT_DIR, order_type)
    df_list = []
    for file_name in ["option.csv"]:
        file_path = os.path.join(CURRENT_DIR, file_name)
        df = pd.read_csv(file_path)
        df_list.append(df)
    top_row = pd.DataFrame([["Option - Last Updated: " + today]], columns=[""])
    combined_df = pd.concat(df_list, ignore_index=True)
    combined_df = pd.concat([top_row, combined_df], ignore_index=True)
    combined_df.to_csv("option.csv", index=False)
    return True
  except PermissionError:
    return {
      "error": f"Close all instances of {order_type}.csv"
    }

# This function gets combined transanctions and converts it to csv
def fullCSV(CURRENT_DIR,today):
  try:
    files = [cryptoCSV(CURRENT_DIR, "crypto", today), stockCSV(CURRENT_DIR, "stock", today), optionCSV(CURRENT_DIR, "option", today)]
    for i in range(len(files)):
      if i != True:
        return files[i]
    df_list = []
    for file_name in ["crypto.csv", "stock.csv", "option.csv"]:
        file_path = os.path.join(CURRENT_DIR, file_name)
        df = pd.read_csv(file_path)
        df_list.append(df)
    top_row = pd.DataFrame([["Full - Last Updated: " + today]], columns=[""])  
    combined_df = pd.concat(df_list, ignore_index=True)
    combined_df = pd.concat([top_row, combined_df], ignore_index=True)
    combined_df.to_csv("combined.csv", index=False)
    return True
  except PermissionError:
    return {
      "error": f"Close all instances of combined.csv"
    }

def completeByTypeCSV(order_type):
  CURRENT_DIR = os.getcwd()
  now = datetime.now()
  today = now.strftime("%m/%d/%Y, %H:%M:%S")
  if order_type == "crypto":
    return cryptoCSV(CURRENT_DIR, order_type, today)
  if order_type == "stock":
    return stockCSV(CURRENT_DIR, order_type, today)
  if order_type == "option":
    return optionCSV(CURRENT_DIR, order_type, today)
  if order_type == "full":
    return fullCSV(CURRENT_DIR, today)


# ------------------------------------------------- END ------------------------------------------------------










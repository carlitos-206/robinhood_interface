# This file contains logic to retrive information on stocks available in RH

from datetime import date, datetime
import pytz

# Robin Stocks Library
from robin_stocks import * 
import robin_stocks.robinhood as r 

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




# # This function gets all available stocks in RH --- avoid this function
# def getAllStocks():
#   info = r.stocks.get_all_stocks()
#   print(info)
# getAllStocks()

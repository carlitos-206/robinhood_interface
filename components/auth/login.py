# This file contains RH Login functionality

import os

# Robin Stocks Library
from robin_stocks import * 
import robin_stocks.robinhood as r 

# This function gets called for each call it does to RH
# inShort: User -> signs-in -> sends_call -> logouts -> gets_data -> User  // So far no downsides but it is inneficient -- RH might get spoofed from constant signin?
def logIn(username, password):
  username = os.getenv('RH_USERNAME') if username == None else username
  password = os.getenv("RH_PASSWORD") if password == None else password
  login = r.login(username, password)
  return login
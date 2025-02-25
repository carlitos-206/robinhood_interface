# This file contains logout functionality

import os

# Robin Stocks Library
from robin_stocks import * 
import robin_stocks.robinhood as r 


# This function logs you out
def logOut():
  r.logout()
  print('You Have succesfully logout')
  return True

logOut()
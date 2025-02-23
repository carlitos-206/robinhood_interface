import os

# This this the library that allows access to robinhood
from robin_stocks import * # first import the library
import robin_stocks.robinhood as r # import the


# This function logs you out
def logOut():
  r.logout()
  print('You Have succesfully logout')
  return True

logOut()
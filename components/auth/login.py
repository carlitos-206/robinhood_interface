import os

# This this the library that allows access to robinhood
from robin_stocks import * # first import the library
import robin_stocks.robinhood as r # import the


def logIn(username, password):
  username = os.getenv('RH_USERNAME') if username == None else username
  password = os.getenv("RH_PASSWORD") if password == None else password
  login = r.login(username, password)
  return login
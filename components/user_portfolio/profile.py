# This file contains logic to retrieve user information

# Robin Stocks Library
from robin_stocks import * 
import robin_stocks.robinhood as r 

# This function views stock holdings
def getPortolio():
  my = r.build_holdings()
  profile = r.build_user_profile()
#   for key, value in my.items():
#     print(key, value)

  return [my, profile]

# This function gets a general profile info
def getGenProfile():
  profile = r.load_account_profile()
  return profile

# This function gets crypto profile
def getCryptoProfile():
  profile = r.load_crypto_profile()
  return profile

# This function gets a gen portfolio info
def getGenPortfolio():
  profile = r.load_portfolio_profile()
  return profile

def get_user_profile():
    profile = [getGenProfile(), getPortolio(), getCryptoProfile(), getGenPortfolio()]
    return profile
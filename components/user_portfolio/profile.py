# This this the library that allows access to robinhood
from robin_stocks import * # first import the library
import robin_stocks.robinhood as r # import the

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
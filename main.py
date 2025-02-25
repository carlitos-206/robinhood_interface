import time
import threading
import os
# This this the library that allows access to robinhood
from robin_stocks import * # first import the library
import robin_stocks.robinhood as r # import the

from components.auth.login import logIn
from components.crypto.info import getCryptoPrice
from components.user_portfolio.profile import get_user_profile
from components.data_cleaners.profile_cleaner import clean_robinhood_data

def doge_coin():
    print("Starting func1")
    print(getCryptoPrice('DOGE'))
    time.sleep(7)
    print("func1 completed")

def bitcoin():
    print("Starting func2")
    print(getCryptoPrice('BTC'))
    time.sleep(7)
    
    print("func2 completed")

def etherum():
    print("Starting func3")
    print(getCryptoPrice('ETH'))
    time.sleep(7)
    
    print("func3 completed")

def func_all_done():
    print("All three functions are done. Now performing another task...")
    return main()

def user_profile():
    print('user portfolio')
    print(clean_robinhood_data(get_user_profile()))

def main():
    user = logIn(None, None)
    # Create threads for each function
    t1 = threading.Thread(target=doge_coin)
    t2 = threading.Thread(target=bitcoin)
    t3 = threading.Thread(target=etherum)
    t4 = threading.Thread(target=user_profile)
    # Start all threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    # Wait for all threads to complete
    t1.join()  
    t2.join()
    t3.join()
    t4.join()

    # Now that all threads are done, run the "trigger" function
    func_all_done()

if __name__ == "__main__":
    main()

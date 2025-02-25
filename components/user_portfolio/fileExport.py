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

from crypto.fileExport import cryptoCSV
from stocks.fileExport import stockCSV
from options.fileExport import optionCSV

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

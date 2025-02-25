# This file contains functions that export RH info to CSV files

import os

# Pandas Library
import pandas as pd

# Robin Stocks Library
from robin_stocks import * 
import robin_stocks.robinhood as r 


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

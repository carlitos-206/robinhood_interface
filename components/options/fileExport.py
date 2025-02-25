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

# This function gets option transanctions and converts it to csv
def optionCSV(CURRENT_DIR, order_type, today):
    try:
        r.export_completed_option_orders(CURRENT_DIR, order_type)
        df_list = []
        for file_name in ["option.csv"]:
            file_path = os.path.join(CURRENT_DIR, file_name)
            df = pd.read_csv(file_path)
            df_list.append(df)
        top_row = pd.DataFrame([["Option - Last Updated: " + today]], columns=[""])
        combined_df = pd.concat(df_list, ignore_index=True)
        combined_df = pd.concat([top_row, combined_df], ignore_index=True)
        combined_df.to_csv("option.csv", index=False)
        return True
    except PermissionError:
        return {
        "error": f"Close all instances of {order_type}.csv"
    }

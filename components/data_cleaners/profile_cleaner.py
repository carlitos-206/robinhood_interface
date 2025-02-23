def clean_robinhood_data(raw_data):
    """
    Cleans & structures the raw list of dictionaries/lists into a single dict.
    Converts any numeric strings to floats recursively.
    Expected structure:
      raw_data[0] -> Brokerage account details (dict)
      raw_data[1] -> List of 2 dicts; second dict has equity info
      raw_data[2] -> Nummus account details (dict)
      raw_data[3] -> Portfolio info (dict)
    """

    def convert_numeric_strings(obj):
        """
        Recursively walks the object (dict/list/primitive),
        converting numeric strings to float where possible.
        """
        if isinstance(obj, dict):
            # Recursively convert each value in the dictionary
            return {k: convert_numeric_strings(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            # Recursively convert each element in the list
            return [convert_numeric_strings(item) for item in obj]
        else:
            # If it's a string that looks like a float/int, convert it
            if isinstance(obj, str):
                try:
                    return float(obj)
                except ValueError:
                    pass  # not numeric, keep as string
            # Return as-is (bool, None, int, float, or non-numeric string)
            return obj

    # Safely parse each segment:
    brokerage_account = raw_data[0] if len(raw_data) > 0 else {}
    equity_list = raw_data[1] if len(raw_data) > 1 else []
    nummus_account = raw_data[2] if len(raw_data) > 2 else {}
    portfolio_info = raw_data[3] if len(raw_data) > 3 else {}

    # The second item is a list of two dicts, where the second dict has actual data
    equity_data = {}
    if isinstance(equity_list, list) and len(equity_list) > 1:
        equity_data = equity_list[1]  # skip the empty dict at index 0

    # Convert numeric strings to floats in each section
    brokerage_account = convert_numeric_strings(brokerage_account)
    equity_data = convert_numeric_strings(equity_data)
    nummus_account = convert_numeric_strings(nummus_account)
    portfolio_info = convert_numeric_strings(portfolio_info)

    # Package everything into a single dict
    cleaned_dict = {
        "brokerage_account": brokerage_account,
        "equities_info": equity_data,
        "nummus_account": nummus_account,
        "portfolio_info": portfolio_info
    }

    return cleaned_dict



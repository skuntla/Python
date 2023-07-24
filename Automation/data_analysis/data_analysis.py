import json

def calculate_average_daily_return(json_data):
    """
    Calculate the average daily return for each stock from the given JSON data.

    Args:
        json_data (dict): A dictionary containing trade data for different stocks.

    Returns:
        dict: A dictionary containing the average daily return for each stock, with stock symbols as keys and
              average daily returns as values. If any error occurs during calculation, returns an empty dictionary.
    """
    average_returns = {}

    try:
        for symbol, stock_data in json_data.items():
            # Extract close prices from the stock data
            close_prices = [data["close"] for data in stock_data.values()]
            previous_close = close_prices[0]

            daily_returns = []
            for close_price in close_prices[1:]:
                # Calculate the daily return as percentage change compared to the previous day's close price
                daily_return = (close_price - previous_close) / previous_close * 100
                daily_returns.append(daily_return)
                previous_close = close_price

            # Calculate the average daily return for the stock
            average_return = sum(daily_returns) / len(daily_returns)
            average_returns[symbol] = average_return

        return average_returns

    except (KeyError, ValueError, ZeroDivisionError) as e:
        print(f"Error occurred during calculation: {e}")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}

if __name__ == "__main__":
    # Assuming you have the JSON data loaded from the file
    json_data = '''
    {
      "AAPL": {
        "2023-07-01": {
          "open": 134.25,
          "high": 135.20,
          "low": 133.75,
          "close": 135.05
        },
        "2023-07-02": {
          "open": 134.90,
          "high": 136.30,
          "low": 134.75,
          "close": 136.10
        }
      },
      "GOOG": {
        "2023-07-01": {
          "open": 2715.30,
          "high": 2730.40,
          "low": 2710.10,
          "close": 2725.20
        },
        "2023-07-02": {
          "open": 2728.10,
          "high": 2745.80,
          "low": 2720.90,
          "close": 2740.50
        }
      }
    }
    '''
    json_data = json.loads(json_data)

    average_daily_return = calculate_average_daily_return(json_data)
    print(average_daily_return)

Given a JSON file that contains trade data in the following format:

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
    },
    ...
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
    },
    ...
  },
  ...
}
Write a python code function to calculate the average daily return for each stock (percentage change in "close" price compared to the previous day's "close" price) and return the result as a dictionary.

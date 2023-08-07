# StockScreener

To improve readability, some files or directories of interest inside the first folder are...
- "main.py" contains the Python code used to filter through all the stocks we want to check
- "Templates" folder holds all of the code for the webpages (HTML)
- "preferences.json" is what the JSON file sent by the homepage looks like but with whatever values the user wants
- "indexesAndExchanges" folder has .CSV files with the stock tickers associated with the option chosen (ex. All tickers in the DOW)
- "static" folder contains formatting for the website (CSS and images)


*NOTE* : This program is quite slow, so if you wish to test if it works we recommend limiting yourself to the DOW (results may take around 30 seconds).
  This is due to the quantity of statistics being checked, Python being an interpreted language, and amount of required calls to the yfinance library.
  Larger queries such as 'ALL' stocks can take up to an hour and a half depending on internet speeds.

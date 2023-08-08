# StockScreener

To improve readability, some files or directories of interest inside the first folder are...
- "main.py" contains the Python code used to filter through all the stocks we want to check
- "Templates" folder holds all of the code for the web pages (HTML)
- "preferences.json" is what the JSON file sent by the homepage looks like but with whatever values the user wants
- "indexesAndExchanges" folder has .CSV files with the stock tickers associated with the option chosen (ex. All tickers in the DOW)
- "static" folder contains the formatting for the website (CSS and images)
- "home" contains all the backend components for the landing page such as the views and their correlated URLs (Django)
- "dataHandler" contains the context processors which take user input from the landing page and convert it into JSON for processing with "main.py" and returns
  filtered data based on user's preferences. The filtered data is then passed into a generated view (dataView.html).


*NOTE*  This program is quite slow, so if you wish to test if it works we recommend limiting yourself to the DOW (results may take around 30 seconds).
  This is due to the number of statistics being checked, Python being an interpreted language, and the number of required calls to the yfinance library.
  Larger queries such as 'ALL' stocks can take up to an hour and a half depending on internet speeds.

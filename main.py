import yfinance as yf
import pandas as pd

# Benton Amon
# Basic Stock Screener


def getTickers(exchange):
    """Gathers all tickers of stocks we'd like to screen

    Args:
        exchange (str): the exchange(s) we would like to gather the tickers from

    Returns:
        List: list of all tickers we will screen
    """
    tickersList = []
    if (exchange == 'BOTH'):
        nasdaq_tickers = pd.read_csv('nasdaq_tickers.csv')
        nyse_tickers = pd.read_csv('nyse_tickers.csv')

        for index, stock in nasdaq_tickers.iterrows():
            tmp = stock['Symbol']
            if not (pd.isna(tmp)):
                if (len(tmp) < 5) and (tmp.isalpha()):
                    tickersList.append(stock['Symbol'])
        for index, stock in nyse_tickers.iterrows():
            tmp = stock['Symbol']
            if not (pd.isna(tmp)):
                if (len(tmp) < 5) and (tmp.isalpha()):
                    tickersList.append(stock['Symbol'])

    elif (exchange == 'NASDAQ'):
        nasdaq_tickers = pd.read_csv('nasdaq_tickers.csv')

        for index, stock in nasdaq_tickers.iterrows():
            tmp = stock['Symbol']
            if not (pd.isna(tmp)):
                if (len(tmp) < 5) and (tmp.isalpha()):
                    tickersList.append(stock['Symbol'])

    else:  # NYSE
        nyse_tickers = pd.read_csv('nyse_tickers.csv')

        for index, stock in nyse_tickers.iterrows():
            tmp = stock['Symbol']
            if not (pd.isna(tmp)):
                if (len(tmp) < 5) and (tmp.isalpha()):
                    tickersList.append(stock['Symbol'])

    return tickersList



# MAIN --------------------------------------------------------------------------------

# Get the exchanges the users would like to get tickers from to screen
exchange = ""
while ((exchange != 'NASDAQ') and (exchange != 'NYSE') and (exchange != 'BOTH')):
    exchange = input(
        "Enter the exchange you would like to screen...\n[NASDAQ] [NYSE] [BOTH]: ").upper()

# Gather tickers in a list
tickerList = getTickers(exchange)

print(tickerList)


# validStocks = pd.DataFrame(columns=['Ticker', 'Company Name'])

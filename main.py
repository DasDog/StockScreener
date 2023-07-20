import yfinance as yf
import pandas as pd
import json

# Basic Stock Screener
# ---------------------------------------------------------------------------

def getPreferences():
    """Loads the JSON file containing the parameters the user wishes to screen stocks for.

    Returns:
        userWants (dict): Key is each category and the Value is the user's entry.
    """
    with open('preferences.json', 'r') as f:
        userWants = json.loads(f.read())

    return userWants

# ---------------------------------------------------------------------------

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

    elif (exchange == 'NYSE'):
        nyse_tickers = pd.read_csv('nyse_tickers.csv')

        for index, stock in nyse_tickers.iterrows():
            tmp = stock['Symbol']
            if not (pd.isna(tmp)):
                if (len(tmp) < 5) and (tmp.isalpha()):
                    tickersList.append(stock['Symbol'])

    return tickersList


# MAIN --------------------------------------------------------------------------------
def main(): 
    # Get the user's preferences they would like to screen for
    userWants = getPreferences()

    # Gather tickers in a list
    # exchange: NASDAQ, NYSE, or BOTH
    tickerList = getTickers(userWants['exchange'])


    for ticker in tickerList:
        
        save = True
        try:
            stock = yf.Ticker(ticker)
            data = stock.info
            for key, value in userWants.items():
                if not (value == ""):
                    #print(data["longName"])
                    match (key):

                        case ('sector'):
                            if not (value == data['sector']):
                                save = False
                                break

                        case ('industry'):
                            if not (value == data['industry']):
                                save = False
                                break
                            
                        case ('payoutRatioMin'):
                            if not (float(value) <= data['payoutRatio']):
                                save = False
                                break
                    
                        case ('payoutRatioMax'):
                            if not (float(value) >= data['payoutRatio']):
                                save = False
                                break
                            
                            
                            
                            
                            
#//////////////////////////// Added Methods ///////////////////////////////////////////////////////////                            
                        case ("priceToBookMin"):
                            if not (float(value) <= data['priceToBook']):
                                save = False
                                break
                            
                        case ("priceToBookMax"):
                            if not (float(value) >= data['priceToBook']):
                                save = False
                                break
                            
                        case ("trailingEpsMin"):
                            if not (float(value) <= data['trailingEps']):
                                save = False
                                break
                            
                        case ("trailingEpsMax"):
                            if not (float(value) >= data['trailingEps']):
                                save = False
                                break
                            
                        case ("quickRatioMin"):
                            if not (float(value) <= data['quickRatio']):
                                save = False
                                break
                            
                        case ("quickRatioMax"):
                            if not (float(value) >= data['quickRatio']):
                                save = False
                                break
                            
                        case ("currentRatioMin"):
                            if not (float(value) <= data['currentRatio']):
                                save = False
                                break
                            
                        case ("currentRatioMax"):
                            if not (float(value) >= data['currentRatio']):
                                save = False
                                break
                            
                        case ("debtToEquityMin"):
                            if not (float(value) <= data['debtToEquity']):
                                save = False
                                break
                            
                        case ("debtToEquityMax"):
                            if not (float(value) >= data['debtToEquity']):
                                save = False
                                break
                            
                        case ("revenuePerShareMin"):
                            if not (float(value) <= data['revenuePerShare']):
                                save = False
                                break
                            
                        case ("revenuePerShareMax"):
                            if not (float(value) >= data['revenuePerShare']):
                                save = False
                                break
                            
                        case ("returnOnAssetsMin"):
                            if not (float(value) <= data['returnOnAssets']):
                                save = False
                                break
                            
                        case ("returnOnAssetsMax"):
                            if not (float(value) >= data['returnOnAssets']):
                                save = False
                                break
                            
                        case ("returnOnEquityMin"):
                            if not (float(value) <= data['returnOnEquity']):
                                save = False
                                break
                            
                        case ("returnOnEquityMax"):
                            if not (float(value) >= data['returnOnEquity']):
                                save = False
                                break
                            
                        case ("earningsGrowthMin"):
                            if not (float(value) <= data['earningsGrowth']):
                                save = False
                                break
                            
                        case ("earningsGrowthMax"):
                            if not (float(value) >= data['earningsGrowth']):
                                save = False
                                break
                            
                        case ("revenueGrowthMin"):
                            if not (float(value) <= data['revenueGrowth']):
                                save = False
                                break
                            
                        case ("revenueGrowthMax"):
                            if not (float(value) >= data['revenueGrowth']):
                                save = False
                                break
                            
                        case ("grossMarginsMin"):
                            if not (float(value) <= data['grossMargins']):
                                save = False
                                break
                            
                        case ("grossMarginsMax"):
                            if not (float(value) >= data['grossMargins']):
                                save = False
                                break
                            
                        case ("operatingMarginsMin"):
                            if not (float(value) <= data['operatingMargins']):
                                save = False
                                break
                            
                        case ("operatingMarginsMax"):
                            if not (float(value) >= data['operatingMargins']):
                                save = False
                                break
                            
                       

        # TODO: Finish the rest of the match-case statement
        # TODO: Include in the loop that if save=False STOP and go on to the next stock

                            # case ('dividendRateMin'):
                            #     if not (value <= stock['dividendRate']):
                            #         save = False
                            #         break




                        # Do nothing and go to the next stock.

            if (save):
                print("Saved!: ", data['longName'])
                
        except KeyError:
            
            save = False
            


    # validStocks = pd.DataFrame(columns=['Ticker', 'Company Name'])
    # Maybe download valid stocks from a list and put that info into excel
    
    
if __name__ == "__main__":
    main()

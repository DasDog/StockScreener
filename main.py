import yfinance as yf
import pandas as pd
import json

# Basic Fundamental Stock Screener
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

def createDf(validStocks):
    """
    Returns a dataframe of the valid stocks stored as a dictionary

    Args:
        validStocks (dict): Data of the stocks that fit the criteria inputted by the user

    Returns:
        Dataframe: A pandas dataframe of all the data in {validStocks}
    """
    
    
    return pd.DataFrame(validStocks)



# MAIN --------------------------------------------------------------------------------
def main():

    # Create the DataFrame that will store all valid stocks with basic info
    # validStocks = pd.DataFrame(columns=['Ticker', 'Company Name', 'Sector', 'Industry',
    #                            'Market Cap', 'Price', 'P/E', 'Dividend Rate', 'Analyst Recommendation'])
    
    
    
    # validStocks = pd.DataFrame(columns=['Ticker', 'Company Name', 'Sector', 'Industry', 'Market Cap', 'Price', 'P/E', 'Dividend Rate', 'Analyst Recommendation'])
    # print(validStocks)
    dictIndexKeeper = 0
    validStocksDict = {}


    # Get the user's preferences they would like to screen for
    userWants = getPreferences()

    # Gather tickers in a list
    # exchange: NASDAQ, NYSE, or BOTH
    tickerList = getTickers(userWants['exchange'])

    # Check every gathered ticker against the user's preferences
    progressCount = 0
    for ticker in tickerList:
        save = True

        # Prints how far we are in the screening process
        progressCount += 1
        progressPercent = progressCount / len(tickerList) * 100
        progressPercent = round(progressPercent, 2)
        print("Progress: ", progressCount, "/",
              len(tickerList), "... (", progressPercent, "%)")

        try:  # Try so if data cannot be grabbed it will skip the stock
            stock = yf.Ticker(ticker)
            data = stock.info

            # Check if the stock meets all of the preferences the user specified
            for key, value in userWants.items():
                if not (value == ""):

                    match (key):

                        case ('sector'):
                            if not (value == data['sector']):
                                save = False
                                break

                        case ('industry'):
                            if not (value == data['industry']):
                                save = False
                                break

                        case ('dividendRateMin'):
                            if not (float(value) <= data['dividendRate']):
                                save = False
                                break

                        case ('dividendRateMax'):
                            if not (float(value) >= data['dividendRate']):
                                save = False
                                break

                        case ('trailingPEMin'):
                            if not (float(value) <= data['trailingPE']):
                                save = False
                                break

                        case ('trailingPEMax'):
                            if not (float(value) >= data['trailingPE']):
                                save = False
                                break

                        case ('marketCapMin'):
                            if not (int(value) <= data['marketCap']):
                                save = False
                                break

                        case ('marketCapMax'):
                            if not (int(value) >= data['marketCap']):
                                save = False
                                break

                        case ('priceToSalesTrailing12MonthsMin'):
                            if (isinstance(data['priceToSalesTrailing12Months'], float)):
                                if not (float(value) <= data['priceToSalesTrailing12Months']):
                                    save = False
                                    break
                            else:
                                save = False
                                break

                        case ('priceToSalesTrailing12MonthsMax'):
                            if (isinstance(data['priceToSalesTrailing12Months'], float)):
                                if not (float(value) >= data['priceToSalesTrailing12Months']):
                                    save = False
                                    break
                            else:
                                save = False
                                break

                        case ('profitMarginsMin'):
                            if not (float(value) <= data['profitMargins']):
                                save = False
                                break

                        case ('profitMarginsMax'):
                            if not (float(value) >= data['profitMargins']):
                                save = False
                                break

                        case ('bookValueMin'):
                            if not (float(value) <= data['bookValue']):
                                save = False
                                break

                        case ('bookValueMax'):
                            if not (float(value) >= data['bookValue']):
                                save = False
                                break

                        case ('priceToBookMin'):
                            if not (float(value) <= data['priceToBook']):
                                save = False
                                break

                        case ('priceToBookMax'):
                            if not (float(value) >= data['priceToBook']):
                                save = False
                                break

                        case ('trailingEpsMin'):
                            if not (float(value) <= data['trailingEps']):
                                save = False
                                break

                        case ('trailingEpsMax'):
                            if not (float(value) >= data['trailingEps']):
                                save = False
                                break

                        case ('quickRatioMin'):
                            if not (float(value) <= data['quickRatio']):
                                save = False
                                break

                        case ('quickRatioMax'):
                            if not (float(value) >= data['quickRatio']):
                                save = False
                                break

                        case ('currentRatioMin'):
                            if not (float(value) <= data['currentRatio']):
                                save = False
                                break

                        case ('currentRatioMax'):
                            if not (float(value) >= data['currentRatio']):
                                save = False
                                break

                        case ('debtToEquityMin'):
                            if not (float(value) <= data['debtToEquity']):
                                save = False
                                break

                        case ('debtToEquityMax'):
                            if not (float(value) >= data['debtToEquity']):
                                save = False
                                break

                        case ('revenuePerShareMin'):
                            if not (float(value) <= data['revenuePerShare']):
                                save = False
                                break

                        case ('revenuePerShareMax'):
                            if not (float(value) >= data['revenuePerShare']):
                                save = False
                                break

                        case ('returnOnAssetsMin'):
                            if not (float(value) <= data['returnOnAssets']):
                                save = False
                                break

                        case ('returnOnAssetsMax'):
                            if not (float(value) >= data['returnOnAssets']):
                                save = False
                                break

                        case ('returnOnEquityMin'):
                            if not (float(value) <= data['returnOnEquity']):
                                save = False
                                break

                        case ('returnOnEquityMax'):
                            if not (float(value) >= data['returnOnEquity']):
                                save = False
                                break

                        case ('earningsGrowthMin'):
                            if not (float(value) <= data['earningsGrowth']):
                                save = False
                                break

                        case ('earningsGrowthMax'):
                            if not (float(value) >= data['earningsGrowth']):
                                save = False
                                break

                        case ('revenueGrowthMin'):
                            if not (float(value) <= data['revenueGrowth']):
                                save = False
                                break

                        case ('revenueGrowthMax'):
                            if not (float(value) >= data['revenueGrowth']):
                                save = False
                                break

                        case ('grossMarginsMin'):
                            if not (float(value) <= data['grossMargins']):
                                save = False
                                break

                        case ('grossMarginsMax'):
                            if not (float(value) >= data['grossMargins']):
                                save = False
                                break

                        case ('operatingMarginsMin'):
                            if not (float(value) <= data['operatingMargins']):
                                save = False
                                break

                        case ('operatingMarginsMax'):
                            if not (float(value) >= data['operatingMargins']):
                                save = False
                                break

            """
            *********************** READ ME ****************************

            What I'm trying to do below after we check all the user's preferences
            and determine the stock should be saved is create a data frame with all
            info we need to properly fill in the table, then adding it to the original
            by using .concat() to stick "dfTemp" into what will be the final data frame
            "validStocks" (validStocks is created in line 73).

            What I have here has not been tested and we need to make sure that if we cannot
            get a certain piece of data we fill in N/A or something instead of erroring
            or skipping the stock (it has been determined valid so we can't just skip it
            like we did in the screening process). Since where we are trying to make this
            data frame is still inside of that try-catch I think we are going to run into
            issues where stocks will be missing from the spreadsheet because one of these
            data entries could not be found.

            I added a new file in GitHub called dataFrameExample that you should look at.

            NOTE: If you see something online saying use .append(), it's outdated and that
            is no longer a thing. Concat() seemed like the way to go when I was looking
            stuff up.

            Good luck, soldier.

            """

            # If stock passes all preferences, save it
            if (save):

                                
                                
                """
                This is the handler for the dictionary if a stock is saved then its related data 
                is added to dict at the index (dictIndexKeeper) there were some issues with a stock being 
                added twice so I had to use the conditionals to prevent this.
                """
                                
                                
                values = validStocksDict.values()
                if len(values) != 0:
                    if data['symbol'] not in values:
                        validStocksDict[dictIndexKeeper] = {'Ticker': data['symbol'],
                                    'Company Name': data['longName'],
                                    'Sector': data['sector'],
                                    'Industry': data['industry'],
                                    'Market Cap': data['marketCap'],
                                    'Price': data['currentPrice'],
                                    'P/E': data['trailingPE'],
                                    'Dividend Rate': data['dividendRate'],
                                    'Analyst Recommendation': data['recommendationKey']
                                    }

                        print("Added: ", data['symbol'], "Index: ", dictIndexKeeper)
                        dictIndexKeeper += 1
                else:
                        validStocksDict[dictIndexKeeper] = {'Ticker': data['symbol'],
                                    'Company Name': data['longName'],
                                    'Sector': data['sector'],
                                    'Industry': data['industry'],
                                    'Market Cap': data['marketCap'],
                                    'Price': data['currentPrice'],
                                    'P/E': data['trailingPE'],
                                    'Dividend Rate': data['dividendRate'],
                                    'Analyst Recommendation': data['recommendationKey']
                                    }
                        print("Added: ", data['symbol'], "Index: ", dictIndexKeeper)
                        dictIndexKeeper += 1

                
        except KeyError:
            save = False
            # Do nothing and screen the next stock, this one is missing data.
            
    # Creates the DF for all valid stocks in the dictionary
    validStocksDf = createDf(validStocksDict)
    print(validStocksDf)

# -----------------------------------------------------------------------------------------

# Run the program
if __name__ == "__main__":
    main()

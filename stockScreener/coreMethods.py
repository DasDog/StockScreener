import yfinance as yf
import json as js
import simpleMethods

# Darin Renusch


"""
    Processes settings.json file and 
    returns a dictionary of (ticker: yFinance obj.)

"""    

def processSettings():
    
    with open("settings.json", "r") as settings :
        
        asDict = js.load(settings)
        tickersLoaded = {}
        for tickers in asDict['tickers']:
            tickersLoaded[tickers] = yf.Ticker(tickers)
            
    
    return tickersLoaded

"""
    Calls and prints ALL info on the given {ticker}
    so long as it is loaded in {tickers}

"""

def callTickerData(ticker, tickers):
    
    try:
        yFinanceObj = tickers[ticker]
        tickerData = yFinanceObj.info
        
        for keys in tickerData.items():
            print(keys, '\n')
            
    except KeyError:
        
        print("This ticker is not loaded! Please modify the settings.json file to call this ticker.")
        
    
    

def main():
    
    workingTickers = processSettings()
    simpleMethods.longShortMean("MSFT", workingTickers)
    
    

if __name__ == "__main__":
    main()
            


processSettings()
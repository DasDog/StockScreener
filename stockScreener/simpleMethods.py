import yfinance as yf
import json as js


def processData(data):
    
    ret = {}
    z = 0
    for k,i,j  in zip(data.index, data['High'], data['Close']):
        
        ret[z] = {'date': k, 'high': i, 'close': j}
        z += 1
    
    return ret

"""
    Calculates SMA for the specified time period {days}
    given {closePrices} of a particular stock.
        
"""

def calculateSMA(closePrices, days):
    
    sma = 0
    
    for i in range(len(closePrices)):
        sma += closePrices[i]["close"]
    
    return (sma/days)

"""
    Gets and returns 30 day historical data for {stock}
        
"""
def getThirtyDayData(stock, tickers):
    
    yFinanceObj = tickers[stock]
    return yFinanceObj.history(period="30d")
    
"""
    Gets and returns 10 day historical data for {stock}
        
"""
def getTenDayData(stock, tickers):
    yFinanceObj = tickers[stock]
    return yFinanceObj.history(period="10d")


"""
    Uses 30 day and 10 ten day SMAs to 
    determine a bullish or bearish sentiment
    on {stock}

"""

def longShortMean(stock, tickers):
    tenDayData = getTenDayData(stock, tickers)
    thirtyDayData = getThirtyDayData(stock, tickers)
    
    cleanTenDay = processData(tenDayData)
    cleanThirtyDay = processData(thirtyDayData)
    
    tenSma = calculateSMA(cleanTenDay, 10)
    thirtySma = calculateSMA(cleanThirtyDay, 30)
    
    percent_difference = (tenSma - thirtySma) / thirtySma
    
    if percent_difference > 0.08:
        print("Go short!")
        
    elif percent_difference < -.08:
        print("Go Long!")
    else:
        print("Indifferent")
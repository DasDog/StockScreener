import yfinance as yf

stock = yf.Ticker('MSFT')
data = stock.info

for key, value in data.items():
    print(key, ": ", value)
import yfinance as yf

stock = yf.Ticker('AMC')
data = stock.info

tmp = data['recommendationKey']
tmp = tmp.capitalize()

print(tmp)

#AMC underperform
#GME underperform
from django.shortcuts import render
from .UserDataFrame import DataContext

# Create your views here.



def dataToHtml(request):
    
    row = DataContext(request)
    row  = row.populateDataContext()

    tickers = row['Ticker'].values()
    companies = row['Company Name'].values()
    sectors = row['Sector'].values()
    industry = row['Industry'].values()
    mCap = row['Market Cap'].values()
    price = row['Price'].values()
    pE = row['P/E'].values()
    dRate = row['Dividend Rate'].values()
    aRec = row['Analyst Recommendation'].values()
    
    
    
    return render(request, 'dataPage/dataView.html', {
        'Tickers': tickers, 
        'companyName': companies,
        'Sectors': sectors,
        'Industry': industry,
        'marketCap': mCap,
        'Price': price,
        'PE': pE,
        'Dividend': dRate,
        'recommend':aRec })
    
    
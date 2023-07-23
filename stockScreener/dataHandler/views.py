from django.shortcuts import render
from .UserDataFrame import DataContext

# Create your views here.



def dataToHtml(request):
    
    data = DataContext(request)
    data  = data.populateDataContext()
    
    return render(request, 'dataPage/dataView.html', {'stocks': data})
    
    
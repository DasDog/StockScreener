from django.shortcuts import render
import pandas as pd
from main import main


def landPage(request):
    
    context = {}
    return render(request, 'home/index.html', context)

def dataPage(request):
    
    context = {}
    data = main()
    
    for key in data:
        
        context[key] = data[key].values()
        print(context[key], key)
    
    return render(request, 'home/dataView.html', context)
    




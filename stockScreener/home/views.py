from django.shortcuts import render, redirect
from dataHandler.views import dataToHtml
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def landPage(request):
    
    context = {}
    
    return render(request, 'home/index.html', context)





    
    

    




from django.shortcuts import render, redirect
from dataHandler.views import dataToHtml
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def refreshSectorView(request):
    
    return redirect("landPage", context = {'I': '1'})

@csrf_exempt
def landPage(request):
    
    context = {'I': 0}
     
    if request.POST.get('Sector') == 'Basic Materials':
        
        context = {'I': 1}
        
        return redirect("home:home", context)
    
    return render(request, 'home/index.html', context)





    
    

    




from django.shortcuts import render
from main import main


def landPage(request):
    
    context = {}
    return render(request, 'home/index.html', context)

    




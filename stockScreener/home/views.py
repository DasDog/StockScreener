from django.shortcuts import render


def landPage(request):
    context = {}
    return render(request, 'home/index.html', context)

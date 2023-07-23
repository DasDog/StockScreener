from django.urls import path
from .views import dataToHtml

urlpatterns = [
    
    path('loadedData/', dataToHtml, name='ReturnedData'),
    
]
from django.urls import path
from .views import dataToHtml, captureJson

urlpatterns = [
    
    path('loadedData/', dataToHtml, name='ReturnedData'),
    path('captureData/', captureJson, name= 'captureJson'),

    
]
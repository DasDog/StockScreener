from django.urls import path
from .views import landPage, dataPage

urlpatterns = [
    
    path('', landPage, name='home'),
    path('userStocks', dataPage, name='validStocks'),
    
]
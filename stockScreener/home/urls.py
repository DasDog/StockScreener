from django.urls import path
from .views import landPage

urlpatterns = [
    
    path('', landPage, name='home')
    
]
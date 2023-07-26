from django.urls import path
from .views import landPage, refreshSectorView

urlpatterns = [
    
    path('', landPage, name='home'),
    path('Sector/', refreshSectorView, name='sectorSelect')
    
]
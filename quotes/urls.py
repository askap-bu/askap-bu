#file name: quotes/urls.py
# description: direct url requests to view functions

from django.urls import path
from .views import HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
  
]
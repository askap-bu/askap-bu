#file name: quotes/urls.py
# description: direct url requests to view functions

from django.urls import path
from .views import * #HomePageView, QuotePageView, RandomQuotePageView, PersonPageView


urlpatterns = [
    path('', RandomQuotePageView.as_view(), name ="random"),
    path('all', HomePageView.as_view(), name='home'),
    path('quote/<int:pk>', QuotePageView.as_view(), name='quote'), 
    path('person/<int:pk>', PersonPageView.as_view(), name='person'),
]
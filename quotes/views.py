from django.shortcuts import render

# Create your views here.
from .models import Quote 
from django.views.generic import ListView

class HomePageView(ListView):
    """ create a subclass of listview to display all quotes"""

    model= Quote #retreive pbjects of type quote from thr database
    template_name= 'quotes/home.html'
    context_object_name = 'all_quotes_list'

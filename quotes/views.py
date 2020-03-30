from django.shortcuts import render
import random
# Create your views here.
from .models import Quote 
from django.views.generic import ListView, DetailView

class HomePageView(ListView):
    """ create a subclass of listview to display all quotes"""

    model= Quote #retreive pbjects of type quote from thr database
    template_name= 'quotes/home.html'
    context_object_name = 'all_quotes_list'

class QuotePageView(DetailView):
    """show the details for one quote"""
    model = Quote 
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'

class RandomQuotePageView(DetailView):
    """show the details for one quote selected at random"""
    model = Quote 
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'

    def get_object(self):
        """return a single instance of a quote object, selected at random"""

        #get all quotes 
        all_quotes = Quote.objects.all()

        # pick one, at random
        r = random.randint(0,len(all_quotes)-1)
        q = all_quotes[r]
        return q
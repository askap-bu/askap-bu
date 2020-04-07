from django.shortcuts import render
import random
from django.urls import reverse

from .models import Quote, Person
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CreateQuoteForm, UpdateQuoteForm, AddImageForm
from django.urls import reverse 
from django.shortcuts import redirect

# Create your views here.
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

class PersonPageView(DetailView):
    """show all quotes and all images for one person"""
    model= Person
    template_name = 'quotes/person.html'
    #context_object_name = 'person'

    def get_context_data(self, **kwargs):
        ''' Return a dictionary with context data for this template to use'''
        context = super(PersonPageView,self).get_context_data(**kwargs)
        add_image_form = AddImageForm()
        context['add_image_form']= add_image_form
        return context 
        
class CreateQuoteView(CreateView):
    """ a view to create a new quote and save it ot the database"""

    form_class= CreateQuoteForm
    template_name = 'quotes/create_quote.html'

class UpdateQuoteView(CreateView):
    """ a view to update a quote and save it ot the database"""

    form_class= UpdateQuoteForm
    template_name = 'quotes/update_quote.html'
    queryset = Quote.objects.all()

class DeleteQuoteView(DeleteView):
    """ a view to delete a quote """

    template_name = 'quotes/delete_quote.html'
    queryset = Quote.objects.all()
    #success_url = "../../all"

    def get_success_url(self):
        """return to the urls which we shoudl be directed to on delete"""
        # get pk for this quote
        pk = self.kwargs.get('pk')
        quote= Quote.objects.filter(pk=pk).first()
        
        # find the person asspciated with the quote 
        person = quote.person 
        return reverse('person', kwargs={'pk':person.pk}) #this is a dictionary and im choosing the person onject and thier pk

def add_image(request, pk):
    ''' a custom view function to handle the submission of an image uplaod'''
    # find the person 
    person = Person.objects.get(pk=pk)

    # read request data imnto addimageform object 
    form = AddImageForm(request.POST or None, request.FILES or None)

    #check if the form is valid
    if form.is_valid():
        image = form.save(commit = False)
        image.person = person 
        image.save()

    else: 
        print("Error: the form was not valid.")

    #redirect to a new url, display person page 
    url = reverse('person', kwargs={'pk':person.pk})
    return redirect(url)
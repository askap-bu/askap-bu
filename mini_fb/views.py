from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile, StatusMessage
from .forms import CreateProfileForm, UpdateProfileForm, CreateStatusMessageForm
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.

class ShowAllProfilesView(ListView):
    """ create a subclass of listview to display all profiles"""

    model= Profile 
    template_name= 'mini_fb/show_all_profiles.html'
    context_object_name = 'show_all_profiles'

class ShowProfilePageView(DetailView):
    """ create a subclass of detailview to display one profile"""

    model= Profile 
    template_name= 'mini_fb/show_profile_page.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record for this page view
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = CreateStatusMessageForm()
        context['create_status_form'] = form
        # return this context dictionary
        return context

def create_status_message(request, pk):
        '''Process a form submission to post a new status message.'''
        # find the profile that matches the `pk` in the URL
        profile = Profile.objects.get(pk=pk)

        # if and only if we are processing a POST request, try to read the data
        if request.method == 'POST':

            # read the data from this form submission
            message = request.POST['message']

            # save the new status message object to the database
            if message:

                sm = StatusMessage()
                sm.profile = profile
                sm.message = message
                sm.save()

        # redirect the user to the show_profile_page view
        return redirect(reverse('profile', kwargs={'pk': pk}))









class CreateProfileView(CreateView):
    ''' subclass of createview to display form to make a profile'''
    form_class= CreateProfileForm
    template_name='mini_fb/create_profile_form.html'
    #queryset = Profile.objects.all()

class UpdateProfileView(UpdateView):
    form_class= UpdateProfileForm
    template_name = 'mini_fb/update_profile_form.html'
    queryset = Profile.objects.all()
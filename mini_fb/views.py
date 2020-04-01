from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile
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
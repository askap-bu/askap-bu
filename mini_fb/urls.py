#file name: mini_fb/urls.py
# description: direct url requests to view functions

from django.urls import path
from .views import ShowAllProfilesView


urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name='show_all_profiles'),
]
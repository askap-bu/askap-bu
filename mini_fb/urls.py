#file name: mini_fb/urls.py
# description: direct url requests to view functions

from django.urls import path
from .views import ShowAllProfilesView, ShowProfilePageView, CreateProfileView, UpdateProfileView, create_status_message


urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='profile'),
    path('create', CreateProfileView.as_view(), name ='create_profile'),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name ='update_profile'),
    path('profile/<int:pk>/post_status', create_status_message, name ='post_status'),
]

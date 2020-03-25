from django.urls import path
from .views import homePageView #AboutPageView, SchedulePageView

urlpatterns = [
    path('', homePageView, name='home'),    
]
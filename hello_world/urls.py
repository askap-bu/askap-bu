from django.urls import path
from .views import homePageView #AboutPageView, SchedulePageView

urlpatterns = [
    path('', homePageView, name='home'),
    #path('about', AboutPageView(), name ="about"),
    #path("schedule", SchedulePageView)
]
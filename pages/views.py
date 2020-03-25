#file name: pages/views/html
#Description: provide a view to send to the user


from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    """ A specialized version of templateview to display our homepage"""

    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    """ A specialized version of templateview to display our about page"""

    template_name = "pages/about.html"

class SchedulePageView(TemplateView):
    """ A specialized version of templateview to display our about page"""

    template_name = "pages/schedule.html"
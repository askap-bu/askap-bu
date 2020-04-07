# quotes/forms.py

from django import forms
from .models import Quote, Image 

class CreateQuoteForm(forms.ModelForm):
    """ a form to add new quotes to the database"""

    class Meta:
        '''associate this form with the Qutoe model'''
        model = Quote 
        fields = ['person', 'text',]

class UpdateQuoteForm(forms.ModelForm):
    """ a form to editquotes to the database"""

    class Meta:
        '''associate this form with the Quote model'''
        model = Quote 
        fields = ['person', 'text',]


class AddImageForm(forms.ModelForm):
    """ a form to collect an image to the user"""

    class Meta: 
        model = Image
        fields = ["image_file",]
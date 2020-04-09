# minifb/forms 
from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
    """ a form to create a new profile"""
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2020,1920,-1),),)
    email_address = forms.CharField(label="Email Address", required=True)
    city = forms.CharField(label="City", required=True)
    profile_image_url = forms.CharField(label="Profile Image Url", required=True)

    class Meta:
        model = Profile 
        fields = ['first_name', 'last_name','email_address','birth_date', 'city','profile_image_url',]

class UpdateProfileForm(forms.ModelForm):
    ''' update an existing form'''
    #first_name = forms.CharField(label="First Name", required=True)
    #last_name = forms.CharField(label="Last Name", required=True)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2020,1920,-1),),)
    email_address = forms.CharField(label="Email Address", required=True)
    city = forms.CharField(label="City", required=True)
    profile_image_url = forms.CharField(label="Profile Image Url", required=True)

    class Meta:
        model = Profile 
        fields = ['email_address','birth_date', 'city','profile_image_url',]

class CreateStatusMessageForm(forms.ModelForm):
    ''' creates a message form'''
    image= forms.ImageField(required=False)

    class Meta:
        '''associate this form with the StatusMessage model'''
        model = StatusMessage 
        fields =['message', 'image']
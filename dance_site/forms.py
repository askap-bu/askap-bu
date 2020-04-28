# File name: forms.py 
# Author: Andriana Skaperdas (askap@bu.edu)
# Description: Holds the forms to create a class and update a student


from django import forms
from .models import Student, Class, Teacher

class CreateClassForm(forms.ModelForm):
    """ a form to create a new class"""
    class_name = forms.CharField(label="Class Name", required=True)
    day = forms.CharField(label="Day", required=True)
    price = forms.CharField(label="City", required=True)
    class_picture = forms.CharField(label="Profile Image Url", required=True)
    #teacher

    class Meta:
        model = Class
        fields = ['class_picture','class_name', 'day','price','teacher', ]


class UpdateStudentForm(forms.ModelForm):
    ''' update an existing student'''
    #first_name = forms.CharField(label="First Name", required=True)
    #last_name = forms.CharField(label="Last Name", required=True)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2020,1920,-1),),)
    email_address = forms.CharField(label="Email Address", required=True)
    city = forms.CharField(label="City", required=True)
    profile_image_url = forms.CharField(label="Profile Image Url", required=True)

    class Meta:
        model = Student 
        fields = ['email_address','birth_date', 'city','profile_image_url',]





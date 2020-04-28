# File name: models.py 
# Author: Andriana Skaperdas (askap@bu.edu)
# Description: Holds all the data models for the dance site including Student, Class, and Teacher

from django.db import models
from django.urls import reverse
# Create your models here.

class Student(models.Model):
    '''holds the data attributes of a dance student'''

    #data attributes of profile 
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank= True)
    city = models.TextField(blank= True)
    email_address = models.TextField(blank= True)
    profile_image_url = models.URLField(blank=True)
    birth_date = models.DateField(blank=True)
    classes_taken = models.ManyToManyField('Class', blank=False )   # classes they are enrolled in

    def __str__(self):
        """return  a string represenation of this object"""
        return  '%s, %s' %(self.first_name, self.last_name)


    def get_classes(self):
        """obtain and return classes"""
        return self.classes_taken.all()
         

    def get_absolute_url(self):
        '''return a url to display this student object'''
        return reverse('student', kwargs={"pk": self.pk })


    def get_class_suggestions(self):
        """obtain and return a qset of all classes that could be added """
        class_s= self.get_classes()
        possible_classes = Class.objects.all().exclude(pk__in=self.get_classes()).exclude(pk=self.pk)
        return possible_classes

    def get_rows(self):
        """get the number rows i need to display"""
        count= len(Student.objects.all())
        rows= count//3
        if count%3==0:
            rows=count//3
            rows=[1 for x in range(rows)]
        else:
            rows= count//3+1
            rows=[1 for x in range(rows)]
        return rows
    
    def get_cols(self):
        """get the number cols i need to display"""
        cols=[0,1,2]
        return cols
        
    def list_of_lists(self):
        """create a sublist for  all the students"""
        list_tot=[]
        list_int=[]
        count = 0 
        for p in people:
            people=list(Student.objects.all())
            if len(list_int) < 3:
                list_int.append(p)
                if len(list_int) == 3:
                    list_tot.append(list_int)
                    list_int=[]
                if people[count]==people[(len(people)-1)]:# there are no more people, append              
                    list_tot.append(list_int)
                count += 1
            return list_tot    



        

class Teacher(models.Model):
    '''holds the data attributes of a dance teacher'''

    #data attributes of profile 
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank= True)
    city = models.TextField(blank= True)
    email_address = models.TextField(blank= True)
    profile_image_url = models.URLField(blank=True)
    birth_date = models.DateField(blank=True)
    #teaches_taught = models.ForeignKey("Class", on_delete=models.CASCADE, blank=False, null=True)  # classes they teach

    def get_classes(self):
        '''classes that they teach'''
        teaches=Class.objects.filter(teacher=self)
        return teaches

    def __str__(self):
        """return a string represenation of this object"""
        return  '%s, %s' %(self.first_name, self.last_name)

class Class(models.Model): 
    '''holds the attributes of a dance class'''
    day= models.TextField(blank=True)  
    class_name = models.TextField(blank=True)
    class_picture = models.URLField(blank=True)   
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, blank=True, null=True)
    price= models.TextField(blank=True)

    def __str__(self):
        """return  a string represenation of this object"""
        return  '%s' %(self.class_name)
    
    def get_absolute_url(self):
        '''return a url to bring you back to the all classes'''
        return reverse('show_all_classes')
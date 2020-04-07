from django.db import models
from django.urls import reverse
import random
 
# Create your models here.
class Person(models.Model):
    """ encapsulates the co cept of  aperson, who said famous quote"""
    name = models.TextField(blank=False)

    def __str__(self):
        """return a string representation of a quote"""
        return self.name

    def get_random_image(self):  # get image at random
        """return a random image"""

        #get all images of this person 
        images = Image.objects.filter(person=self.pk)
        
        #chose a random image
        i = random.randint(0, len(images)-1)
        return images[i]

    def get_all_images(self):  #get all images for this person 
        """ return a query of all images for this person"""
        
        images = Image.objects.filter(person=self.pk)
        return images 
    
    def get_all_quotes(self): #get all quotes for this person
        """ return a queryset of a;; quotes for this person"""
        
        quotes = Quote.objects.filter(person=self.pk)
        return quotes 
                        

class Quote(models.Model):
    """ encapsulate the idea of a quote"""

    #data attributesof quote 
    text = models.TextField(blank=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

    def __str__(self):
        """return  a string represenation of this object"""
        return ' "%s" - %s' % (self.text, self.person.name)

    def get_absolute_url(self):
        '''return a url to display this quote object'''
        return reverse("quote", kwargs={"pk": self.pk })


class Image(models.Model):
    """represent an image that is a associated with a person"""
    image_url = models.URLField(blank=True)
    image_file= models.ImageField(blank = True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
 
    def __str__(self):
        """return  a string represenation of this object"""
        if self.image_url:
            return self.image_url
        else: 
            return self.image_file.url
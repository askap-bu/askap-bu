from django.db import models


# Create your models here.

class Quote(models.Model):
    """ encapsulate the idea of a quote"""

    #data attributesof quote 
    text = models.TextField(blank=True)
    author = models.TextField(blank= True)
    image_url = models.URLField(blank=True)

    def __repr__(self):
        """return  a string represenation of this object"""
        return ' "%s" - %s' % (self.text, self.author)
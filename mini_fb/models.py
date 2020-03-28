from django.db import models

# Create your models here.
 
class Profile(models.Model):
    """ encapsulate the idea of a quote"""

    #data attributesof quote 
    fname = models.TextField(blank=True)
    lname = models.TextField(blank= True)
    city = models.TextField(blank= True)
    email = models.TextField(blank= True)
    profile_image = models.URLField(blank=True)

    def __str__(self):
        """return  a string represenation of this object"""
        return  '%s, %s,%s,%s,%s' %(self.fname, self.lname, self.city, self.email, self.profile_image)
        
       
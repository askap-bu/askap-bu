from django.db import models

# Create your models here.
 
class Profile(models.Model):
    """ encapsulate the idea of a quote"""

    #data attributesof quote 
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank= True)
    city = models.TextField(blank= True)
    email_address = models.TextField(blank= True)
    profile_image_url = models.URLField(blank=True)

    def __str__(self):
        """return  a string represenation of this object"""
        return  '%s, %s,%s,%s,%s' %(self.first_name, self.last_name, self.city, self.email_address, self.profile_image_url)
        
       
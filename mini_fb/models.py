from django.db import models

# Create your models here.
 
class Profile(models.Model):
    """ encapsulate the idea of a quote"""

    #data attributes of quote 
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank= True)
    city = models.TextField(blank= True)
    email_address = models.TextField(blank= True)
    profile_image_url = models.URLField(blank=True)
    

    def __str__(self):
        """return  a string represenation of this object"""
        return  '%s, %s' %(self.first_name, self.last_name)

    def get_status_messages(self):
        statusmessages = StatusMessage.objects.filter(profile=self.pk)
        return statusmessages


class StatusMessage(models.Model):
    """ model data attributes of a facebook status message"""
    timestamp = models.TimeField(auto_now_add=True)
    message= models.TextField(blank=True)
    profile= models.ForeignKey('Profile', on_delete=models.CASCADE)


    def __str__(self):
        return '%s, %s' %(self.timestamp, self.message)

from django.db import models
from django.urls import reverse
import datetime

# Create your models here.
 
class Profile(models.Model):
    """ encapsulate the idea of a profile"""

    #data attributes of profile 
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank= True)
    city = models.TextField(blank= True)
    email_address = models.TextField(blank= True)
    profile_image_url = models.URLField(blank=True)
    birth_date = models.DateField(blank=False)
    friends = models.ManyToManyField("self")

    def get_friends(self):
        """ will return a qset of all friends fro this profile"""
        friend= self.friends.exclude(pk=self.pk)
        return friend

    def get_news_feed(self):
        friends= self.get_friends()
        """obtain and return news feed items"""
        #newsfeed = StatusMessage.objects.all().order_by("-timestamp") #should i made that Profile instead
        newsfeed = StatusMessage.objects.filter(profile__in=self.get_friends()).order_by("-timestamp")
        return newsfeed


    def get_friend_suggestions(self):
        """obtain and return a qset of all profile that could be added as friends"""
        friends= self.get_friends()
        possible_friends = Profile.objects.all().exclude(pk__in=self.get_friends()).exclude(pk=self.pk)
        return possible_friends


    def __str__(self):
        """return  a string represenation of this object"""
        return  '%s, %s' %(self.first_name, self.last_name)

    def get_status_messages(self):
        statusmessages = StatusMessage.objects.filter(profile=self.pk)
        return statusmessages

    def get_absolute_url(self):
        '''return a url to display this profile object'''
        return reverse('profile', kwargs={"pk": self.pk })

class StatusMessage(models.Model):
    """ model data attributes of a facebook status message"""
    timestamp = models.TimeField(auto_now_add=True)
    message= models.TextField(blank=True)
    profile= models.ForeignKey('Profile', on_delete=models.CASCADE)
    image= models.ImageField(blank=True)

    def __str__(self):
        return '%s, %s, %s' %(self.timestamp, self.message, self.image)

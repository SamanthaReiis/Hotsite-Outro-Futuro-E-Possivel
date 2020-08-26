from django.db import models
import os
from django.conf import settings
from django.utils import timezone
from  embed_video.fields  import  EmbedVideoField


def get_image_path(instance, filename):
    return os.path.join('static/hotsite/img', str(instance.id), filename)


class  Item ( models.Model ): 
    video  =  EmbedVideoField () 

    def publish(self):
        self.video =  EmbedVideoField()
        self.save()



class Podcast (models.Model):
    podcast = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.CharField(max_length=200)

    def publish(self):
        self.podcast = models.ImageField(upload_to=get_image_path, blank=True, null=True)
        self.save()

    def __init__(self, arg):
        super(Podcast , self).__init__()
        self.arg = arg

class Storie (models.Model):
    storie = EmbedVideoField()
    title = models.CharField(max_length=200)
    text = models.TextField()

    def publish(self):
        self.storie =  EmbedVideoField()
        self.save()

    def __init__(self, arg):
        super(Storie , self).__init__()
        self.arg = arg
                        



class Report (models.Model):
    photo = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    text = models.TextField()
   
   
    def get_image_path(instance, filename):
      return os.path.join('static/img', str(instance.id), filename)
    

    def publish(self):
        self.photo = models.ImageField(upload_to=get_image_path, blank=True, null=True)
        self.save()

    def __str__(self):
        return self.title
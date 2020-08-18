from django.db import models
import os
from django.conf import settings
from django.utils import timezone

# Create your models here.

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Report (models.Model):
    photo = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    link = models.URLField(max_length=250)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    text = models.TextField()
   
   

    def publish(self):
        self.photo = models.ImageField(upload_to=get_image_path, blank=True, null=True)
        self.save()

    def __str__(self):
        return self.title
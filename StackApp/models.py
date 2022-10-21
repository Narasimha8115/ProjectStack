from datetime import datetime
from distutils.command.upload import upload
from email.policy import default
from tkinter import CASCADE
from turtle import title
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class Projectss(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.TextField()
    images_one = models.ImageField(upload_to = 'projects/images_one',default="" )
    images_two = models.ImageField(upload_to = 'projects/images_two',default="" )
    images_three = models.ImageField(upload_to = 'projects/images_three',default="" )
    videos = models.FileField(upload_to = 'projects/videos')
    created_at = models.DateField(default = datetime.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default="")



    def __str__(self):
        return self.title


class Profile_Up(models.Model):
    fullname=models.ForeignKey(User,on_delete=models.CASCADE)
    #Email=models.CharField(User,max_length=50,default="")
    phone=models.CharField(max_length=10,default="")
    profession=models.CharField(max_length=100,default="")
    inst_or_org=models.CharField(max_length=100,default="")
    Address=models.CharField(max_length=150,default="")
    prof_image=models.ImageField(upload_to = 'projects/profile_images',default="{% static 'images/default_profile.jpg' %}" )


    def __str__(self):
        return self.fullname
    




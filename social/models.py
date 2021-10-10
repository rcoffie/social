from django.db import models
from django.utils import timezone 
from datetime import datetime 
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
  body = models.TextField()
  created_on = models.DateField(default=datetime.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  
  
  
class Comment(models.Model):
  post = models.ForeignKey(Post,on_delete=models.CASCADE)
  body = models.TextField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  created_on = models.DateField(default=datetime.now)
  
  
  
  
class UserProfile(models.Model):
  user = models.OneToOneField(User,primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
  name = models.CharField(max_length=30, blank=True, null=True)
  bio  = models.TextField(max_length=500, blank=True, null=True)
  birth_date = models.DateField(null=True, blank=True)
  picture = models.ImageField(upload_to='uploads/profile_pictures', default='uploads/profile_pictures/images.jpg', blank=True)
  
  
  
  
  
  

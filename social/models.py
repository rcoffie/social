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
  
  
  
  

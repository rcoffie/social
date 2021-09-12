from django.shortcuts import render, redirect 
from . models import * 
from .forms import *

# Create your views here.

def Index(request):
  form = PostForm()
  posts = Post.objects.all()
  context = {'posts':posts,'form':form}
  
  return render(request,'social/index.html',context)

from django.shortcuts import render, redirect 
from . models import * 
from .forms import *
from django.contrib import messages

# Create your views here.

def Index(request):
  
  posts = Post.objects.all().order_by('-id')
  form = PostForm()
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.save()
      messages.success(request,'post sent')
      return redirect('social:index')
      
  context = {'posts':posts,'form':form}
  
  return render(request,'social/index.html',context)

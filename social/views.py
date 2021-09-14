from django.shortcuts import render, redirect ,get_object_or_404,HttpResponseRedirect
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



def postDetail(request, id):
  post = get_object_or_404(Post, id=id)
  form = CommentForm()
  context = {'post':post,'form':form}
  
  return render(request,'social/detail.html',context)


def editPost(request, id):
  
  post = get_object_or_404(Post, id=id)
  form = PostForm(request.POST or None, instance=post)
  if form.is_valid():
    form.save() 
    return HttpResponseRedirect('/'+id)
  
  context = {'form':form }
  
  return render(request,'social/edit.html',context)



def deletePost(request, id):
  post = Post.objects.get(id=id)
  post.delete()

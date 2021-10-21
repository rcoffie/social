from django.shortcuts import render, redirect ,get_object_or_404,HttpResponseRedirect
from . models import * 
from .forms import *
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse 

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
  comments = Comment.objects.all()
  form = CommentForm()
  if request.method == 'POST':
    body = request.POST['body']
    author = request.user 
    comment = Comment.objects.create(author=author,body=body,post=post)
    comment.save()
    return HttpResponseRedirect(reverse('social:post_detail', args=[post.id]))
    
    
  context = {'post':post,'form':form,'comments':comments}
  
  return render(request,'social/detail.html',context)


def editPost(request, id):
  
  post = get_object_or_404(Post, id=id)
  form = PostForm(request.POST or None, instance=post)
  if form.is_valid():
    form.save() 
    return HttpResponseRedirect(reverse('social:edit_post', args=[post.id]))
  
  context = {'form':form }
  
  return render(request,'social/edit.html',context)



def deletePost(request, id):
  post = Post.objects.get(id=id)
  post.delete()


def editComment(request, id):
  
  comment = get_object_or_404(Comment, id=id) 
  form = CommentForm(request.POST or None, instance=comment)
  if form.is_valid(): 
    print (form)
    form.save()
    return HttpResponseRedirect(reverse('social:edit_comment', args=[comment.id]))
  context = {'form':form}
  return render(request,'social/edit_comment.html',context)


def deleteComment(request, id):
  comment = Comment.objects.get(id=id)
  comment.delete() 
  
  
  
def Profile(request, pk):
  profile = UserProfile.objects.get(user_id=pk)
  user = profile.user 
  following = profile.followers
  followers = profile.followers.all()
  posts = Post.objects.filter(author=user).order_by('created_on')
  num_followers = followers.count()
  
  context = {
    'user':user,
    'profile':profile, 
    'posts':posts,
    'followers':followers,
    'num_followers':num_followers,
  }
  
  return render(request, 'social/profile.html',context)
  
  

def EditProfile(request):
  if request.method == 'POST': 
    p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
    if p_form.is_valid():
      p_form.save()
      return HttpResponseRedirect(reverse('social:profile',args=[request.user.id]))
  else:
    p_form = ProfileUpdateForm(instance=request.user.profile)
    
  context = {
    'p_form':p_form,
  }
  
  return render(request, 'social/profile_edit.html',context )


def Follow(request, id):
  profile = get_object_or_404(UserProfile, user_id=request.POST.get('profile_id'))
  
  user_id = request.user.id 
  if user_id is None:
    return redirect('/accounts/login')
  else: 
    if profile.followers.filter(id=request.user.id).exists():
      profile.followers.remove(request.user)
    else:
      profile.followers.add(request.user)
  return HttpResponseRedirect(reverse('social:profile',args=[profile.user.id]))
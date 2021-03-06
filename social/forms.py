from django.forms import ModelForm 
from django import forms
from .models import * 


class PostForm(ModelForm):
  body = forms.CharField( 
    label= '',
    widget=forms.Textarea(attrs={
      'rows':'5',
      'placeholder':'say something'
    })                      
                          )
  class Meta:
    model = Post 
    fields = ['body']
    


class CommentForm(ModelForm):
  body = forms.CharField(
    label = '',
    widget=forms.Textarea(attrs={
      'rows':'3',
      'placeholder':'comment'
    })
  )
  class Meta:
    model = Comment 
    fields = ['body']
    


class ProfileUpdateForm(forms.ModelForm): 
  class Meta: 
    model = UserProfile 
    fields = ['bio','birth_date','location','picture','name']
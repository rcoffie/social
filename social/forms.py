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
from django import forms
from .models import NewsPost
from django.forms import ModelForm

class NewsPostForm(ModelForm):

    class Meta:
        model = NewsPost
        fields = ('topic', 'author', 'body')

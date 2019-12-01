from django.shortcuts import render
from naac import naac_settings as config
from .models import NewsPost
# Create your views here.

def news_index(request):
    news = NewsPost.objects.all() # [:config.max_news]
    return render(request, 'news/index.html', {'news': news})

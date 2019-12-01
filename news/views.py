from django.shortcuts import render, redirect, reverse
from naac import naac_settings as config
from .models import NewsPost
from .forms import NewsPostForm
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def news_index(request):
    news = NewsPost.objects.all() # [:config.max_news]
    return render(request, 'news/index.html', {'news': news})

@staff_member_required
def add_news_post(request):
    form = NewsPostForm(request.POST or None, initial={'author': request.user})
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect(reverse('news_index'))

    return render(request, 'news/add_news_post.html', {'form': form })

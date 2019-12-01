from django.shortcuts import render, redirect, reverse
from naac import naac_settings as config
from .models import NewsPost
from .forms import NewsPostForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
# Create your views here.

def news_index(request):
    news = NewsPost.objects.order_by('-created')[:config.latest_news]
    return render(request, 'news/index.html', {'news': news})

@staff_member_required
def add_news_post(request):
    form = NewsPostForm(request.POST or None, initial={'author': request.user})
    if request.POST:
        if form.is_valid():
            form.save()
            messages.success(request, "News post added!")
            return redirect(reverse('news_index'))

    return render(request, 'news/add_news_post.html', {'form': form })

@staff_member_required
def delete_news(request, id):
    post = NewsPost.objects.get(id=id)
    if post:
        messages.success(request, "News post %s deleted!" % post.topic)
        post.delete()
    else:
        messages.fail('message')(request, "News post with that id doesn't exist")

    return redirect(reverse('news_index'))

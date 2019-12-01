from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.news_index, name='news_index'),
    path('add', views.add_news_post, name='add_news_post'),

]

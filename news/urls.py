from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.news_index, name='news_index'),

]

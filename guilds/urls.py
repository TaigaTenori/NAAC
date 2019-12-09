from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.guilds_index, name='guilds_index'),

]

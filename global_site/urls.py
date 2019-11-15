
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('accounts/create', views.create_account, name='create_account'),
    path('accounts/logout', views.user_logout, name='user_logout'),
]

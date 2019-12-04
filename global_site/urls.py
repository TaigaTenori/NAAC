
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('accounts/create', views.create_account, name='create_account'),
    path('accounts/logout', views.user_logout, name='user_logout'),
    path('accounts/login/', views.user_login, name='user_login'), # new
    path('accounts/overview', views.account_overview, name='account_overview'),
    path('accounts/password_reset', views.password_reset, name='password_reset'),
    path('accounts/reset/<str:hash>', views.set_new_password, name="set_new_password"),
    path('ajax/change_email/', views.change_email, name='change_email'),
    path('ajax/change_password/', views.change_password, name='change_password'),
]

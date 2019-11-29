from django.urls import path, include


from . import views

urlpatterns = [
    path('view/<str:name>', views.view_character, name='view_character'),
    path('delete/<str:name>', views.delete_character, name='delete_character'),
    path('create', views.create_character, name='create_character')
]

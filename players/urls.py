from django.urls import path, include


from . import views

urlpatterns = [
    path('view/<str:name>', views.view_character, name='view_character'),
]

from django.shortcuts import render
from .models import Guild
# Create your views here.



def guilds_index(request):
    guilds = Guild.objects.all()
    return render(request, 'guilds/index.html', {'guilds': guilds })
    

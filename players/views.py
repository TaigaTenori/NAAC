from django.shortcuts import render, get_object_or_404, reverse
from .models import Player

from datetime import datetime


def view_character(request, name):
    player = get_object_or_404(Player, name=name)

    # Creating a datetime object from unix timestamp
    #TODO: Add a template filter instead
    created = datetime.fromtimestamp(player.created)
    return render(request, 'players/view_character.html', {'player': player, 'created': created})

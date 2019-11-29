from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Player
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required
from global_site import urls

def view_character(request, name):
    player = get_object_or_404(Player, name=name)

    # Creating a datetime object from unix timestamp
    #TODO: Add a template filter instead
    created = datetime.fromtimestamp(player.created)
    return render(request, 'players/view_character.html', {'player': player, 'created': created})

@login_required
def delete_character(request, name):
    character = get_object_or_404(Player, name=name)
    if character.account_id == request.user.id:
        character.delete()
        messages.success(request, "Character " + name + " has been deleted.")
    else:
        messages.warning(request, "You can't delete characters you don't own.")
    return redirect(reverse('account_overview'))

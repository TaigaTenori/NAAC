from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Player
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required
from global_site import urls
from players.forms import CharacterCreationForm
from django import forms


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


@login_required
def create_character(request):
    form = CharacterCreationForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            messages.success(request, "Character successfuly created!")
            character = form.save(commit=False)
            character.account_id = request.user.id
            character.save()
            return redirect(reverse('account_overview'))
    return render(request, 'players/create_character.html', {'form': form})

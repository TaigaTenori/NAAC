from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users.forms import AccountCreationForm, AccountAuthenticationForm
from users.models import Account
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from players.models import Player
import datetime
from naac import naac_settings as config

from django.contrib.auth.models import update_last_login

# Create your views here.
def index(request):
    return render(request, 'global_site/index.html')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = AccountAuthenticationForm()
    if request.method == 'POST':
        form = AccountAuthenticationForm(data=request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(name=username,
                                password=password)

            if user is not None:
                messages.success(request, "You are now logged in!")
                login(request, user)
                #update_last_login(None, user)
                return redirect('index')
            else:
                messages.error(request, 'The supplied account name and password is incorrect')

    return render(request, 'global_site/login.html', {'form': form})

def user_logout(request):
    messages.info(request, 'You have been logged out.')
    logout(request)
    return redirect('index')

def create_account(request):
    if request.user.is_authenticated and request.method != 'POST':
        messages.info(request, 'You need to log out if you want to create another account.')
        return redirect('index')
    if request.method != 'POST':
        form = AccountCreationForm()
        return render(request, 'global_site/create_account.html', {'form': form })


    form = AccountCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        messages.success(request, "Success! You are now registered!")
        if config.AUTO_LOGIN:
            # automatically login the user
            user = authenticate(name=form.cleaned_data['name'], password=form.cleaned_data['password1'],)
            login(request, user)

        return redirect('index')
    else:
        return render(request, 'global_site/create_account.html', {'form': form })

@login_required
def account_overview(request):
    account = request.user
    # Also provide a list of characters on this accounts
    characters = Player.objects.filter(account_id=account.id).only('name', 'level')
    return render(request, 'global_site/account_overview.html', {'account': account, 'characters': characters })

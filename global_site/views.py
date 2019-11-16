from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users.forms import AccountCreationForm, AccountAuthenticationForm
from users.models import Account
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def index(request):
    return render(request, 'global_site/index.html')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(name=username,
                                password=password)

            if user is not None:
                messages.success(request, "You are now logged in!")
                login(request, user)
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
        #if OTS['auto_login']:
            # automatically login the users
        messages.success(request, "Success! You are now registered and logged in!")
        user = authenticate(name=form.cleaned_data['name'],
                            password=form.cleaned_data['password1'],)
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'global_site/create_account.html', {'form': form })

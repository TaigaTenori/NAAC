from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users.forms import AccountCreationForm
from users.models import Account
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'global_site/index.html')
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

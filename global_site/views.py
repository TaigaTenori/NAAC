from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from users.forms import AccountCreationForm, AccountAuthenticationForm, PasswordResetForm, PostResetPasswordForm
from users.models import Account
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from players.models import Player
import datetime
from naac import naac_settings as config
from django.core.mail import send_mail
from django.contrib.auth.models import update_last_login
import naac.emails as emails
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request, 'global_site/index.html')

@login_required
def change_email(request):
    validate_email(request.GET.get('new_email')) # will throw an exception if the user bypasses valid email check in preceeding js
    account = get_object_or_404(Account, name=request.user)
    account.email = request.GET.get('new_email')
    account.save()

    return JsonResponse({'success': True})


@login_required
def change_password(request):
    validate_password(request.GET.get('new_password'))
    account = get_object_or_404(Account, name=request.user)
    account.set_password(request.GET.get('new_password'))
    account.save()
    update_session_auth_hash(request, account)

    return JsonResponse({'success': True})

def set_new_password(request, hash):
    account = get_object_or_404(Account, password_reset=hash)

    form = PostResetPasswordForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            account.set_password(form.cleaned_data['password1'])
            account.password_reset = None
            account.save()
            messages.success(request, 'Your password has been changed!')
            return redirect(reverse('account_overview'))
    else:
        messages.success(request, 'You can now set your new password below')
    return render(request, 'global_site/new_password.html', {'form': form})



def password_reset(request):
    form = PasswordResetForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            if Account.objects.filter(name=form.cleaned_data['name'], email=form.cleaned_data['email']).exists():

                account = Account.objects.get(name=form.cleaned_data['name'], email=form.cleaned_data['email'])
                hash = emails.generateHash()
                account.password_reset = hash
                account.save()
                messages.success(request, "We've sent a password reset link to your email!")
                send_mail(emails.res_topic, emails.res_message.replace('{hash}', hash), emails.from_email, [form.cleaned_data['email']] )
            else:
                messages.error(request, "The account and e-mail address do not match.")
    return render(request, 'global_site/password_reset.html', {"form": form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = AccountAuthenticationForm()
    if request.method == 'POST':
        form = AccountAuthenticationForm(data=request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']
            user = authenticate(name=username,
                                password=password)

            if user is not None:
                messages.success(request, "You are now logged in!")
                login(request, user)
                if remember_me:
                    request.session.set_expiry(config.cookie_timeout)
                else:
                    request.session.set_expiry(0)
                return redirect('account_overview')
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
        if config.registration_email:
            send_mail(emails.reg_topic, emails.reg_message.replace('{username}', user.name), emails.from_email , [user.email])
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

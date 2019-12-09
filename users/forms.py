# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import Account

class PasswordResetForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=40)

class PostResetPasswordForm(forms.Form):
    password1 = forms.CharField(label="New Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput())

    def clean(self):
        pass1 = self.cleaned_data['password1']
        if pass1 != self.cleaned_data['password2']:
            raise forms.ValidationError('The passwords do not match.')

class AccountAuthenticationForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False)
    
    class Meta:
        model = Account
        fields = {'name', 'password', }
        labels = { 'name': 'Account name', }


class AccountCreationForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ('name','email',)
        labels = {
            'name': 'Account name',
        }
class AccountChangeForm(UserChangeForm):

    class Meta:
        model = Account
        fields = ('name','email',)

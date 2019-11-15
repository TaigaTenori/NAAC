from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import Account
from .forms import AccountCreationForm, AccountChangeForm

class AccountAdmin(UserAdmin):
    add_form = AccountCreationForm
    form = AccountChangeForm
    model = Account
    list_display = ['name','username',]

admin.site.register(Account, AccountAdmin)

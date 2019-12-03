# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser, User, UserManager




class AccountManager(UserManager):
    def create_user(self, name = None, email=None, password1=None ):
        if not email:
            raise ValueError("Email buddy")
#        if not username:
#            raise ValueError("username buddy")
        if not password1:
            raise ValueError("password buddy")
        if not name:
            raise ValueError("name buddy")
        user = self.model(
            email = self.normalize_email(email),
            name = name
        )
        user.set_password(password1)
        user.save()
        return user

    def create_superuser(self, name, email, password):
        user = self.create_user(name, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class Account(AbstractUser):
    name = models.CharField(unique=True, max_length=32)
    password_reset = models.CharField(default=None, max_length=50)

    USERNAME_FIELD = 'name'

    objects = AccountManager()


    def __str__(self):
        return self.name
    class Meta:
        managed = True
        db_table = 'accounts'

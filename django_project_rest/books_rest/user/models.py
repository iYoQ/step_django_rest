from typing import AbstractSet
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, 
    PermissionsMixin, 
    BaseUserManager,
)
from django.db.models.fields import BooleanField


# class User(AbstractBaseUser, PermissionsMixin):
#     USER = 'user'
#     ADMIN = 'admin'
#     ROLE = [
#         (USER, 'user'),
#         (ADMIN, 'admin'),
#     ]

#     email = models.EmailField(max_length=100)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     patronymic = models.CharField(max_length=100)
#     role = models.CharField(max_length=100)
#     date_create = models.DateField()
#     is_staff = BooleanField()
#     is_active = BooleanField()
#     is_superuser = BooleanField()
#     post_agreement = BooleanField()
#     inn = models.CharField(max_length=100)
#     bank_account = models.CharField(max_length=100)
#     phone = models.CharField(max_length=100)
#     address = models.CharField(max_length=200)

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from petstagram_2024.accounts.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        blank=False,
        null=False,
        unique=True
    )

    is_active = models.BooleanField(
        default=True
    )

    is_staff = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AppUserManager()

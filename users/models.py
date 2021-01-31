from django.db import models
from django.contrib.auth.models import AbstractUser
from languages.fields import LanguageField


class MyUser(AbstractUser):

    display_name = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    email = models.EmailField(
        verbose_name="Email Address",
        max_length=255,
        unique=True
    )

    language = LanguageField(
        max_length=8,
        blank=True,
        default="eng"
        )

    bio = models.TextField(
        null=True,
        blank=True,
        help_text="A little about yourself. Do you like cheese, for instance?"
    )

    avatar = models.ImageField()

    is_online = models.BooleanField(
        default=False
        )

    is_active = models.BooleanField(
        default=True
        )

    is_admin = models.BooleanField(
        default=False
        )

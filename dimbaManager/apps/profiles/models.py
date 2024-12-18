from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from dimbaManager.apps.common.models import CommonFieldsMixin

User = get_user_model()


class Profile(CommonFieldsMixin):
    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete=models.CASCADE
    )
    profile_photo = models.FileField(
        verbose_name=_("Profile Photo"),
        default="/profile.png"
    )

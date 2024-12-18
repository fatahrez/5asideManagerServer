import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from dimbaManager.config.settings.base import AUTH_USER_MODEL
import dimbaManager.apps.users.models as user_models
from .models import Profile

logger = logging.getLogger(__name__)

@receiver(post_save, sender=user_models.Admin)
@receiver(post_save, sender=user_models.StaffManager)
@receiver(post_save, sender=user_models.FieldManager)
@receiver(post_save, sender=user_models.Captain)
@receiver(post_save, sender=user_models.NormalUser)
@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=user_models.Admin)
@receiver(post_save, sender=user_models.StaffManager)
@receiver(post_save, sender=user_models.FieldManager)
@receiver(post_save, sender=user_models.Captain)
@receiver(post_save, sender=user_models.NormalUser)
@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    logger.info(f"{instance}'s profile created")
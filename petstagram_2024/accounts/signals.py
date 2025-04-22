# accounts/signals.py
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from petstagram_2024.accounts.models import Profile

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_for_new_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from petstagram_2024.accounts.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def add_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

        send_mail(
            subject='New account has been created!',
            message='Welcome to our lovely community, hope you enjoy it!',
            from_email='alexmilenkov07@gmail.com',
            recipient_list=[instance.email],
            fail_silently=False
        )


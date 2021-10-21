from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from user.models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print('in create profile ')
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save,  sender=User)
def save_profile(sender, instance, created, **kwargs):
    print('in save profile ')

    if created:
        instance.profile.save()
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Quiz


@receiver(post_save, sender=Quiz())
def create_profile(sender, instance, created, **kwargs):
    if created:
        print("Quiz questions ", instance.get_questions())
        
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete =models.CASCADE,primary_key=True)
    photo = models.ImageField(blank=True)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.user.pk})

def on_post_save_for_user(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        Profile.objects.create(user=user)

post_save.connect(on_post_save_for_user,sender=settings.AUTH_USER_MODEL)
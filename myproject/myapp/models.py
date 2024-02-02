

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    phone_number=models.IntegerField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_url(self):
        return reverse('profile', args=[ self.user])

    def __str__(self):
        return '{}' .format(self.user)
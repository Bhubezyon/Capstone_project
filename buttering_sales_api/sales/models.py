from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.textField(blank=True)
    profile_picture = models.ImageField(upload_to='profile/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetricall=False, related_name='following', blank=True)

    def __str__(self):
        return self.username
        
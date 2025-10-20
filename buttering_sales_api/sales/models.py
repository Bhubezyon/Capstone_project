from django.contrib.auth.models import User
from django.db import models

class Profile(models.Models):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile/', blank=True, null=True)

    def __str__(self):
        return self.user.username


        
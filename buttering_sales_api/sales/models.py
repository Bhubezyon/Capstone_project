from django.contrib.auth.models import User
from django.db import models

class UserRegistration(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Follow(models.Model):
    follower = models.ForeignKey('auth.User', related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey('auth.User', related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.follower} follows {self.following}"

class Like(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, null=True, blank=True, related_name='likes')
    comment = models.ForeignKey('posts.Comment', on_delete=models.CASCADE, null=True, blank=True, related_name='comment_likes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.post:
            return f"{self.user} liked post {self.post.id} at {self.created_at}"
        elif self.comment:
            return f"{self.user} liked comment {self.comment.id} at {self.created_at}"
        return f"{self.user} liked at {self.created_at}"


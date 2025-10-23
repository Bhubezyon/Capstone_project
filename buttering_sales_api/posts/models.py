from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from .models import Post
from sales.models import CustomUser
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_save
from django.dispatch import reciever

class Post(models.Models):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    summery = models.CharField(max_length=300) # brief item summary
    content = models.TextField()
    is_for_sale = models.BooleanField(default=True) # sales request
    exchange_item = models.CharField(max_length=255, blank=true, null=True) # barter request
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(CustomUser, related_name='liked_posts', blank=True)
    image = models.ImageField(
        upload_to='post_image/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]
    )

    def __str__(self):
        return self.title

class Comment(models.Models):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    content = models.TextFiel()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyfield(CustomUser, related_name='liked_comments', blank=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('furniture', 'Furniture'),
        ('clothing', 'Clothing'),
        ('books', 'Books'),
        ('tools', 'Tools'),
        ('jewellery', 'Jewellery'),
        ('other', 'Other')
    ]
catergory = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')

class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notificationd')
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Notificatio for {self.recipient.username}'

class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='recieved_messages')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Message from {self.sender.username} to {self.recipient.username}'

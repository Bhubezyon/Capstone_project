from django.db import models
from sales.models import CustomUser
from django.core.validators import FileExtensionValidator

class Post(models.Models):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    summery = models.CharField(max_length=300) # brief item summary
    content = models.TextField()
    is_for_sale = models.BooleanField(default=True) # sales request
    exchange_item = models.CharField(max_length=255, blank=true, null=True) # barter request
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
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
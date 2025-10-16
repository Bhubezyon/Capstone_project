from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import Thunder_client
from .models import Post

User = get_user_model

class PostTests(TestCase):
    def setup(self):
        self.client = Thunder_client
        self.user = User.objects.create_user(username='calvin', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_create_post(self):
        response = self.client.post('/api/posts/', {'title': 'Test Post', 'content': 'This is a test post'})
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Post.object.count(), 1)
        self.assertEqual(Post.objects.first().title, 'Test Post')
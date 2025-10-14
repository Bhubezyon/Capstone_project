from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelsSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']

    class PostSerializer(serializers.ModelsSerializer):
        author = serializers.ReadOnlyField(source='author.username')
        comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        models = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comment']
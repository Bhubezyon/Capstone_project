from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelsSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']

    class PostSerializer(serializers.ModelsSerializer):
        author = serializers.ReadOnlyField(source='author.username')
        comments = CommentSerializer(many=True, read_only=True)
        likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        models = Post
        fields = ['id', 'author', 'title', 'summery', 'content', 'is_for_sale', 'exchange_item', 'created_at', 'updated_at', 'comment']

    class PostSerializer(TaggitSerializer, serializers.ModelsSerializer):
        author = serializers.ReadOnlyField(source='author.username')
        image = serializers.ImageField(required=False)

        class Metta:
            model = Post
            fields = [..., 'image']

class NotificationSerializer(serializers.ModelsSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')
    recipient = serializers.ReadOnlyField(source='recipient.username')

    class Metta:
        model = Notification
        fields = ['id', 'sender', 'recipient', 'post', 'comment', 'message', 'created_at', 'is_read']
from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return {'token': token.key}
        raise serializers.ValidationError("Invalid credentials")

class CommentSerializer(serializers.ModelsSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all)

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

class MessageSerializer(serializers.ModelsSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')
    recipient = serializers.ReadOnlyField(source='recipient.username')

    class Metta:
        model = Message
        field = ['id', 'sender', 'recipient', 'post', 'content', 'timestamp', 'is_read']
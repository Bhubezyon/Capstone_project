from rest_framework import serializers
from .models import CustomUser, ProfileSerializer, UserSerializer, LikeSerializer, UnlikeSerializer, FollowSerilizer, UnfollowSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_picture', 'followers']

        def update(self, instance, validated_data):
            instance.bio = validated_data.get('bio', instance.bio)
            instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
            instance.save()
            return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']

        def create(self, validated_data):
            user = CustomUser.objects.create_user(
                username=validated_data['username'],
                email=validated_data.get('email'),
                password=validated_data['password']
            )
            return user

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            # Add other fields as needed
        )
        return user

class UnlikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username']

    def update(self, instance, validated_data):
        # Custom logic to "unlike" (remove like relationship)
        # Example: instance.likes.remove(validated_data['target'])
        instance.save()
        return instance

class FollowSerilizer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            # Add other fields as needed
        )
        return user   

class UnfollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username']

    def update(self, instance, validated_data):
        # Custom logic to "unfollow" (remove follower relationship)
        # Example: instance.followers.remove(validated_data['target'])
        instance.save()
        return instance

from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class RegisterSerializer(serializer.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password','email', 'bio', 'profile_picture']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.serializer):
    username = serializers.CharField()
    password = serializers.Charfield(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return {'token': token.key}
        raise serializers.validationError("Invalid credentials")

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_picture', 'followers']
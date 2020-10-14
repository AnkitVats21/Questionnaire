from rest_framework import serializers
from .models import User, UserProfile
from django.contrib.auth import authenticate


class UserProfileSerializer(serializers.ModelSerializer):    
    class Meta:
        model   = UserProfile
        fields  = ('name','course','branch','section','picture')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model       = User
        fields      = ('id', 'email', 'password', 'profile','teacher')
        extra_kwargs= {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

from rest_framework import serializers
from .models import User, UserProfile, OTP
from django.contrib.auth import authenticate
#from rest_framework_jwt.settings import api_settings
class OTPSerializer(serializers.ModelSerializer):

    class Meta:
        model   = OTP
        fields  = ('otp_email','otp','time')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model       = User
        fields      = ('id', 'email',
         'password', 'teacher', 'name',
          'course', 'branch','section',
           'picture',
           )
        extra_kwargs= {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

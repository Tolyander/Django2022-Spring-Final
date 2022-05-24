from rest_framework import serializers
# from .models import UserProfile
from django.contrib.auth.models import User

class UserRegistrationSerializer(serializers.Serializer):

    first_name =serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(write_only=True)
    username = serializers.CharField()
    email = serializers.CharField(required=False)


    def validate(self,data):
        data['username'] = data['username'].lower()
        if ' ' in data['username']:
            raise serializers.ValidationError("Username is wrong")
        return data
    

    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
from django.contrib.auth import get_user_model, authenticate
from django_countries.serializer_fields import CountryField, countries
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from .models import Profile
from ..users.serializers import UserShortSerializer


User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    user = UserShortSerializer()

    class Meta:
        model = Profile
        fields = ["id", "user", "profile_photo"]
    

class ProfileEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class UpdateProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    current_password = serializers.CharField(write_only=True, required=False)
    profile_photo = serializers.FileField(required=False)
    
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'profile_photo',
            'password',
            'current_password'
        ]
    
    def update(self, instance, validated_data):
        print(validated_data)
        if 'password' in validated_data:
            current_password = validated_data['current_password']
            print(current_password)
            user = authenticate(username=instance.username, password=current_password)
            if user is not None:
                instance.set_password(validated_data['password'])
            
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.profile.profile_photo = validated_data.get('profile_photo', instance.profile.profile_photo)

        instance.save()

        return instance
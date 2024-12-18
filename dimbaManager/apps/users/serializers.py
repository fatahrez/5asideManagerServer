import enum

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import (NormalUser, Captain, FieldManager, StaffManager, Admin, User)


class CreateUserSerializer(serializers.ModelSerializer):
    class Roles(enum.Enum):
        NORMALUSER = "NORMALUSER", "NormalUser"
        FIELDMANAGER = "FIELDMANAGER", "FieldManager"
        CAPTAIN = "CAPTAIN", "Captain"
        STAFFMANAGER = "STAFFMANAGER", "StaffManager"
        ADMIN = "ADMIN", "Admin"

    password = serializers.CharField(min_length=6, max_length=100, write_only=True)
    roles = [role.value for role in Roles]
    type = serializers.ChoiceField(choices=roles, required=True)
    first_name = serializers.CharField(max_length=100, required=True)
    email = serializers.CharField(
        max_length=100,
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "email",
            "password",
            "type",
            "tokens",
            "id"
        ]

        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        type = self.validated_data["type"]
        if type == "ADMIN":
            user = Admin.objects.create(
                username = validated_data["email"],
                email = validated_data["email"],
                first_name = validated_data["first_name"],
                password = validated_data["password"],
                type = type
            )
        elif type == "CAPTAIN":
            user = Captain.objects.create(
                username = validated_data["email"],
                email = validated_data["email"],
                first_name = validated_data["first_name"],
                password = validated_data["password"],
                type=type
            )
        elif type == "FIELDMANAGER":
            user = FieldManager.objects.create(
                username = validated_data["email"],
                email = validated_data["email"],
                first_name = validated_data["first_name"],
                password = validated_data["password"],
                type=type
            )
        elif type == "STAFFMANAGER":
            user = StaffManager.objects.create(
                username = validated_data["email"],
                email = validated_data["email"],
                first_name = validated_data["first_name"],
                password = validated_data["password"],
                type=type
            )
        else:
            user = NormalUser.objects.create(
                username = validated_data["email"],
                email = validated_data["email"],
                first_name = validated_data["first_name"],
                password = validated_data["password"],
                type=type
            )
        return user
    

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ("email", "first_name", "username", "password", "tokens")

        read_only_fields = ("tokens",)


    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)
        
        instance.save()

        return instance
    

class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email")
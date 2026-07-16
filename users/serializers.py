from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "username",
            "first_name",
            "last_name",
        ]

    def create(self, validated_data):
        username = validated_data.pop("username", None)
        if username in (None, ""):
            username = None

        password = validated_data.pop("password")
        email = validated_data.pop("email")

        return User.objects.create_user(
            username=username,
            email=email,
            password=password,
            **validated_data,
        )

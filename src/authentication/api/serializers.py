from django.contrib.auth import password_validation, authenticate
from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
        )


class UserLoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, attrs):

        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(username=email, password=password)

        if not user:
            raise serializers.ValidationError("Invalid credentials")

        self.context["user"] = user
        return attrs

    def create(self, validated_data):
        token, created = Token.objects.get_or_create(user=self.context["user"])
        return self.context["user"], token.key

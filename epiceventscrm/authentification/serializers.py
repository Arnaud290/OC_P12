"""Logins serialization and account creation module"""
from rest_framework import serializers
from django.utils import timezone
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from contact.models import Contact


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Returns a pair of tokens based on the username"""
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        user.last_login = timezone.now()
        user.save()
        return token


class ChangePasswordSerializer(serializers.ModelSerializer):
    """Password change serialization class"""
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True
    )
    old_password = serializers.CharField(
        write_only=True,
        required=True
    )

    class Meta:
        model = Contact
        fields = ['old_password', 'password', 'password2']

    def validate(self, attrs):
        """Passwords match verification"""
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": "Old password is not correct"}
            )
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

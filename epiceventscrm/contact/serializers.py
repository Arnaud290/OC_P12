"""Contact serialization module"""
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from contract.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Contact.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True
    )

    class Meta:
        model = Contact
        fields = [
            'username',
            'password',
            'password2',
            'email',
            'first_name',
            'last_name',
            'post',
            'mobile',
            'is_superuser',
            'is_staff'
        ]
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'is_superuser': {'required': True},
            'is_staff': {'required': True},
        }

    def validate(self, attrs):
        """Passwords match verification"""
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        user = Contact.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            post=validated_data['post'],
            mobile=validated_data['mobile'],
            is_superuser=validated_data['is_superuser'],
            is_staff=validated_data['is_staff']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ContactretrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        exclude = ['password', 'groups', 'user_permissions']


class ContactListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name', 'mobile', 'email', 'post']

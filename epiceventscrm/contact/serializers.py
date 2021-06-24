"""Contact serialization module"""
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from contract.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_serializer = dict()

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
            'id',
            'username',
            'password',
            'password2',
            'email',
            'first_name',
            'last_name',
            'post',
            'mobile',
            'is_active'
        ]
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'is_active': {'required': True},
        }

    def validate(self, attrs):
        """Passwords match verification"""
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        self.data_serializer = {
            'username': attrs['username'],
            'email': attrs['email'],
            'first_name': attrs['first_name'],
            'last_name': attrs['last_name'],
            'post': attrs['post'],
            'mobile': attrs['mobile'],
            'is_superuser': attrs['post'] == 'ADMIN',
            'is_staff': attrs['post'] == 'ADMIN',
            'is_active': attrs['is_active'],
        }
        return attrs

    def create(self, validated_data):
        user = Contact.objects.create(**self.data_serializer)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        Contact.objects.filter(id=instance.id).update(**self.data_serializer)
        user = Contact.objects.get(id=instance.id)
        user.set_password(validated_data['password'])
        return user


class ContactretrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        exclude = ['password', 'groups', 'user_permissions']


class ContactListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name', 'mobile', 'email', 'post']

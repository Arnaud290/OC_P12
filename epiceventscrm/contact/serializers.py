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
        if type(attrs['is_active']) != bool:
            raise serializers.ValidationError(
                {"is_staff must be 'True' or 'False'"}
            )
        return attrs

    def create(self, validated_data):
        if validated_data['post'] == 'ADMIN':
            superuser = True
        else:
            superuser = False
        user = Contact.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            post=validated_data['post'],
            mobile=validated_data['mobile'],
            is_superuser=superuser,
            is_staff=superuser,
            is_active=validated_data['is_active'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        if validated_data['post'] == 'ADMIN':
            superuser = True
        else:
            superuser = False
        instance.username = validated_data['username']
        instance.email = validated_data['email']
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.post = validated_data['post']
        instance.mobile = validated_data['mobile']
        instance.is_superuser = superuser
        instance.is_staff = superuser
        instance.set_password(validated_data['password'])
        instance.is_staff = validated_data['is_active']
        instance.save()
        return instance


class ContactretrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        exclude = ['password', 'groups', 'user_permissions']


class ContactListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name', 'mobile', 'email', 'post']

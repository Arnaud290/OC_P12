"""Contact serialization module"""
from rest_framework import serializers
from contract.models import Contact


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        exclude = '__all__'


class ContactretrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        exclude = ['password', 'groups', 'user_permissions']


class ContactListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name', 'mobile', 'email', 'post']

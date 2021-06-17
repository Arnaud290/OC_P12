from rest_framework import serializers
from client.models import Client


class ClientSerializer(serializers.ModelSerializer):

    sales_contact_id = serializers.ReadOnlyField(source='sales_contact_id.id')

    class Meta:

        model = Client
        fields = '__all__'


class ClientListSerializer(serializers.ModelSerializer):

    class Meta:

        model = Client
        fields = ['id', 'first_name', 'last_name', 'company_name']

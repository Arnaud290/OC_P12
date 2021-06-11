from rest_framework import serializers
from client.models import Client


class ClientSerializer(serializers.ModelSerializer):

    sales_contact_id = serializers.ReadOnlyField(source='sales_contact_id.id')

    class Meta:

        model = Client
        fields = '__all__'

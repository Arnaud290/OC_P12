"""Contract serialisation module"""
from rest_framework import serializers
from contract.models import Contract, Status
from client.models import Client


class ContractSerializer(serializers.ModelSerializer):
    sales_contact_id = serializers.ReadOnlyField(source='sales_contact_id.id')

    class Meta:
        model = Contract
        fields = '__all__'

    def validate(self, data):
        user = self.context.get("request").user
        if user.post == 'COMMERCIAL':
            client = [
                client for client in Client.objects.filter(sales_contact_id=user)
            ]
        else:
            client = Client.objects.all()
        if data['client_id'] not in client:
            raise serializers.ValidationError("Client not exist")
        return data


class ContractListSerializer(serializers.ModelSerializer):
    date_created = serializers.DateTimeField(format='%d %m %Y', read_only=True)
    company_name = serializers.ReadOnlyField(source='client_id.company_name')

    class Meta:
        model = Contract
        fields = ['id', 'company_name', 'date_created']


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = '__all__'

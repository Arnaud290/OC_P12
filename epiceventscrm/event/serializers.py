"""Event serialization module"""
from rest_framework import serializers
from contract.models import Contract
from event.models import Event, Status


class EventSerializer(serializers.ModelSerializer):
    client_id = serializers.ReadOnlyField(source='client_id.id')

    class Meta:
        model = Event
        fields = '__all__'
        extra_kwargs = {'support_contact_id': {'required': True}}

    def validate(self, data):
        user = self.context.get("request").user
        if user.post == 'COMMERCIAL':
            contract = [
                contract for contract in
                Contract.objects.filter(sales_contact_id=user)
            ]
        else:
            contract = Contract.objects.all()
        if data['contract_id'] not in contract:
            raise serializers.ValidationError("Contract not exist")
        if data['support_contact_id'].post != 'SUPPORT':
            raise serializers.ValidationError("Contact is not support")
        return data


class EventSupportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        exclude = ['contract_id', 'support_contact_id', 'client_id']


class EventListSerializer(serializers.ModelSerializer):

    date_created = serializers.DateTimeField(format='%d %m %Y', read_only=True)
    company_name = serializers.ReadOnlyField(source='client_id.company_name')
    sales_contact = serializers.ReadOnlyField(
        source='contract_id.sales_contact_id.username'
    )
    support_contact = serializers.ReadOnlyField(
        source='support_contact_id.username'
    )

    class Meta:
        model = Event
        fields = [
            'id',
            'company_name',
            'date_created',
            'sales_contact',
            'support_contact'
        ]


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = '__all__'

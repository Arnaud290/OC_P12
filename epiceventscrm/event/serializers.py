from rest_framework import serializers
from rest_framework.views import exception_handler
from contract.models import Contract
from event.models import Event, Status


class EventSerializer(serializers.ModelSerializer):

    client_id = serializers.ReadOnlyField(source='client_id.id')

    class Meta:

        model = Event
        fields = '__all__'

    def validate(self, data):
        user = self.context.get("request").user
        contract = [
            contract for contract in\
            Contract.objects.filter(sales_contact_id=user)
        ]
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

    class Meta:

        model = Event
        fields = ['id', 'company_name', 'date_created']


class StatusSerializer:

    class Meta:
    
        model = Status
        exclude = '__all__'

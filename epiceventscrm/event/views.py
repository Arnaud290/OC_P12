from rest_framework import viewsets, permissions
from event.models import Event
from contract.models import Contract
from event.serializers import (
    EventListSerializer,
    EventSerializer,
    EventSupportSerializer
)
from event.permissions import IsCommercialOrSupport


class EventViewSet(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsCommercialOrSupport
    ]

    def get_queryset(self):
        user = self.request.user
        if user.post == 'SUPPORT':
            return Event.objects.filter(support_contact_id=user) 
        contract = [
            contract for contract in\
            Contract.objects.filter(sales_contact_id=user)
        ]
        return Event.objects.filter(contract_id__in=contract) 

    def get_serializer_class(self):
        if self.action == 'list':
            return EventListSerializer
        if self.request.user.post == 'SUPPORT':
            if self.action != 'retrieve':
                return EventSupportSerializer
        return EventSerializer

    def perform_create(self, serializer):
        contract = Contract.objects.get(pk=self.request.data['contract_id'])
        serializer.save(client_id=contract.client_id)

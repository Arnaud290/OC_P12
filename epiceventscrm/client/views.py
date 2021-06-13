from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from client.models import Client
from event.models import Event
from client.serializers import ClientSerializer, ClientListSerializer
from client.permissions import IsCommercialOrReadOnly


class ClientViewSet(viewsets.ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsCommercialOrReadOnly
    ]
    filter_backends = [filters.SearchFilter]
    search_fields = ['last_name', 'email']

    def get_queryset(self):
        user = self.request.user
        if user.post == 'SUPPORT':
            clients_id = [
                event.client_id.id for event in\
                Event.objects.filter(support_contact_id=user)
            ] 
        if user.post == 'COMMERCIAL':
            clients_id = [
                client.id for client in\
                Client.objects.filter(sales_contact_id=user)
            ]    
        return Client.objects.filter(id__in=clients_id) 
     

    def get_serializer_class(self):
        if self.action == 'list':
            return  ClientListSerializer
        return ClientSerializer

    def perform_create(self, serializer):
        serializer.save(sales_contact_id=self.request.user)

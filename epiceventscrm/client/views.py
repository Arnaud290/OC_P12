from django.shortcuts import render
from rest_framework import viewsets, permissions
from client.models import Client
from client.serializers import ClientSerializer
from client.permissions import IsOwner
  

class ClientViewSet(viewsets.ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        user = self.request.user
        return Client.objects.filter(sales_contact_id=user)

    def perform_create(self, serializer):
        serializer.save(sales_contact_id=self.request.user)


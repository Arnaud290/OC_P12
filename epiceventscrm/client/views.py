"""Views module"""
from rest_framework import viewsets, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.db import models
from client.models import Client
from client.serializers import ClientSerializer, ClientListSerializer
from client.permissions import IsCommercialOrReadOnly, IscommercialOrAdmin
from client.filters import ClientFilter


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsCommercialOrReadOnly,
        IscommercialOrAdmin
    ]
    filter_class = ClientFilter
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_serializer_class(self):
        if self.action == 'list':
            return ClientListSerializer
        return ClientSerializer

    def perform_create(self, serializer):
        serializer.save(sales_contact_id=self.request.user)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response(status=204)
        except models.deletion.ProtectedError:
            raise ValidationError(
                "Un ou plusieurs contrats et événements sont liés à ce client"
            )

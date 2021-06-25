"""Contract views module"""
from rest_framework import viewsets, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.db import models
from contract.models import Contract, Status
from contract.serializers import (
    ContractListSerializer,
    ContractSerializer,
    StatusSerializer
)
from contract.permissions import IsAdminOrCommercial, IsAdminOrCommercialReadOnly
from contract.filters import ContractFilter


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrCommercial]
    filter_class = ContractFilter
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_serializer_class(self):
        if self.action == 'list':
            return ContractListSerializer
        return ContractSerializer

    def perform_create(self, serializer):
        serializer.save(sales_contact_id=self.request.user)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response(status=204)
        except models.deletion.ProtectedError:
            raise ValidationError(
                "Un ou plusieurs événements sont liés à ce contrat"
            )


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAdminOrCommercialReadOnly
    ]
    http_method_names = ['get', 'post', 'put', 'delete']

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response(status=204)
        except models.deletion.ProtectedError:
            raise ValidationError(
                "Un ou plusieurs contrats sont liés à ce statut"
            )

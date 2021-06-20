"""Contract views module"""
from rest_framework import viewsets, permissions
from rest_framework.exceptions import ValidationError
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

    def get_queryset(self):
        """For sales, this returns the contracts assigned to them"""
        user = self.request.user
        if user.post == 'COMMERCIAL':
            return Contract.objects.filter(sales_contact_id=user)
        return Contract.objects.all()

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

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
        except models.deletion.ProtectedError:
            raise ValidationError(
                "Un ou plusieurs contrats sont liés à ce statut"
            )

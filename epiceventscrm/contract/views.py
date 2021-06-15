from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters
from contract.models import Contract, Status
from contract.serializers import (
    ContractListSerializer,
    ContractSerializer,
    StatusSerializer
)
from contract.permissions import IsAdminOrCommercial, IsAdminOrCommercialReadOnly


class ContractViewSet(viewsets.ModelViewSet):

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrCommercial]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = [
        'client_id__last_name',
        'client_id__email',
        'date_created',
        'amount'
    ]
    search_fields = [
        'client_id__last_name',
        'client_id__email',
        '$date_created',
        '=amount'
    ]
    ordering_fields = [
        'amount'
    ]

    def get_queryset(self):
        user = self.request.user
        if user.post == 'COMMERCIAL':
            return Contract.objects.filter(sales_contact_id=user)
        return Contract.objects.filter()

    def get_serializer_class(self):
        if self.action == 'list':
            return  ContractListSerializer
        return ContractSerializer

    def perform_create(self, serializer):
        serializer.save(sales_contact_id=self.request.user)


class StatusViewSet(viewsets.ModelViewSet):
    
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAdminOrCommercialReadOnly
    ]

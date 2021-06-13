from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters
from contract.models import Contract
from contract.serializers import ContractListSerializer,ContractSerializer
from contract.permissions import IsCommercial


class ContractViewSet(viewsets.ModelViewSet):

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticated, IsCommercial]
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
        return Contract.objects.filter(sales_contact_id=user) 

    def get_serializer_class(self):
        if self.action == 'list':
            return  ContractListSerializer
        return ContractSerializer

    def perform_create(self, serializer):
        serializer.save(sales_contact_id=self.request.user)

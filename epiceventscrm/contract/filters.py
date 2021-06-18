"""Filtering module for contract searches"""
from django_filters import FilterSet, CharFilter, DateTimeFilter, NumberFilter
from contract.models import Contract


class ContractFilter(FilterSet):
    """
    Possibility of searching by the client's first and last name,
    the date of creation, the minimum and maximum amount
    """
    last_name = CharFilter(
        field_name='client_id__last_name', lookup_expr='icontains'
    )
    first_name = CharFilter(
        field_name='client_id__first_name', lookup_expr='icontains'
    )
    date_from = DateTimeFilter(
        field_name="date_created", lookup_expr='gte'
    )
    date_to = DateTimeFilter(
        field_name="date_created", lookup_expr='lte'
    )
    amount_min = NumberFilter(field_name='amount', lookup_expr='gt')
    amount_max = NumberFilter(field_name='amount', lookup_expr='lt')

    class Meta:
        model = Contract
        fields = [
            'last_name',
            'first_name',
            'date_from',
            'date_to',
            'amount_min',
            'amount_max'
        ]

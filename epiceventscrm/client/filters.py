"""Search filter module"""
from django_filters import FilterSet, CharFilter
from client.models import Client


class ClientFilter(FilterSet):
    """Searches can be made by first name, last name or email"""
    last_name = CharFilter(
        field_name='last_name', lookup_expr='icontains'
    )
    first_name = CharFilter(
        field_name='first_name', lookup_expr='icontains'
    )
    email = CharFilter(field_name='email', lookup_expr='icontains')

    class Meta:
        model = Client
        fields = [
            'last_name',
            'first_name',
            'email'
        ]

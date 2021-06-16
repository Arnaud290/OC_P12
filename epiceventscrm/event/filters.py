from django_filters import FilterSet, CharFilter, DateTimeFilter
from event.models import Event


class EventFilter(FilterSet):
    
    last_name = CharFilter(
        field_name='client_id__last_name', lookup_expr='icontains'
    )
    first_name = CharFilter(
        field_name='client_id__first_name', lookup_expr='icontains'
    )
    email = CharFilter(
        field_name='client_id__email', lookup_expr='icontains'
    )
    date_from= DateTimeFilter(
        field_name="event_date", lookup_expr='gte'
    )
    date_to = DateTimeFilter(
        field_name="event_date", lookup_expr='lte'
    )

    class Meta:
        model = Event
        fields = [
            'last_name',
            'first_name',
            'email',
            'date_from',
            'date_to',
        ]

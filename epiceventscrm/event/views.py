"""Event views module"""
from rest_framework import viewsets, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.db import models
from event.models import Event, Status
from contract.models import Contract
from event.serializers import (
    EventListSerializer,
    EventSerializer,
    EventSupportSerializer,
    StatusSerializer
)
from event.permissions import IsAdminOrCommercialOrSupport, IsAdminOrReadOnly
from event.filters import EventFilter


class EventViewSet(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAdminOrCommercialOrSupport
    ]
    filter_class = EventFilter
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_serializer_class(self):
        if self.action == 'list':
            return EventListSerializer
        if self.request.user.post == 'SUPPORT' and self.action != 'retrieve':
            return EventSupportSerializer
        return EventSerializer

    def perform_create(self, serializer):
        contract = Contract.objects.get(pk=self.request.data['contract_id'])
        serializer.save(client_id=contract.client_id)


class StatusViewSet(viewsets.ModelViewSet):

    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAdminOrReadOnly
    ]
    http_method_names = ['get', 'post', 'put', 'delete']

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response(status=204)
        except models.deletion.ProtectedError:
            raise ValidationError(
                "Un ou plusieurs événements sont liés à ce statut"
            )

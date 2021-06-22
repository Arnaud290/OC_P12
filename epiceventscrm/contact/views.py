"""Contact views module"""
from rest_framework import viewsets, permissions
from contact.models import Contact
from contact.serializers import (
    ContactListSerializer,
    ContactSerializer,
    ContactretrieveSerializer
)
from contract.permissions import IsAdminOrCommercialReadOnly


class ContactViewSet(viewsets.ModelViewSet):

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAdminOrCommercialReadOnly
    ]
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        """For sales, this returns the list of support"""
        user = self.request.user
        if user.post == 'COMMERCIAL':
            return Contact.objects.filter(post='SUPPORT')
        return Contact.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ContactListSerializer
        if self.action == 'retrieve':
            return ContactretrieveSerializer
        return ContactSerializer

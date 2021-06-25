from rest_framework import permissions
from event.models import Event


class IsCommercialOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user
        if request.method in permissions.SAFE_METHODS:
            if view.action != 'list':
                if user.post == 'SUPPORT':
                    support_clients = [
                        client.client_id for client in Event.objects.filter(
                            support_contact_id=user
                        )
                    ]
                    return obj in support_clients
                return obj.sales_contact_id == user or user.post == 'ADMIN'
            return True
        if obj.sales_contact_id == user or user.post == 'ADMIN':
            return True

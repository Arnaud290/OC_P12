"""Contract permissions module"""
from rest_framework import permissions
from event.models import Event


class IsAdminOrCommercial(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user
        if request.method in permissions.SAFE_METHODS:
                if user.post == 'SUPPORT':
                    contract_support = [
                        contract.contract_id for contract in 
                        Event.objects.filter(support_contact_id=user)
                    ]
                    return obj in contract_support
                return obj.sales_contact_id == user or user.post == 'ADMIN'
        if obj.sales_contact_id == user or user.post == 'ADMIN':
            return True


class IsAdminOrCommercialCreate(permissions.BasePermission):
    
    def has_permission(self, request, view):
        user = request.user
        if view.action == 'create':
            return user.post == 'COMMERCIAL' or user.post == 'ADMIN'
        return True


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        return request.user.post == 'ADMIN'

"""Event permissions module"""
from rest_framework import permissions


class IsAdminOrCommercialOrSupport(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action in ['create', 'destroy']:
            return request.user.post in ['ADMIN', 'COMMERCIAL']
        return True

    def has_object_permission(self, request, view, obj):
        user = request.user
        if request.method in permissions.SAFE_METHODS:
            if view.action != 'list':
                if user.post == 'COMMERCIAL':
                    return obj.contract_id.sales_contact_id == user
                if user.post == 'SUPPORT':
                    return obj.support_contact_id == user
            return True
        if user.post == 'ADMIN':
            return True
        if user.post == 'COMMERCIAL':
            return obj.contract_id.sales_contact_id == user
        if user.post == 'SUPPORT':
            if view.action == 'destroy':
                return False
            return obj.support_contact_id == user


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        return request.user.post == 'ADMIN'

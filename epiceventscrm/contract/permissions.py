"""Contract permissions module"""
from rest_framework import permissions


class IsAdminOrCommercial(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user
        if request.method in permissions.SAFE_METHODS:
            if view.action != 'list':
                return obj.sales_contact_id == user or user.post == 'ADMIN'
            return True
        if obj.sales_contact_id == user or user.post == 'ADMIN':
            return True


class IsAdminOrCommercialReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        return request.user.post == 'ADMIN'

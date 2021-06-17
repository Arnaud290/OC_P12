from rest_framework import permissions


class IsAdminOrCommercialOrSupport(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action in ['create', 'destroy']:
            return request.user.post in ['ADMIN', 'COMMERCIAL']
        return True


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        return request.user.post == 'ADMIN'

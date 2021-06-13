from rest_framework import permissions


class IsCommercialOrSupport(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action in ['create', 'destroy']:
            return request.user.post == 'COMMERCIAL'
        return True

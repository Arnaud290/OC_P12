from rest_framework import permissions


class IsCommercialOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return True
        return request.user.post == 'COMMERCIAL'

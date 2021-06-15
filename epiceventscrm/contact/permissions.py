from rest_framework import permissions


class IsAdminOrCommercialReadOnly(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.post in ['COMMERCIAL', 'ADMIN']
        return request.user.post == 'ADMIN'

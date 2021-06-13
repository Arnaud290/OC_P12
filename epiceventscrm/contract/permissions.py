from rest_framework import permissions


class IsCommercial(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.post == 'COMMERCIAL'

from rest_framework import permissions


class IsOwner(permissions.BasePermission):
  
    def has_object_permission(self, request, view, obj):

        if  request.user.post == 'COMMERCIAL':
            return obj.sales_contact_id == request.user


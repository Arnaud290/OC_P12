"""Middleware module"""
from django.utils.datastructures import MultiValueDictKeyError
from .models import ContactLog


class ContactRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
        At each request, the name of the user,
        the method and the path are sent to the database
        """
        response = self.get_response(request)
        if str(request.user) == 'AnonymousUser':
            if request.POST:
                try:
                    username = request.POST['username']
                except MultiValueDictKeyError:
                    username = 'AnonymousUser'
            else:
                username = 'AnonymousUser'
        else:
            username = request.user.username
        contact_log = ContactLog.objects.create(
            username=username,
            method=request.META['REQUEST_METHOD'],
            request_url=request.META['PATH_INFO']
        )
        contact_log.save()
        return response

"""Middleware module"""
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
            username = request.POST['username']
        else:
            username = request.user.username
        contact_log = ContactLog.objects.create(
            username=username,
            method=request.META['REQUEST_METHOD'],
            request_url=request.META['PATH_INFO']
        )
        contact_log.save()
        return response

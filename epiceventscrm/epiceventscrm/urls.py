"""General url module"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/log_viewer/', include('log_viewer.urls')),
    path('admin/', admin.site.urls),
    # /login, /refresh, /change_password, /logout
    path('', include('authentification.urls')),
    path('contact/', include('contact.urls')),
    path('client/', include('client.urls')),
    # /contract, /status_contract
    path('', include('contract.urls')),
    # /event, /status_event
    path('', include('event.urls')),
]

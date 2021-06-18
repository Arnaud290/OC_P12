"""General url module"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/log_viewer/', include('log_viewer.urls')),
    path('admin/', admin.site.urls),
    path('', include('authentification.urls')),
    path('contact/', include('contact.urls')),
    path('client/', include('client.urls')),
    path('', include('contract.urls')),
    path('', include('event.urls')),
]

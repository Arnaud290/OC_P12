from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentification.urls')),
    path('', include('client.urls')),
    path('', include('contract.urls')),
    path('', include('event.urls')),
]

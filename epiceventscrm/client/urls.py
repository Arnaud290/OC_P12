from django.urls import path, include
from rest_framework.routers import DefaultRouter
from client import views

router = DefaultRouter()
router.register(r'client', views.ClientViewSet)
urlpatterns = [
    path('', include(router.urls)),
]

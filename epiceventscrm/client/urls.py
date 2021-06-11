from django.urls import path, include
from rest_framework.routers import SimpleRouter
from client import views

router = SimpleRouter()
router.register(r'client', views.ClientViewSet)
urlpatterns = [
    path('', include(router.urls)),
]

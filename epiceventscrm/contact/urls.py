"""Contact urls module"""
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from contact import views

router = SimpleRouter()
router.register(r'', views.ContactViewSet)
urlpatterns = [
    path('', include(router.urls)),
]

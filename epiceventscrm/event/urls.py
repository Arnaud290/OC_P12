from django.urls import path, include
from rest_framework.routers import SimpleRouter
from event import views

router = SimpleRouter()
router.register(r'event', views.EventViewSet)
urlpatterns = [
    path('', include(router.urls)),
]

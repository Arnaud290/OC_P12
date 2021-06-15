from django.urls import path, include
from rest_framework.routers import SimpleRouter
from event import views

router = SimpleRouter()
router.register(r'', views.EventViewSet)
router.register(r'status_event', views.StatusViewSet)
urlpatterns = [
    path('', include(router.urls)),
]

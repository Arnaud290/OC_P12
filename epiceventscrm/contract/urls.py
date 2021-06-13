from django.urls import path, include
from rest_framework.routers import SimpleRouter
from contract import views

router = SimpleRouter()
router.register(r'contract', views.ContractViewSet)
urlpatterns = [
    path('', include(router.urls)),
]

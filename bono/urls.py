# bono/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import BonoViewSet, GeneratedBonoViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'bonos', BonoViewSet, basename='bono')
router.register(r'generated-bonos', GeneratedBonoViewSet, basename='generated-bono')

urlpatterns = [
    path('', include(router.urls)),
]

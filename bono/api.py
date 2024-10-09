# bono/api.py
from rest_framework import viewsets
from .models import Bono, GeneratedBono
from .serializers import BonoSerializer, GeneratedBonoSerializer

class BonoViewSet(viewsets.ModelViewSet):
    queryset = Bono.objects.all()
    serializer_class = BonoSerializer

# GeneratedBono ViewSet
class GeneratedBonoViewSet(viewsets.ModelViewSet):
    queryset = GeneratedBono.objects.all()
    serializer_class = GeneratedBonoSerializer
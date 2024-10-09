# bono/views.py
from rest_framework import generics, response
from .models import Bono
from .serializers import BonoSerializer

class BonoListCreateView(generics.ListCreateAPIView):
    queryset = Bono.objects.all()
    serializer_class = BonoSerializer

class BonoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bono.objects.all()
    serializer_class = BonoSerializer

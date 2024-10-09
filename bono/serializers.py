
from rest_framework import serializers
from .models import Bono,GeneratedBono

# Bono Serializer
class BonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bono
        fields = '__all__'

# GeneratedBono Serializer
class GeneratedBonoSerializer(serializers.ModelSerializer):
    khat_owner_name = serializers.CharField(source='bono.khat_owner_name', read_only=True)
    khat_type = serializers.CharField(source='bono.khat_type', read_only=True)
    count = serializers.IntegerField(source='bono.count', read_only=True)

    class Meta:
        model = GeneratedBono
        fields = ['id', 'bono', 'khat_owner_name', 'khat_type', 'count', 'price', 'trader_signature', 'added_by']
from rest_framework import serializers
from .models import MiModelo

class MiModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiModelo
        fields = '__all__'
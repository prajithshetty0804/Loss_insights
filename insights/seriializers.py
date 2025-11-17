from rest_framework import serializers
from .models import Plant, WeeklyLoss

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

class WeeklyLossSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyLoss
        fields = '__all__'

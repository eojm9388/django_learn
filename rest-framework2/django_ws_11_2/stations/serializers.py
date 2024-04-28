from rest_framework import serializers
from .models import Station, Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class StationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'
        read_only_fields = ('address',)

class StationsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('address', 'is_opening',)
        
class StationsAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'
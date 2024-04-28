from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import LocationSerializer, StationsSerializer, StationsListSerializer, StationsAllSerializer

from .models import Location, Station



# Create your views here.
@api_view(['POST'])
def locations(request):
    if request.method == 'POST':
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def stations(request, location_pk):
    location = Location.objects.get(pk=location_pk)

    if request.method == 'POST':
        serializer = StationsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(address=location)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    
    
@api_view(['GET'])
def station_list(request):
    if request.method == 'GET':
        station_list = Station.objects.all()
        serializer = StationsListSerializer(station_list, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def station_all(request, station_pk):
    if request.method == 'GET':
        station = Station.objects.get(pk=station_pk)
        serializer = StationsAllSerializer(station)
        return Response(serializer.data)
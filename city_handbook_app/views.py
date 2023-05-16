from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView

from city_handbook_app.models import Establishment, EstCategory
from city_handbook_app.serializers import EstablishmentSerializer, EstCategorySerializer, EstabRetrieveSerializer

class EstablishmentViewSet(ModelViewSet):

    permission_classes = [AllowAny]
    queryset = Establishment.objects.all()
    #serializer_class = EstablishmentSerializer

    def get_serializer_class(self):
        print(self.action)
        if self.action == "retrieve":
            return EstabRetrieveSerializer
        return EstablishmentSerializer


class EstablishmentByCategory(ListAPIView):
    serializer_class = EstabRetrieveSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        queryset = Establishment.objects.filter(category_id=category_id)
        return queryset

class EstablishmentByCity(ListAPIView):
    serializer_class = EstabRetrieveSerializer

    def get_queryset(self):
        city_id = self.kwargs['city_id']
        queryset = Establishment.objects.filter(city_id=city_id)
        return queryset

class EstablishSearchByAddress(ListAPIView):
    serializer_class = EstabRetrieveSerializer

    def get_queryset(self):
        address = self.kwargs['address']
        return Establishment.objects.filter(address__icontains=address)

class EstablishSearchByName(ListAPIView):
    serializer_class = EstabRetrieveSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Establishment.objects.filter(name__icontains=name)








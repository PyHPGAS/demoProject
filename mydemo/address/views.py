from django.shortcuts import render
from address.models import Country, State, City
from address.serializers import CountrySerializer, StateSerializer, CitySerializer
from rest_framework import viewsets
# Create your views here.
class CountryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    serializer_class = CountrySerializer

    def get_queryset(self):

        try:
            return Country.objects.all()
        except Exception as err:
            return {}

class StateViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    serializer_class = StateSerializer

    def get_queryset(self):

        try:
            return State.objects.all()
        except Exception as err:
            return {}

class CityViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    serializer_class = CitySerializer

    def get_queryset(self):

        try:
            return City.objects.all()
        except Exception as err:
            return {}
from rest_framework import viewsets

from .. import models
from . import serializers


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = models.Collection.objects.all()
    serializer_class = serializers.CollectionSerializer


class ServerViewSet(viewsets.ModelViewSet):
    queryset = models.Server.objects.all()
    serializer_class = serializers.ServerSerializer


class ServerSchemeViewSet(viewsets.ModelViewSet):
    queryset = models.ServerScheme.objects.all()
    serializer_class = serializers.ServerSchemeSerializer


class GetLocationViewSet(viewsets.ModelViewSet):
    queryset = models.GetLocation.objects.all()
    serializer_class = serializers.GetLocationSerializer


class PostLocationViewSet(viewsets.ModelViewSet):
    queryset = models.PostLocation.objects.all()
    serializer_class = serializers.PostLocationSerializer


class FindLocationViewSet(viewsets.ModelViewSet):
    queryset = models.FindLocation.objects.all()
    serializer_class = serializers.FindLocationSerializer


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = models.Resource.objects.all()
    serializer_class = serializers.ResourceSerializer

from rest_framework import serializers

from .. import models


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Collection


class ServerSerializer(serializers.ModelSerializer):
    schemes = serializers.HyperlinkedIdentityField(
        view_name="serverscheme-detail", many=True, read_only=True)

    class Meta:
        model = models.Server


class ServerSchemeBasePathSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ServerSchemeBasePath


class ServerSchemeSerializer(serializers.ModelSerializer):
    base_paths = ServerSchemeBasePathSerializer(many=True)

    class Meta:
        model = models.ServerScheme


class GetLocationRelativePathSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GetLocationRelativePath


class PostLocationRelativePathSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostLocationRelativePath


class FindLocationRelativePathSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FindLocationRelativePath


class GetLocationSerializer(serializers.ModelSerializer):
    relative_paths = GetLocationRelativePathSerializer(many=True)

    class Meta:
        model = models.GetLocation


class PostLocationSerializer(serializers.ModelSerializer):
    relative_paths = PostLocationRelativePathSerializer(many=True)

    class Meta:
        model = models.PostLocation


class FindLocationSerializer(serializers.ModelSerializer):
    relative_paths = FindLocationRelativePathSerializer(many=True)

    class Meta:
        model = models.FindLocation


class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Parameter


class ResourceSerializer(serializers.ModelSerializer):
    parameters = ParameterSerializer(many=True)
    conductorsettings_getlocation_related = serializers.HyperlinkedIdentityField(
        view_name="getlocation-detail", many=True, read_only=True)
    conductorsettings_postlocation_related = serializers.HyperlinkedIdentityField(
        view_name="postlocation-detail", many=True, read_only=True)
    conductorsettings_findlocation_related = serializers.HyperlinkedIdentityField(
        view_name="findlocation-detail", many=True, read_only=True)

    class Meta:
        model = models.Resource

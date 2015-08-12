from __future__ import absolute_import
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from . import validators
from .enumerations import (ParameterType, TemporalSelectionRule,
                           ParameterSelectionRule, ServerSchemeMethod,
                           ConductorScheme)


# This model might be moved to another app
@python_2_unicode_compatible
class Collection(models.Model):
    short_name = models.CharField(max_length=20)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.short_name


@python_2_unicode_compatible
class Resource(models.Model):
    name = models.CharField(
        max_length=255, unique=True,
        validators=[validators.validate_no_whitespace]
    )
    local_pattern = models.CharField(max_length=255)
    urn_pattern = models.CharField(max_length=255)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Parameter(models.Model):
    VALUE_CHOICES = [(n, n) for n, m in ParameterType.__members__.items()]
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    value_type = models.CharField(
        max_length=50, choices=VALUE_CHOICES,
        default=ParameterType.NUMBER.name
    )
    resource = models.ForeignKey(Resource, related_name="parameters")

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Location(models.Model):
    resource = models.ForeignKey(
        Resource, related_name="%(app_label)s_%(class)s_related")
    server_scheme = models.ForeignKey(
        "ServerScheme", related_name="%(app_label)s_%(class)s_related")
    media_type = models.CharField(max_length=50)
    authorization = models.CharField(max_length=100, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "{0.resource} - {0.server_scheme}".format(self)


# TODO: Investigate if adding the server_scheme field here and
#    using the ForeignKey.limit_choices_to attribute will work
#    and be more intuitive
class GetLocation(Location):
    pass


class PostLocation(Location):
    pass


class FindLocation(Location):
    temporal_choices = [(n, n) for n, m in
                        TemporalSelectionRule.__members__.items()]
    parameter_choices = [(n, n) for n, m in
                         ParameterSelectionRule.__members__.items()]
    temporal_rule = models.CharField(max_length=30, choices=temporal_choices,
                                     default=TemporalSelectionRule.LATEST.name)
    parameter = models.ForeignKey(Parameter, related_name="+")
    parameter_rule = models.CharField(
        max_length=30, choices=parameter_choices,
        default=ParameterSelectionRule.HIGHEST.name
    )
    lock_timeslot_year = models.BooleanField()
    lock_timeslot_month = models.BooleanField()
    lock_timeslot_day = models.BooleanField()
    lock_timeslot_hour = models.BooleanField()
    lock_timeslot_minute = models.BooleanField()
    lock_dekade = models.BooleanField()


@python_2_unicode_compatible
class LocationRelativePath(models.Model):
    path = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.path


class FindLocationRelativePath(LocationRelativePath):
    # this class is needed because we need to establish a foreign key
    # to the Location model for each location type (find, get, post).
    # since the Location model is abstract, it cannot have relationships
    # defined (the table does not actually exist on the database).
    location = models.ForeignKey(FindLocation, related_name="relative_paths")


class GetLocationRelativePath(LocationRelativePath):
    # this class is needed because we need to establish a foreign key
    # to the Location model for each location type (find, get, post).
    # since the Location model is abstract, it cannot have relationships
    # defined (the table does not actually exist on the database).
    location = models.ForeignKey(GetLocation, related_name="relative_paths")


class PostLocationRelativePath(LocationRelativePath):
    # this class is needed because we need to establish a foreign key
    # to the Location model for each location type (find, get, post).
    # since the Location model is abstract, it cannot have relationships
    # defined (the table does not actually exist on the database).
    location = models.ForeignKey(PostLocation, related_name="relative_paths")


@python_2_unicode_compatible
class Server(models.Model):
    name = models.CharField(max_length=200, unique=True,
                            validators=[validators.validate_no_whitespace],
                            help_text="A friendly name for this server. It "
                                      "will be used throughout the settings.")
    domain = models.CharField(max_length=200,
                              help_text="The domain where this server is "
                                        "accessible.")

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class ServerScheme(models.Model):
    meth_choices = [(n, n) for n, m in
                    ServerSchemeMethod.__members__.items()]
    name_choices = [(n, n) for n, m in
                    ConductorScheme.__members__.items()]
    server = models.ForeignKey(Server, related_name="schemes")
    name = models.CharField(max_length=30, choices=name_choices,
                            help_text="Name of the scheme")
    method = models.CharField(max_length=30, choices=meth_choices,
                              help_text="What operation does this scheme "
                                        "support?")

    def __str__(self):
        return "{0.server}:{0.name}:{0.method}".format(self)


@python_2_unicode_compatible
class ServerSchemeBasePath(models.Model):
    path = models.CharField(max_length=255)
    server_scheme = models.ForeignKey(ServerScheme, related_name="base_paths")

    def __str__(self):
        return self.path

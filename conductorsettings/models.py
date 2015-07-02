from django.db import models

from . import (ServerSchemeMethod, ConductorScheme, ParameterType,
               TemporalRule, ParameterRule, TemporalPart)

# TODO - Add validators

class Server(models.Model):
    name = models.CharField(max_length=200,
                            help_text="A friendly name for this server. It "
                                      "will be used throughout the settings.")
    domain = models.CharField(max_length=200,
                              help_text="The domain where this server is "
                                        "accessible.")

    def __unicode__(self):
        return self.name

class ServerScheme(models.Model):
    meth_choices = [(n, n) for n, m in ServerSchemeMethod.__members__.items()]
    name_choices = [(n, n) for n, m in ConductorScheme.__members__.items()]
    server = models.ForeignKey(Server, related_name="schemes")
    name = models.CharField(max_length=30, choices=name_choices,
                            help_text="Name of the scheme")
    method = models.CharField(max_length=30, choices=meth_choices,
                              help_text="What operation does this scheme "
                                        "support?")

    def __unicode__(self):
        return "{0.server}:{0.name}:{0.method}".format(self)


class ServerSchemeBasePath(models.Model):
    path = models.CharField(max_length=255)
    server_scheme = models.ForeignKey(ServerScheme, related_name="base_paths")

    def __unicode__(self):
        return self.path


class Collection(models.Model):
    short_name = models.CharField(max_length=20)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.short_name


class Resource(models.Model):
    name = models.CharField(max_length=255)
    local_pattern = models.CharField(max_length=255)
    urn = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Parameter(models.Model):
    value_choices = [(n, n) for n, m in ParameterType.__members__.items()]
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    value_type = models.CharField(max_length=50, choices=value_choices,
                                  default=ParameterType.NUMBER.name)
    resource = models.ForeignKey(Resource, related_name="parameters")

    def __unicode__(self):
        return self.name


class Location(models.Model):
    resource = models.ForeignKey(
        Resource, related_name="%(app_label)s_%(class)s_related")
    server_scheme = models.ForeignKey(
        ServerScheme, related_name="%(app_label)s_%(class)s_related")
    media_type = models.CharField(max_length=50)
    authorization = models.CharField(max_length=100, blank=True)

    class Meta:
        abstract = True


class GetLocation(Location):
    pass


class PostLocation(Location):
    pass


class FindLocation(Location):
    temporal_choices = [(n, n) for n, m in TemporalRule.__members__.items()]
    parameter_choices = [(n, n) for n, m in ParameterRule.__members__.items()]
    temporal_rule = models.CharField(max_length=30, choices=temporal_choices,
                                     default=TemporalRule.LATEST.name)
    parameter = models.ForeignKey(Parameter, related_name="location")
    parameter_rule = models.CharField(max_length=30, choices=parameter_choices,
                                      default=ParameterRule.HIGHEST.name)
    lock_timeslot_year = models.BooleanField()
    lock_timeslot_month = models.BooleanField()
    lock_timeslot_day = models.BooleanField()
    lock_timeslot_hour = models.BooleanField()
    lock_timeslot_minute = models.BooleanField()
    lock_dekade = models.BooleanField()


class LocationRelativePath(models.Model):
    path = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.path


class FindLocationRelativePath(LocationRelativePath):
    location = models.ForeignKey(FindLocation, related_name="relative_paths")


class GetLocationRelativePath(LocationRelativePath):
    location = models.ForeignKey(GetLocation, related_name="relative_paths")


class PostLocationRelativePath(LocationRelativePath):
    location = models.ForeignKey(PostLocation, related_name="relative_paths")

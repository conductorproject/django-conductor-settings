from django.contrib import admin

from . import models

class ServerSchemeBasePathInline(admin.StackedInline):
    model = models.ServerSchemeBasePath
    extra = 1


class FindLocationRelativePathInline(admin.StackedInline):
    model = models.FindLocationRelativePath
    extra = 1


class GetLocationRelativePathInline(admin.StackedInline):
    model = models.GetLocationRelativePath
    extra = 1


class PostLocationRelativePathInline(admin.StackedInline):
    model = models.PostLocationRelativePath
    extra = 1


class ParameterInline(admin.StackedInline):
    model = models.Parameter
    extra = 1


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Server)
class ServerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ServerScheme)
class ServerSchemeAdmin(admin.ModelAdmin):
    inlines = [ServerSchemeBasePathInline,]
    list_display = ("id", "server", "name", "method",)


@admin.register(models.Resource)
class ResourceAdmin(admin.ModelAdmin):
    inlines = [ParameterInline,]
    list_display = ("id", "name", "local_pattern",)


@admin.register(models.FindLocation)
class FindLocationAdmin(admin.ModelAdmin):
    inlines = [FindLocationRelativePathInline,]


@admin.register(models.GetLocation)
class GetLocationAdmin(admin.ModelAdmin):
    inlines = [GetLocationRelativePathInline,]
    list_display = ("id", "resource", "server_scheme",)


@admin.register(models.PostLocation)
class PostLocationAdmin(admin.ModelAdmin):
    inlines = [PostLocationRelativePathInline,]

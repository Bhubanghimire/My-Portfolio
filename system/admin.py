from django.contrib import admin
from .models import ConfigChoice, ConfigCategory, Ad


# Register your models here.
@admin.register(ConfigCategory)
class PopularRouteAdmin(admin.ModelAdmin):
    list_display = ["id","type","description"]


@admin.register(ConfigChoice)
class PopularRouteAdmin(admin.ModelAdmin):
    list_display = ["id","value","description"]


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ["id","title","url","image"]
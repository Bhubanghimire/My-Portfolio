from django.contrib import admin
from .models import About,Experience,Education,Task,Testimonials,Fact,Portfolio,Skills


# Register your models here.
@admin.register(About)
class MyUserAdmin(admin.ModelAdmin):
    list_display = []


@admin.register(Education)
class MyUserAdmin(admin.ModelAdmin):
    list_display = []


@admin.register(Experience)
class MyUserAdmin(admin.ModelAdmin):
    list_display = []


@admin.register(Task)
class MyUserAdmin(admin.ModelAdmin):
    list_display = []

@admin.register(Testimonials)
class MyUserAdmin(admin.ModelAdmin):
    list_display = []


@admin.register(Fact)
class MyUserAdmin(admin.ModelAdmin):
    list_display = []

@admin.register(Portfolio)
class MyUserAdmin(admin.ModelAdmin):
    list_display = []

@admin.register(Skills)
class MyUserAdmin(admin.ModelAdmin):
    list_display = []
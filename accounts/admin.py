from django.contrib import admin
from .models import User, Contact, Address


# Register your models here.
@admin.register(User)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ["id",'email', 'first_name', 'last_name']


@admin.register(Contact)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ["id",'name', 'subject', 'message']


@admin.register(Address)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ["id","country","district","city"]
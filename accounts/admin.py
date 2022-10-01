from django.contrib import admin
from .models import User, Contact, Address, About, Skills, Testimonials, Services, Education, Experience, Portfolio, \
    Gallery


# Register your models here.
@admin.register(User)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ["id", 'email', 'first_name', 'last_name']


@admin.register(Contact)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ["id", 'first_name', 'subject', 'message']


@admin.register(Address)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ["id", "country", "district", "city"]


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ["id"]


@admin.register(Skills)
class AboutAdmin(admin.ModelAdmin):
    list_display = ["id"]


@admin.register(Testimonials)
class AboutAdmin(admin.ModelAdmin):
    list_display = ["id"]


@admin.register(Services)
class AboutAdmin(admin.ModelAdmin):
    list_display = ["id"]


@admin.register(Education)
class AboutAdmin(admin.ModelAdmin):
    list_display = ["id"]


@admin.register(Experience)
class AboutAdmin(admin.ModelAdmin):
    list_display = ["id"]


@admin.register(Portfolio)
class AboutAdmin(admin.ModelAdmin):
    list_display = ["id"]


@admin.register(Gallery)
class AboutAdmin(admin.ModelAdmin):
    list_display = ["id"]

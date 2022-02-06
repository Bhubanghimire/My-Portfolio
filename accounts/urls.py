from django.urls import path
from .views import Test,ContactUS, Detail

urlpatterns = [
    path("",Test,name="home"),
    path("portfolio/<int:id>/details", Detail,name="detail"),
    path("contact/",ContactUS,name="contact"),
    ]
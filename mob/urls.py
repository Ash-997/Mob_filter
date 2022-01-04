from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
path("", views.show, name="show"),
path("goom", views.gta, name="gta"),
]
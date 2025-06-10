from django.urls import path, include
from rest_framework import routers
from .views import satellite_map,satellite_api,get_drones,drone_map,dashboard,home



urlpatterns = [
    path('satellite_api/', satellite_api, name='satellite_api'),
    path('satellite_map/', satellite_map,name="satellite_map"),
    path('api/drones/', get_drones, name='get_drones'),
    path('drone_map',drone_map,name='drone_map'),
    path('dashboard',dashboard,name='dashboard'),
    path('',home,name='home')
]
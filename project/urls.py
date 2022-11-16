from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app.api import viewsets

route = routers.DefaultRouter()
route.register(r'users', viewsets.UsersViewSet, basename='Users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
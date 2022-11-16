from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from desafio_tech.api import viewsets

route = routers.DefaultRouter()
route.register(r'register', viewsets.RegisterUsersViewSet, basename='Register')
route.register(r'users', viewsets.UsersViewSet, basename='Users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
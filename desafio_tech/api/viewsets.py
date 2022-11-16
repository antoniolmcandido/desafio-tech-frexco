from rest_framework import viewsets
from rest_pandas import PandasViewSet
from desafio_tech.api import serializers
from desafio_tech import models

class RegisterUsersViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.RegisterUsersSerializer
  queryset = models.Users.objects.all()
  http_method_names = ['post']

class UsersViewSet(PandasViewSet):
  serializer_class = serializers.UsersSerializer
  queryset = models.Users.objects.all()
  http_method_names = ['get']
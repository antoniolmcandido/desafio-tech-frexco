from rest_framework import serializers
from desafio_tech import models

class RegisterUsersSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Users
    fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Users
    fields = '__all__'
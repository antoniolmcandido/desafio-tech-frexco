from rest_framework.serializers import ModelSerializer
from app import models

class UsersSerializer(ModelSerializer):  
  class Meta:
    model = models.Users
    fields = ('id_user', 'login', 'password', 'birth')
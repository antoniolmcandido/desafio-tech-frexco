from rest_framework.viewsets import ModelViewSet
from app.api import serializers
from app import models
from django.contrib.auth.base_user import BaseUserManager

class UsersViewSet(ModelViewSet):
  serializer_class = serializers.UsersSerializer
  queryset = models.Users.objects.all().order_by('login')



  # def create(self, request, *args, **kwargs):
  #   user = models.Users.objects.get(id=request.data['id_user'])
  #   if user.password == '':
  #     user.password = BaseUserManager().make_random_password()
  #   user.save()

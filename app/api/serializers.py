from rest_framework.serializers import ModelSerializer
from app.models import Users
from django.contrib.auth.base_user import BaseUserManager

class UsersSerializer(ModelSerializer):
  class Meta:
    model = Users
    fields = ('id_user', 'login', 'password', 'birth')

  def save(self):
    user = Users(        
        login = self.validated_data['login'], 
        birth = self.validated_data['birth'],
    )
    password = self.validated_data['password']

    # generating random password if empty
    if password == '': password = BaseUserManager().make_random_password()

    user.set_password(password)
    user.save()

    return user
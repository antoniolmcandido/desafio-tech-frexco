from rest_framework.viewsets import ModelViewSet
from app.api import serializers
from app.models import Users

class UsersViewSet(ModelViewSet):
  serializer_class = serializers.UsersSerializer
  queryset = Users.objects.all().order_by('login')
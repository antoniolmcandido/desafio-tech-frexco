from django.db import models
from uuid import uuid4

class Users(models.Model):
  id_user = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  login = models.EmailField(max_length=255, unique=True)
  password = models.CharField(max_length=50, blank=True, default='')
  birth = models.DateField()
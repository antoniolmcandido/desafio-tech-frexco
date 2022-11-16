from django.db import models
from uuid import uuid4
from random import choice
import string

class Users(models.Model):
  id_user = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  login = models.EmailField(max_length=255)

  # start defined random pass
  length = 8
  values = string.ascii_letters + string.digits + string.punctuation
  random_pass = ''
  for i in range(length):
    random_pass += choice(values)
  # end random pass

  password = models.CharField(default=random_pass, max_length=255)
  birth = models.DateField()
<h1 align="center">  Desafio Tech - Frexco (Django) </h1>

<img align="center" alt="Vini-Python" height="35" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" />
<img align="center" alt="Vini-django" height="30" width="40" src="https://www.vectorlogo.zone/logos/djangoproject/djangoproject-icon.svg" />

<p align="center">Construção de 2 endpoints para cadastro e consulta de usuários.<p>
<p align="center">
    <a href="##Autor">Autor</a> |
    <a href="##Empresa">Empresa Frexco</a>
</p>

## Autor

- [Antonio Leandro Martins Candido](https://antoniolmcandido.com)

## Empresa

<p style='margin: 16px 4px 32px;'>
	<a href="https://www.frexco.com.br/" target="_blank" rel="noreferrer">
        <img src="https://www.frexco.com.br/_next/static/media/logo.fbc69385.svg" alt="frexco" width="80" height="80" />
    </a>
</p>

## Configurações

Após realizar o download do projeto, execute os seguintes comandos:

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Dois módulos foram instalados para a possibilidade de consultas no formato xlsx e csv, caso não possua, realiza as instalações:

```
pip install drf-excel
pip install djangorestframework-csv
```

Após as instalações dos módulos renderers, edite o arquivo de configurações do projeto (settings.py):

```
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',                
        'drf_excel.renderers.XLSXRenderer',
        'rest_framework_csv.renderers.CSVRenderer',        
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]
}
```

Para realizar as consultas em formatos de mídias, use algum dos links abaixo:

```
http://127.0.0.1:8000/users/?format=json
http://127.0.0.1:8000/users/?format=xlsx
http://127.0.0.1:8000/users/?format=csv
http://127.0.0.1:8000/users/?format=api
```

Outro procedimento solicitado, foi a possibilidade de aceitar senhas em branco, gerando senhas aleatórias para a substituição. É possível realizar os testes com os exemplos abaixo:

```
{
  "login": "test1@test.com",
  "password": "",
  "birth": "2007-01-10"
}

{
  "login": "test2@test.com",
  "password": "12341234",
  "birth": "2005-07-22"
}
```

## Implementações

Model Users
```
from django.db import models
from uuid import uuid4

class Users(models.Model):
  id_user = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  login = models.EmailField(max_length=255, unique=True)
  password = models.CharField(max_length=50, blank=True, default='')
  birth = models.DateField()

  def set_password(self, new_password):
    self.password = new_password
```

Serializer Users
```
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
```

View Users
```
from rest_framework.viewsets import ModelViewSet
from app.api import serializers
from app.models import Users

class UsersViewSet(ModelViewSet):
  serializer_class = serializers.UsersSerializer
  queryset = Users.objects.all().order_by('login')
```

Rota Users
```
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
```

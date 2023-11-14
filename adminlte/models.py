from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    es_gerente = models.BooleanField(default=False)
    es_jefe_de_taller = models.BooleanField(default=False)
    es_vendedor = models.BooleanField(default=False)
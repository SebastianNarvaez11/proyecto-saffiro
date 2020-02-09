from django.db import models
from django_userforeignkey.models.fields import UserForeignKey

# Create your models here.

class ModeloBase(models.Model):
    estado = models.BooleanField(default=True)
    creacion = models.DateTimeField(auto_now_add=True)
    edicion = models.DateTimeField(auto_now=True)
    user_create = UserForeignKey(auto_user_add=True, related_name='+')
    user_update = UserForeignKey(auto_user=True, related_name='+')

    class Meta:
        abstract = True

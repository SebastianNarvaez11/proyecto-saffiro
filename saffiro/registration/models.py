from django.db import models
from core.models import ModeloBase
from empresa.models import Empresa
from django.contrib.auth.models import AbstractUser
import reversion

# Create your models here.


def custom_upload_to_user(instance, filename):
    # primero evalua si existen instancias anteriores de el objeto a crear
    if not User.objects.filter(pk=instance.pk):
        return 'user/' + filename
    else:
        old_instance = User.objects.get(pk=instance.pk)
        if old_instance.foto:
            old_instance.foto.delete()
            
        return 'user/' + filename

@reversion.register()
class User(AbstractUser, ModeloBase):
    empresa = models.ForeignKey(Empresa, verbose_name='Empresa', on_delete=models.SET_NULL, null=True)
    foto = models.ImageField('Foto', upload_to=custom_upload_to_user, null=True, blank=True)
from django.db import models
from core.models import ModeloBase
import reversion
from core.validators import *

# Create your models here.


def custom_upload_to_empresa(instance, filename):
    # primero evalua si existen instancias anteriores de el objeto a crear
    if not Empresa.objects.filter(pk=instance.pk):
        return 'empresa/' + filename
    else:
        old_instance = Empresa.objects.get(pk=instance.pk)
        old_instance.logo.delete()
        return 'empresa/' + filename


@reversion.register()
class Empresa(ModeloBase):
    nit = models.CharField('Nit', max_length=20)
    representante = models.CharField('Representante Legal', max_length=20, validators=[validate_only_letters])
    cedula = models.CharField('Cedula del representante', validators=[validate_only_numbers], max_length=20)
    nombre = models.CharField('Nombre', max_length=20, unique=True)
    logo = models.ImageField('Logo', upload_to=custom_upload_to_empresa)
    direccion = models.CharField('Direccion', max_length=20, null=True)
    telefono = models.CharField('Telefono', max_length=20, null=True, validators=[validate_only_numbers])
    email = models.EmailField('Email')
    disable = models.BooleanField('Inactiva', default=False)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['-creacion']


    def __str__(self):
        return self.nombre

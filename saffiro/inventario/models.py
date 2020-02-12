from django.db import models
from core.models import ModeloBase
from empresa.models import Empresa
from django.dispatch import receiver
from django.db.models.signals import post_save
import reversion

# Create your models here.


class Inventario(ModeloBase):
    empresa = models.OneToOneField(
        Empresa, verbose_name='Empresa', on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'

@receiver(post_save, sender=Empresa)
def create_inventario(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Inventario.objects.get_or_create(empresa=instance)



@reversion.register()
class Marca(ModeloBase):
    nombre = models.CharField('Nombre', max_length=15, unique=True)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

from django.db import models
import reversion

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
class Empresa(models.Model):
    nombre = models.CharField('Nombre', max_length=20, unique=True)
    logo = models.ImageField('Logo', upload_to=custom_upload_to_empresa)
    direccion = models.CharField('Direccion', max_length=20, null=True)
    telefono = models.CharField('Telefono', max_length=20, null=True)
    creacion = models.DateField('Fecha de creacion', auto_now_add=True)
    edicion = models.DateField('Fecha de edicion', auto_now=True)
    disable = models.BooleanField('Eliminado', default=False)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['-creacion']


    def __str__(self):
        return self.nombre

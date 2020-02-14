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
    
    def __str__(self):
        return self.empresa


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
        ordering = ['-creacion']
    
    def __str__(self):
        return self.nombre


@reversion.register()
class Categoria(ModeloBase):
    nombre = models.CharField('Nombre', max_length=15, unique=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-creacion']
    
    def __str__(self):
        return self.nombre


@reversion.register()
class UnidadMedida(ModeloBase):
    nombre = models.CharField('Nombre', max_length=15, unique=True)

    class Meta:
        verbose_name = 'Unidad de Medidad'
        verbose_name_plural = 'Unidades de Medidad'
        ordering = ['-creacion']

    def __str__(self):
        return self.nombre



def custom_upload_to_producto(instance, filename):
    # primero evalua si existen instancias anteriores de el objeto a crear
    if not Producto.objects.filter(pk=instance.pk):
        return 'producto/' + filename
    else:
        old_instance = Producto.objects.get(pk=instance.pk)
        old_instance.foto.delete()
        return 'producto/' + filename
        

@reversion.register()
class Producto(ModeloBase):
    nombre = models.CharField('Nombre', max_length=20, unique=True)
    codigo = models.CharField('Codigo', max_length=10, unique=True)
    referencia = models.CharField('Referencia', max_length=20, unique=True)
    descripcion = models.CharField('Descripcion', max_length=100, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, verbose_name='Categoria', on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, verbose_name='Marca', on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UnidadMedida, verbose_name='Unidad de medida', on_delete=models.CASCADE)
    foto = models.ImageField('Foto', upload_to=custom_upload_to_producto, null=True, blank=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-creacion']
    
    def __str__(self):
        return self.nombre

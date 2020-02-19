from django.db import models
from core.models import ModeloBase
from empresa.models import Empresa
from inventario.models import Producto
import reversion
from core.validators import *

# Create your models here.

@reversion.register()
class Proveedor(ModeloBase):
    nombre = models.CharField('Nombre', max_length=100, unique=True)
    direccion = models.CharField('Direccion', max_length=250, null=True, blank=True)
    contacto = models.CharField('Contacto', max_length=100)
    telefono = models.CharField('Telefono', max_length=15)
    email = models.CharField('Email', max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.nombre

@reversion.register()
class Compra(ModeloBase):
    empresa = models.ForeignKey(Empresa, verbose_name='Empresa', on_delete=models.CASCADE)
    codigo = models.IntegerField('Codigo')
    observacion = models.CharField('Observacion', max_length=100, null=True, blank=True)
    proveedor = models.ForeignKey(Proveedor, verbose_name='Proveedor', on_delete=models.CASCADE)
    sub_total = models.FloatField('Sub Total', default=0)
    descuento = models.FloatField('Descuento', default=0)
    total = models.FloatField('Total', default=0)

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'

    def __str__(self):
        return self.codigo


class DetalleCompra(ModeloBase):
    compra = models.ForeignKey(Compra, verbose_name='Compra', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, verbose_name='Producto', on_delete=models.CASCADE)
    cantidad = models.BigIntegerField('Cantidad', default=0)
    precio_compra = models.FloatField('Precio de compra', default=0)
    sub_total = models.FloatField('Sub-Total', default=0)
    descuento = models.FloatField('Descuento', default=0, null=True, blank=True)
    total = models.FloatField('Total', default=0)

    class Meta:
        verbose_name = 'Detalle Compra'
        verbose_name_plural = 'Detalles Compra'

    def __str__(self):
        return self.compra + self.nombre





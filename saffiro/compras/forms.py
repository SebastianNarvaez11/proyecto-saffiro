from django.forms import ModelForm
from .models import Compra, Proveedor


class ProveedorForm(ModelForm):

    class Meta:
        model = Proveedor
        fields = ['nombre', 'direccion', 'telefono',
                  'contacto', 'email']


class CompraForm(ModelForm):

    class Meta:
        model = Compra
        fields = ['codigo', 'observacion', 'proveedor',
                  'sub_total', 'descuento', 'total']

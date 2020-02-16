from django.forms import ModelForm
from django import forms
from core.validators import *
from .models import Producto


class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre', 'codigo', 'referencia',
                  'descripcion', 'categoria', 'marca', 'unidad_medida', 'foto']

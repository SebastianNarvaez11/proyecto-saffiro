from django.forms import ModelForm
from django import forms
from core.validators import *
from .models import Producto


class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre', 'codigo', 'referencia',
                  'descripcion', 'categoria', 'marca', 'unidad_medida', 'foto']
        widgets = {'categoria': forms.Select(attrs={'class': 'form-control custom-select'}),
                   'marca': forms.Select(attrs={'class': 'form-control custom-select'}),
                   'unidad_medida': forms.Select(attrs={'class': 'form-control custom-select'}),
                   }

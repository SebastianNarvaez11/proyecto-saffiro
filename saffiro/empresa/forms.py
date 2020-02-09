from django.forms import ModelForm
from .models import Empresa


class EmpresaForm(ModelForm):

    class Meta:
        model = Empresa
        fields = ['nit','representante', 'cedula', 'nombre', 'logo', 'direccion', 'telefono', 'email']


class EmpresaInactiveForm(ModelForm):

    class Meta:
        model = Empresa
        fields = ['disable']

from django.forms import ModelForm
from .models import Empresa


class EmpresaForm(ModelForm):

    class Meta:
        model = Empresa
        fields = ['nombre', 'logo', 'direccion', 'telefono']


class EmpresaInactiveForm(ModelForm):

    class Meta:
        model = Empresa
        fields = ['disable']

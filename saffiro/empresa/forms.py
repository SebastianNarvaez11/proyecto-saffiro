from django.forms import ModelForm
from .models import Empresa


class EmpresaForm(ModelForm):

    class Meta:
        model = Empresa
        fields = ['nombre', 'logo', 'direccion', 'telefono']


class EmpresaInactiveForm(ModelForm):

    class Meta:
        model = Empresa
        fields = ['id', 'disable']

    def clean(self):
        id = self.cleaned_data.get("id")
        if id == self.request.user.empresa.id:
            raise forms.ValidationError(
                "La empresa se encuentra activa")

        return email

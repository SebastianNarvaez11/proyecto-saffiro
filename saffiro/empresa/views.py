from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from core.views import Permisos
from .models import Empresa
from django.urls import reverse_lazy
from .forms import EmpresaForm

# Create your views here.


class EmpresaListView(Permisos, ListView):
    permission_required = 'empresa.view_empresa'
    model = Empresa



class EmpresaCreateView(Permisos, CreateView):
    permission_required = 'empresa.add_empresa'
    model = Empresa
    form_class = EmpresaForm
    success_url = reverse_lazy('empresa_urls:list')
    success_message = 'Empresa creada satisfactoriamente'



class EmpresaUpdateView(Permisos, UpdateView):
    permission_required = 'empresa.change_empresa'
    model = Empresa
    form_class = EmpresaForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('empresa_urls:list')
    success_message = 'Empresa actualizada satisfactoriamente'

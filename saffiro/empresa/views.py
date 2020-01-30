from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from core.views import Permisos
from .models import Empresa
from django.urls import reverse_lazy
from .forms import EmpresaForm
from django.contrib import messages

# Create your views here.


class EmpresaListView(Permisos, ListView):
    permission_required = 'empresa.view_empresa'
    model = Empresa

    # filtra el el queryset por empresa activa
    def get_queryset(self):
        return Empresa.objects.filter(disable=False)


class EmpresaListDisableView(EmpresaListView):
    template_name_suffix = '_list_disable'
    # filtra el el queryset por empresa inactiva
    def get_queryset(self):
        return Empresa.objects.filter(disable=True)



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


class EmpresaInactiveView(Permisos, UpdateView):
    permission_required = 'empresa.change_empresa'
    model = Empresa
    fields = ['disable']
    template_name_suffix = '_inactive_form'
    success_url = reverse_lazy('empresa_urls:list')
    success_message = 'Empresa inactivada satisfactoriamente'

    def form_valid(self, form):
        form.instance.disable = True
        return super().form_valid(form)


def EmpresaActive(request, id):
    empresa = Empresa.objects.get(id=id)
    empresa.disable = False
    empresa.save()
    messages.add_message(request, messages.SUCCESS, 'Empresa activada satisfactoriamente')
    return redirect('empresa_urls:list')
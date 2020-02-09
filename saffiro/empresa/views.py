from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from core.views import Permisos
from .models import Empresa
from django.urls import reverse_lazy
from .forms import EmpresaForm, EmpresaInactiveForm
from django.contrib import messages
import reversion

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

    @reversion.create_revision()
    def form_valid(self, form):
        empresa = form.save()
        # guardar el registro de cambios
        with reversion.create_revision():
            reversion.set_user(self.request.user)
            reversion.set_comment(
                "La empresa '" + empresa.nombre + "' ah sido creada")

        return super().form_valid(form)


class EmpresaUpdateView(Permisos, UpdateView):
    permission_required = 'empresa.change_empresa'
    model = Empresa
    form_class = EmpresaForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('empresa_urls:list')
    success_message = 'Empresa actualizada satisfactoriamente'

    @reversion.create_revision()
    def form_valid(self, form):
        empresa = form.save()
        # guardar el registro de cambios
        with reversion.create_revision():
            reversion.set_user(self.request.user)
            if form.changed_data:
                reversion.set_comment(
                    "La empresa '" + empresa.nombre + "' ah sido modificada en los campos: " + (", ".join(form.changed_data)))
            else:
                reversion.set_comment(
                    "La empresa '" + empresa.nombre + "' ah sido actualizada")

        return super().form_valid(form)


class EmpresaInactiveView(Permisos, UpdateView):
    permission_required = 'empresa.change_empresa'
    model = Empresa
    form_class = EmpresaInactiveForm
    template_name_suffix = '_inactive_form'
    success_url = reverse_lazy('empresa_urls:list')
    success_message = 'Empresa inactivada satisfactoriamente'

    def form_valid(self, form):
        form.instance.disable = True
        return super().form_valid(form)


def EmpresaInactive(request, id):
    empresa = Empresa.objects.get(id=id)
    if empresa.id == request.user.empresa.id:
        messages.add_message(request, messages.ERROR,
                             'La empresa no se puede inactivar, debido a que esta actualmente seleccionada')
        return redirect('empresa_urls:list')
    else:
        empresa.disable = True
        empresa.save()
        messages.add_message(request, messages.SUCCESS,
                             'Empresa inactivada satisfactoriamente')
        return redirect('empresa_urls:list')


def EmpresaActive(request, id):
    empresa = Empresa.objects.get(id=id)
    empresa.disable = False
    empresa.save()
    messages.add_message(request, messages.SUCCESS,
                         'Empresa activada satisfactoriamente')
    return redirect('empresa_urls:list')

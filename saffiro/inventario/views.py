from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Marca
from core.views import Permisos
from django.urls import reverse_lazy
import reversion
from django.contrib import messages

# Create your views here.


class MarcaListView(Permisos, ListView):
    permission_required = 'inventario.view_marca'
    model = Marca



class MarcaCreateView(Permisos, CreateView):
    permission_required = 'inventario.add_marca'
    model = Marca
    fields = ['nombre', 'estado']
    success_url = reverse_lazy('marca_urls:list')
    success_message = 'Marca creada satisfactoriamente'

    @reversion.create_revision()
    def form_valid(self, form):
        marca = form.save()
        with reversion.create_revision():
            reversion.set_user(self.request.user)
            reversion.set_comment(
                "La marca '" + marca.nombre + "' ah sido creada")

        return super().form_valid(form)


class MarcaUpdateView(Permisos, UpdateView):
    permission_required = 'inventario.change_marca'
    model = Marca
    fields = ['nombre']
    success_url = reverse_lazy('marca_urls:list')
    success_message = 'Marca actualizada satisfactoriamente'

    @reversion.create_revision()
    def form_valid(self, form):
        marca = form.save()
        with reversion.create_revision():
            reversion.set_user(self.request.user)
            reversion.set_comment(
                "La marca '" + marca.nombre + "' ah sido modificada")

        return super().form_valid(form)


def change_estado(request, id):
    marca = Marca.objects.get(id=id)
    if marca.estado:
        marca.estado = False
        marca.save()
        messages.add_message(request, messages.SUCCESS,
                             'Marca desactivada satisfactoriamente')
    else:
        marca.estado = True
        marca.save()
        messages.add_message(request, messages.SUCCESS,
                             'Marca activada satisfactoriamente')

    return redirect('marca_urls:list')

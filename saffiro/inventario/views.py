from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Marca, Categoria, UnidadMedida, Producto
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
    fields = ['nombre', 'estado']
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



class CategoriaListView(Permisos, ListView):
    permission_required = 'inventario.view_categoria'
    model = Categoria


class CategoriaCreateView(Permisos, CreateView):
    permission_required = 'inventario.add_categoria'
    model = Categoria
    fields = ['nombre', 'estado']
    success_url = reverse_lazy('categoria_urls:list')
    success_message = 'Categoria creada satisfactoriamente'

    @reversion.create_revision()
    def form_valid(self, form):
        categoria = form.save()
        with reversion.create_revision():
            reversion.set_user(self.request.user)
            reversion.set_comment(
                "La categoria '" + categoria.nombre + "' ah sido creada")

        return super().form_valid(form)


class CategoriaUpdateView(Permisos, UpdateView):
    permission_required = 'inventario.change_categoria'
    model = Categoria
    fields = ['nombre', 'estado']
    success_url = reverse_lazy('categoria_urls:list')
    success_message = 'Categoria actualizada satisfactoriamente'

    @reversion.create_revision()
    def form_valid(self, form):
        categoria = form.save()
        with reversion.create_revision():
            reversion.set_user(self.request.user)
            reversion.set_comment(
                "La categoria '" + categoria.nombre + "' ah sido modificada")

        return super().form_valid(form)



class UnidadMedidaListView(Permisos, ListView):
    permission_required = 'inventario.view_unidadmedida'
    model = UnidadMedida


class UnidadMedidaCreateView(Permisos, CreateView):
    permission_required = 'inventario.add_unidadmedida'
    model = UnidadMedida
    fields = ['nombre', 'estado']
    success_url = reverse_lazy('unidadmedida_urls:list')
    success_message = 'Unidad de medida creada satisfactoriamente'

    @reversion.create_revision()
    def form_valid(self, form):
        unidadmedida = form.save()
        with reversion.create_revision():
            reversion.set_user(self.request.user)
            reversion.set_comment(
                "La unidad de medida '" + unidadmedida.nombre + "' ah sido creada")

        return super().form_valid(form)


class UnidadMedidaUpdateView(Permisos, UpdateView):
    permission_required = 'inventario.change_unidadmedida'
    model = UnidadMedida
    fields = ['nombre', 'estado']
    success_url = reverse_lazy('unidadmedida_urls:list')
    success_message = 'Unidad de medida actualizada satisfactoriamente'

    @reversion.create_revision()
    def form_valid(self, form):
        unidadmedida = form.save()
        with reversion.create_revision():
            reversion.set_user(self.request.user)
            reversion.set_comment(
                "La unidad de medida '" + unidadmedida.nombre + "' ah sido modificada")

        return super().form_valid(form)
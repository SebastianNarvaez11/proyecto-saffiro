from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Marca, Categoria, UnidadMedida, Producto
from core.views import Permisos
from django.urls import reverse_lazy
import reversion
from django.contrib import messages
from .forms import ProductoForm

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


#########################################################################################################################################################################

class ProductoListView(Permisos, ListView):
    permission_required = 'inventario.view_producto'
    model = Producto

    def get_queryset(self):
        return Producto.objects.filter(estado=True)


class ProductoDisableListView(ProductoListView):
    template_name_suffix = '_list_disable'

    def get_queryset(self):
        return Producto.objects.filter(estado=False)


class ProductoCreateView(Permisos, CreateView):
    permission_required = 'inventario.add_producto'
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('producto_urls:list')
    success_message = 'Producto creado satisfactoriamente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.filter(estado=True)
        context['marcas'] = Marca.objects.filter(estado=True)
        context['unidad_medidas'] = UnidadMedida.objects.filter(estado=True)
        return context

    @reversion.create_revision()
    def form_valid(self, form):
        producto = form.save()
        with reversion.create_revision():
            reversion.set_user(self.request.user)
            reversion.set_comment(
                "El producto '" + producto.nombre + "' ah sido creado")

        return super().form_valid(form)


class ProductoUpdateView(Permisos, UpdateView):
    permission_required = 'inventario.change_producto'
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('producto_urls:list')
    success_message = 'Producto actualizado satisfactoriamente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.filter(estado=True)
        context['marcas'] = Marca.objects.filter(estado=True)
        context['unidad_medidas'] = UnidadMedida.objects.filter(estado=True)
        return context

    @reversion.create_revision()
    def form_valid(self, form):
        producto = form.save()
        with reversion.create_revision():
            reversion.set_user(self.request.user)
            if form.changed_data:
                reversion.set_comment(
                    "El producto '" + producto.nombre + "' ah sido modificado en los campos: " + (", ".join(form.changed_data)))
            else:
                reversion.set_comment(
                    "El producto '" + producto.nombre + "' ah sido actualizado")

        return super().form_valid(form)


class ProductoInactiveView(Permisos, UpdateView):
    permission_required = 'empresa.change_producto'
    model = Producto
    fields = ['estado']
    template_name_suffix = '_inactive_form'
    success_url = reverse_lazy('producto_urls:list')
    success_message = 'Producto inactivado satisfactoriamente'

    def form_valid(self, form):
        form.instance.estado = False
        return super().form_valid(form)


def ProductoActive(request, id):
    producto = Producto.objects.get(id=id)
    producto.estado = True
    producto.save()
    messages.add_message(request, messages.SUCCESS,
                         'Producto activado satisfactoriamente')
    return redirect('producto_urls:list')

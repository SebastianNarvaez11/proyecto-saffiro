from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from core.views import Permisos
from empresa.models import Empresa
from inventario.models import Producto
from .forms import CompraForm, ProveedorForm
from .models import Compra, DetalleCompra, Proveedor
from django.urls import reverse_lazy
import reversion

# Create your views here.


class ProveedorListView(Permisos, ListView):
    permission_required = 'compra.view_proveedor'
    model = Proveedor


class ProveedorCreateView(Permisos, CreateView):
    permission_required = 'compra.add_proveedor'
    model = Proveedor
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor_urls:list')
    success_message = 'Proveedor creado satisfactoriamente'

    @reversion.create_revision()
    def form_valid(self, form):
        proveedor = form.save()

        with reversion.create_revision():
            reversion.set_user(self.request.user)
            reversion.set_comment(
                "El proveedor '" + proveedor.nombre + "' ah sido creado")

        return super().form_valid(form)


class ProveedorUpdateView(Permisos, UpdateView):
    permission_required = 'compra.change_proveedor'
    model = Proveedor
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor_urls:list')
    success_message = 'Proveedor actualizado satisfactoriamente'

    @reversion.create_revision()
    def form_valid(self, form):
        proveedor = form.save()

        with reversion.create_revision():
            reversion.set_user(self.request.user)
            if form.changed_data:
                reversion.set_comment(
                    "El proveedor '" + proveedor.nombre + "' ah sido modificado en los campos: " + (", ".join(form.changed_data)))
            else:
                reversion.set_comment(
                    "El proveedor '" + proveedor.nombre + "' ah sido actualizado")

        return super().form_valid(form)


class ComprasListView(Permisos, ListView):
    permission_required = 'compras.view_compra'
    model = Compra


class CompraProductosList(Permisos, ListView):
    permission_required = 'compras.view_compra'
    template_name = 'compras/productos.html'
    model = Producto


def Compra(request):
    productos = Producto.objects.filter(estado=True)
    proveedores = Proveedor.objects.filter(estado=True)
    form = {}
    empresa = request.user.empresa
    codigo = 0
    compras = empresa.compra_set.all()
    if compras:
        codigo = compras.length + 1
    else:
        codigo = 1

    return render(request, 'compras/compra.html', {'form': form, 'proveedores': proveedores, 'productos': productos, 'codigo': codigo})

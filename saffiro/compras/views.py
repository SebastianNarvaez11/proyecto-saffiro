from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from core.views import Permisos
from empresa.models import Empresa
from .models import Compra, DetalleCompra
from django.urls import reverse_lazy
import reversion

# Create your views here.

class ComprasListView(Permisos, ListView):
    permission_required = 'compras.view_compra'
    model = Compra
    
from django.urls import path
from .views import *

proveedor_urls = ([
    path('list/', ProveedorListView.as_view(), name='list'),
    path('create/', ProveedorCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProveedorUpdateView.as_view(), name='update')
],'proveedor_urls')

compra_urls = ([
    path('list/', ComprasListView.as_view(), name='list'),
    path('create/', Compra, name='create'),
    path('product/', CompraProductosList.as_view(), name= 'productos_list')
], 'compra_urls')

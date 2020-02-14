from django.urls import path
from .views import *

marca_urls = ([
    path('list/', MarcaListView.as_view(), name='list'),
    path('create/', MarcaCreateView.as_view(), name='create'),
    path('update/<int:pk>/', MarcaUpdateView.as_view(), name='update'),
], 'marca_urls')

categoria_urls = ([
    path('list/', CategoriaListView.as_view(), name='list'),
    path('create/', CategoriaCreateView.as_view(), name='create'),
    path('update/<int:pk>/', CategoriaUpdateView.as_view(), name='update'),
], 'categoria_urls')

unidadmedida_urls = ([
    path('list/', UnidadMedidaListView.as_view(), name='list'),
    path('create/', UnidadMedidaCreateView.as_view(), name='create'),
    path('update/<int:pk>/', UnidadMedidaUpdateView.as_view(), name='update'),
], 'unidadmedida_urls')

producto_urls = ([
    path('list/', ProductoListView.as_view(), name='list'),
    path('create/', ProductoCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductoUpdateView.as_view(), name='update'),
    path('disable-list/', ProductoDisableListView.as_view(), name='disable-list'),
    path('disable-form/<int:pk>/', ProductoInactiveView.as_view(), name='disable-form'),#muestra el formulario para desactivar
    path('active/<int:id>/', ProductoActive, name='active')#actualiza el estado ah activo
], 'producto_urls')


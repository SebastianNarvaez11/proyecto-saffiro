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

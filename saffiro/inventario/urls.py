from django.urls import path
from .views import *

marca_urls = ([
    path('list/', MarcaListView.as_view(), name='list'),
    path('create/', MarcaCreateView.as_view(), name='create'),
    path('update/<int:pk>/', MarcaUpdateView.as_view(), name='update'),
    path('disable/<int:id>/', change_estado, name='change_estado'),
], 'marca_urls')

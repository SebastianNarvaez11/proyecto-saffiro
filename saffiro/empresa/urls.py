from django.urls import path
from .views import *

empresa_urls = ([
    path('create/', EmpresaCreateView.as_view(), name='create'),
    path('list/', EmpresaListView.as_view(), name='list'),
    path('update/<int:pk>/',EmpresaUpdateView.as_view(), name = 'update'),
    path('delete/<int:pk>/', EmpresaDeleteView.as_view(), name='delete')
], 'empresa_urls')

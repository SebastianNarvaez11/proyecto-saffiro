from django.urls import path
from .views import *

empresa_urls = ([
    path('create/', EmpresaCreateView.as_view(), name='create'),
    path('list/', EmpresaListView.as_view(), name='list'),
    path('update/<int:pk>/', EmpresaUpdateView.as_view(), name='update'),
    path('disable-list/', EmpresaListDisableView.as_view(), name='disable-list'),#lista empresas inactivas
    path('disable/<int:pk>/', EmpresaInactiveView.as_view(), name='disable'),#actualiza el estado a inacativa
    path('active/<int:id>/', EmpresaActive, name='active')#actualiza el estado ah activa
], 'empresa_urls')

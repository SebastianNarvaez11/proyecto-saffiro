from django.urls import path
from .views import *

user_urls = ([
    path('create/', UserCreateView.as_view(), name='create'),
    path('list/', UserListView.as_view(), name='list'),
    path('empresa/', ChangeEmpresaView.as_view(), name='change_empresa')
],'user_urls')


from django.urls import path
from .views import *

user_urls = ([
    path('list/', UserListView.as_view(), name='list'),
    path('create/', UserCreateView.as_view(), name='create'),
    path('update/<int:pk>', UserUpdateView.as_view(), name='update'),
    path('empresa/', ChangeEmpresaView.as_view(), name='change_empresa')
],'user_urls')


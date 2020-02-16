from django.urls import path
from .views import *

compra_urls = ([
    path('list/', ComprasListView.as_view(), name='list')
],'compra_urls')
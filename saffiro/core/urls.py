from django.urls import path
from .views import *

urlpatterns = [
    path('',IndexTemplateView.as_view(), name='home'),
    path('change_e/<int:id_empresa>/', ChangeEmpresa, name='change_empresa'),
    path('record/', RevisionListView.as_view(), name='record')
]
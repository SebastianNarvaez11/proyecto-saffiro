from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from core.views import Permisos
from .models import User
from .forms import UserForm, ChangeEmpresaForm
from django.urls import reverse_lazy

# Create your views here.

class UserListView(Permisos, ListView):
    permission_required = 'auth.view_user'
    model = User

    # no mostrar en la lista, ni el usuario actual, ni los super usuarios
    def get_queryset(self):
        return User.objects.exclude(is_superuser=True).exclude(id=self.request.user.id)

        

class UserCreateView(Permisos, CreateView):
    permission_required = 'auth.add_user'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('user_urls:list')
    success_message = 'Usuario creado satisfactoriamente'

    # funcion le agrega los permisos(grupos) al usuario despues de crearlo
    def form_valid(self, form):
        user = form.save()
        grupos = form.cleaned_data.get("groups")
        for grupo in grupos:
            user.groups.add(grupo)
        return super().form_valid(form)





class ChangeEmpresaView(Permisos, UpdateView):
    permission_required = 'empresa.add_empresa'#se le pone este permiso, ya que el administrador sera el unico que lo tendra
    model = User
    form_class = ChangeEmpresaForm
    template_name = 'registration/empresa_change.html'
    success_message = 'Cambio realizado con exito'
    success_url = reverse_lazy('home')

    # obtener objeto que se va a editar para no pasar el id por la url
    def get_object(self):
        user = self.request.user
        return user





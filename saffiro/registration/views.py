from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from core.views import Permisos
from .models import User
from .forms import UserForm, ChangeEmpresaForm, UserUpdateForm
from django.urls import reverse_lazy
from django.contrib import messages
import reversion


# Create your views here.


class UserListView(Permisos, ListView):
    permission_required = 'auth.view_user'
    model = User

    # no mostrar en la lista, ni el usuario actual, ni los super usuarios
    # solo mostrar los usuarios que estan activos
    def get_queryset(self):
        return User.objects.exclude(is_superuser=True).exclude(id=self.request.user.id).exclude(is_active=False)


class UserListDisableView(UserListView):
    template_name_suffix = '_list_disable'

    # no mostrar en la lista, ni el usuario actual, ni los super usuarios
    # solo mostrar los usuarios que estan inactivos
    def get_queryset(self):
        return User.objects.exclude(is_superuser=True).exclude(id=self.request.user.id).exclude(is_active=True)


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


class UserUpdateView(Permisos, UpdateView):
    permission_required = 'auth.change_user'
    model = User
    form_class = UserUpdateForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('user_urls:list')
    success_message = 'Usuario actualizado satisfactoriamente'

    @reversion.create_revision()
    def form_valid(self, form):
        # cambia los permisos(grupos) al usuario despues de actualizarlo
        user = form.save()
        grupos = form.cleaned_data.get("groups")
        user.groups.set(grupos)

        # guardar el registro de cambios
        with reversion.create_revision():
            reversion.set_user(self.request.user)
            reversion.set_comment("Usuario '" + user.first_name + " " + user.last_name + "' ah sido modificado")

        return super().form_valid(form)


class UserInactiveView(Permisos, UpdateView):
    permission_required = 'auth.change_user'
    model = User
    fields = ['is_active']
    template_name_suffix = '_inactive_form'
    success_url = reverse_lazy('user_urls:list')
    success_message = 'Usuario inactivado satisfactoriamente'

    def form_valid(self, form):
        form.instance.is_active = False
        return super().form_valid(form)


class ChangeEmpresaView(Permisos, UpdateView):
    # se le pone este permiso, ya que el administrador sera el unico que lo tendra
    permission_required = 'empresa.add_empresa'
    model = User
    form_class = ChangeEmpresaForm
    template_name = 'registration/empresa_change.html'
    success_message = 'Cambio realizado con exito'
    success_url = reverse_lazy('home')

    # obtener objeto que se va a editar para no pasar el id por la url
    def get_object(self):
        user = self.request.user
        return user


def UserActive(request, id):
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    messages.add_message(request, messages.SUCCESS,
                         'Usuario activado satisfactoriamente')
    return redirect('user_urls:list')

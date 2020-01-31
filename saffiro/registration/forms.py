from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import User
from core.validators import *


class UserForm(UserCreationForm):
    username = forms.CharField(max_length=15, validators=[
                               MinLengthValidator(5)])
    first_name = forms.CharField(max_length=20, required=True, validators=[
                                 validate_only_letters, MinLengthValidator(2)])
    last_name = forms.CharField(max_length=20, required=True, validators=[
                                validate_only_letters, MinLengthValidator(2)])
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', 'groups', 'is_active', 'empresa', 'foto']
        widgets = {'empresa': forms.Select(attrs={'class': 'form-control custom-select'}),
                   'groups': forms.SelectMultiple(attrs={'class': 'custom-select'})
                   }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            username = self.cleaned_data.get("username")
            if not user.username == username:
                raise forms.ValidationError(
                    "El email ya existe, prueba con otro")

        return email


class UserUpdateForm(UserChangeForm):
    username = forms.CharField(max_length=15, validators=[
                               MinLengthValidator(5)])
    first_name = forms.CharField(max_length=20, required=True, validators=[
                                 validate_only_letters, MinLengthValidator(2)])
    last_name = forms.CharField(max_length=20, required=True, validators=[
                                validate_only_letters, MinLengthValidator(2)])
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'groups', 'empresa', 'foto']
        widgets = {'empresa': forms.Select(attrs={'class': 'form-control custom-select'}),
                   'groups': forms.SelectMultiple(attrs={'class': 'custom-select'})
                   }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        # comprobamos si el campo email se ah modificado
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError(
                    "El email ya existe, prueba con otro")

        return email


class ChangeEmpresaForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['empresa']
        widgets = {'empresa': forms.Select(
            attrs={'class': 'form-control custom-select'})}


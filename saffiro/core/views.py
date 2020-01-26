from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from registration.models import User
from empresa.models import Empresa
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
# Create your views here.

#formulario invalido con ajax
class MixinFormInvalid:
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response


@method_decorator(login_required, name='dispatch')
class Permisos(PermissionRequiredMixin, SuccessMessageMixin, MixinFormInvalid):
    raise_exception = False
    redirect_field_name = 'redirect_to'
    

class IndexTemplateView(Permisos, TemplateView):
    permission_required = 'sessions.add_session'
    template_name = 'core/home.html'


def ChangeEmpresa(request, id_empresa):
    empresa = get_object_or_404(Empresa, id=id_empresa)
    user = request.user
    user.empresa = empresa
    user.save()
    return redirect('home')
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from registration.models import User
from empresa.models import Empresa
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from reversion.models import Revision
import reversion
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.

# formulario invalido con ajax


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
    messages.add_message(request, messages.SUCCESS,
                         'Cambio realizado satisfactoriamente')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class RevisionListView(Permisos, ListView):
    permission_required = 'reversion.view_revision'
    model = Revision
    template_name = 'core/reversion_list.html'

    def get_queryset(self):
        return Revision.objects.exclude(user=None)


def RevisionDelete(request):
    historial = Revision.objects.exclude(user=None)
    for registro in historial:
        registro.delete()
    
    messages.add_message(request, messages.SUCCESS,
                         'Limpieza realizada satisfactoriamente')
    return redirect('record')

from empresa.models import Empresa

def empresa_ctx(request):
    if request.user.is_anonymous:
        return {}

    if not request.user.empresa:
        return {'Empresas':Empresa.objects.all()}
    
    id_empresa = request.user.empresa.id
    empresa = Empresa.objects.get(id=id_empresa)
    

    return {'Empresa':empresa}



def empresas_ctx(request):
        return {'Empresas':Empresa.objects.all()}

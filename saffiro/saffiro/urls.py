"""saffiro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from registration.urls import user_urls
from empresa.urls import empresa_urls
from inventario.urls import marca_urls, categoria_urls, unidadmedida_urls, producto_urls
# from core.urls import

urlpatterns = [
    # url home
    path('', include('core.urls')),
    # url crud marca
    path('marca/', include(marca_urls)),
    # url crud categorias
    path('categoria/', include(categoria_urls)),
    # url crud unidades de medida
    path('medida/', include(unidadmedida_urls)),
    # url crud empresas
    path('empresa/', include(empresa_urls)),
    # url crud producto
    path('producto/', include(producto_urls)),
    # url crud usuarios
    path('user/', include(user_urls)),
    # url de autenticacion
    path('accounts/', include('django.contrib.auth.urls')),
    # url admin django
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

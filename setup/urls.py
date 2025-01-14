"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from imobiliaria import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from setup.settings import MEDIA_ROOT


router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)
router.register('imoveis', views.ImoveisViewSet)
router.register('categorias', views.CategoriasViewSet)
router.register('categoriasGetAll', views.GetAllCategoriasViewSet)
router.register('tiposImoveis', views.TipoImovelViewSet)
router.register('tiposImoveisGetAll', views.GetAllTipoImovelViewSet)
router.register('fotosImovel', views.FotosImovelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', TokenObtainPairView.as_view()),
    path('tokenRefresh/', TokenRefreshView.as_view()),
    path('api/', include(router.urls)),
    path('', views.index),
    path('teste', views.index2)



] + static(settings.MEDIA_URL, document_root=MEDIA_ROOT)

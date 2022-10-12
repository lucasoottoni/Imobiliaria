from django.shortcuts import render
from django.contrib.auth.models import User, Group
from imobiliaria.models import Fotos, Imovel, TipoImovel, Categoria
from rest_framework import permissions, authentication, viewsets
from rest_framework.permissions import IsAuthenticated
from imobiliaria.serializers import FotosImoveisSerializer, UserSerializer, GroupSerializer, ImoveisSerializer, TipoImovelSerializer, CategoriaSerializer


from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
import json


@csrf_exempt
def login(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    if body['username']:
        user = authenticate(username=body['username'], password=body['password'])
        if user:
            token = Token.objects.get_or_create(user=user)
            return JsonResponse(  {'token': token[0].key, 'id': user.id, 'usuario': user.username, 'email': user.email, 'nome': user.first_name} )



def index(request):
    fazendas = Imovel.objects.all()
    print(request.build_absolute_uri())
    return render(request, 'index.html', {'fazendas': fazendas})


def index2(request): 
    fazendas = Imovel.objects.all()
    print('Olha o print ai', request.build_absolute_uri())
    return render(request, 'index2.html', {'fazendas': fazendas})
    
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = (authentication.TokenAuthentication,)

class ImoveisViewSet(viewsets.ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImoveisSerializer
    #authentication_classes = (authentication.TokenAuthentication,)

class CategoriasViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    #authentication_classes = (authentication.TokenAuthentication,)

class TipoImovelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = TipoImovel.objects.all()
    serializer_class = TipoImovelSerializer
    #authentication_classes = (authentication.TokenAuthentication,)
    
class FotosImovelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Fotos.objects.all()
    serializer_class = FotosImoveisSerializer
    #authentication_classes = (authentication.TokenAuthentication,)

from django.contrib.auth.models import User, Group
from imobiliaria.models import Imovel, Fotos, Categoria, TipoImovel
from rest_framework import serializers




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class FotosImoveisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fotos
        fields = ['id', 'descricao', 'foto']

class ImoveisSerializer(serializers.ModelSerializer):
    fotos = FotosImoveisSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = Imovel
        fields = ['id', 'nome', 'descricao', 'fotos', 'categoria', 'tipoImovel']

class TipoImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoImovel
        fields = ['id', 'nome', 'status']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'status']

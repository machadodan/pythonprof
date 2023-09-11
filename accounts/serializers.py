from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer, 
    TokenRefreshSerializer,
    TokenBlacklistSerializer,
    )


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # o pop remove o elemento da lista e retorna para 
        # elemento data uma nova chave token e o acess e apagado
        # ai adiciona tokenOb... em settings TOKEN_OBTAIN_SERIALIZER
        data["token"] = data.pop("access")
        data["refresh_token"] = data.pop("refresh")
        return data


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    refresh_token = serializers.CharField(required=True)
    refresh = None

    # removo refresh_token attribuo refresh ao attrs original
    def validate(self, attrs):
        attrs["refresh"] = attrs.pop("refresh_token")
        # atribuo o attrs ao variavel data
        data = super().validate(attrs)
        # removo access de data e atribuo o token
        data["token"] = data.pop("access")
        # removo o refresh e atribuo o refresh_token
        data["refresh_token"] = data.pop("refresh")
        # retorno o refresh_token como esperado
        # configuro em settings do app setup
        return data

class CustomTokenBlacklistSerializer(TokenBlacklistSerializer):
    refresh_token = serializers.CharField(required=True)
    refresh = None

    def validate(self, attrs):
        attrs["refresh"] = attrs.pop("refresh_token")
        # retorno super direto não precisa retornar nada no
        # corpo da resposta visto que estou fazendo logout
        # porem precisa criar view customizada em views
        return super().validate(attrs)










from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenBlacklistView


class CustomTokenBlackListView(TokenBlacklistView):
    def post(self, request, *args, **kwargs):
        # chama super para colocar retorno na blackList
        super().post(request, *args, **kwargs)
        # e muda o status do retorno
        # sendo 205 
        return Response(status=status.HTTP_205_RESET_CONTENT)

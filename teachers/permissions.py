from rest_framework.permissions import BasePermission

class TeacherListPermission(BasePermission):
    def has_permission(self, request, view):
        # se request method não estiver em put ou delete        
        if request.method not in ("PUT", "DELETE"):
            # retorno verdadeiro(ou seja se for um get, post, patch...)
            return True
        # se não retorno, se for put ou delete tenho quer ter
        # um usuario dentro dessa requisição e esse usuario
        # tem que ta autenticado
        return request.user and request.user.is_authenticated

      
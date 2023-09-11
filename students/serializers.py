from rest_framework import serializers
from django.utils import timezone

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(required=True, min_length=3, max_length=100, source="name")
    data_aula = serializers.DateTimeField(required=True, source="class_date")

    
    class Meta:
        model = Student
        fields = ("id", "nome", "data_aula", "email",  "created_at", "updated_at")
        # campo precisa extra.. por ele é somente leitura
        extra_kwargs = {
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
            }
    
    # criando validação data_aula
    # importado biblioteca timezone porque ela trabalha
    # com fuso horario o datetime do python nao
    def validate_data_aula(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError(" A data da aula deve ser no futuro")
        return value



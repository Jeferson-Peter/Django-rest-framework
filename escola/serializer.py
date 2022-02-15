from rest_framework import serializers
from escola.models import Aluno, Curso

class AlunoSerializer(serializers.ModelSerializers):
    class Meta:
        model = Aluno
        field = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializers):
    class Meta:
        model = Curso
        fields

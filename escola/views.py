from rest_framework import viewsets
from escola.models import Aluno, Curso
from .serializer import AlunoSerializer, CursoSerializer

class AlunoViewSet(viewsets.ViewSet):
    """Exibir todos od alunos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursoViewSet(viewsets.ViewSet):
    """Exibir todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
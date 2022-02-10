from django.http import JsonResponse

def alunos(request):
    if request.method == 'GET':
        aluno = {
            "id":1,
            "nome": "jeferson"
        }
        return JsonResponse(aluno)
from django.shortcuts import render

def pagina_inicial(request):
    nome_visitante = request.GET.get('nome', 'Viajante')
    contexto = {
        'nome': nome_visitante
    }
    return render(request, 'viagens/index.html', contexto)

def catalogo(request):
    return render(request, 'viagens/catalogo.html')

# Tirei os acentos do nome da função e do HTML!
def descricao(request):
    return render(request, 'viagens/descricao.html')
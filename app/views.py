from django.shortcuts import render

def index(request):
    return render(request, 'app/index.html')

def visao(request):
    return render(request, 'app/visao.html')

def elenco(request):
    lista_elenco = [
        {"nome": "Juno Temple", "idade": 36, "Profissão": "Atriz inglesa", "Personagem": "Ivy"},
        {"nome": "Tracy Morgan", "idade": 57, "Profissão": "Ator e comediante", "Personagem": "Boogle"},
        {"nome": "Michael B. Jordan", "idade": 39, "Profissão": "Ator norte-americano", "Personagem": "Ollie"},
        {"nome": "Ambika Mod", "idade": 30, "Profissão": "Atriz e comediante", "Personagem": "Violet"},
        {"nome": "Cedric the Entertainer", "idade": 62, "Profissão": "Ator e comediante", "Personagem": "Caloo"},
        {"nome": "Justina Machado", "idade": 53, "Profissão": "Atriz americana", "Personagem": "Calli"},
    ]

    context = {
        "elenco": lista_elenco,
    }
    return render(request, 'app/elenco.html', context)

def sobre(request):
    return render(request, 'app/sobre.html')
from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat


# Create your views here.

def index(request):
    contatos = Contato.objects.order_by('-id')
    paginator = Paginator(contatos, 20)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def ver_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })


def busca(request):
    campos = Concat('nome', Value(' '), 'sobrenome')
    termo = request.GET.get('termo')
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )
    paginator = Paginator(contatos, 20)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


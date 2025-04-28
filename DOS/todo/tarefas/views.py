from django.shortcuts import render
from .models import Tarefa, Usuario
from datetime import datetime
from django.http import HttpResponseRedirect

# Create your views here.

def listarTarefas(request):

    tarefas = Tarefa.objects.all()

    return render(request, "listarTarefas.html",{"tarefas" : tarefas})

def listarUsuarios(request):

    usuarios = Usuario.objects.all()

    return render(request, "listarUsuarios.html",{"usuarios" : usuarios})

def cadastroAtividade(request):

    if(request.method == "POST"):
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        ano = int(request.POST.get('data').split("-")[0])
        mes = int(request.POST.get('data').split("-")[1])
        dia = int(request.POST.get('data').split("-")[2])
        data = datetime(ano,mes,dia)
        usuario = Usuario.objects.get(id = request.POST.get('usuario'))

        nova_atividade = Tarefa(titulo=titulo, 
                                descricao=descricao, 
                                data=data, 
                                usuario=usuario)
        nova_atividade.save()

        return HttpResponseRedirect('/tarefas/listartarefas')

    usuarios = Usuario.objects.all()

    return render(request, "cadastroAtividade.html", {'usuarios':usuarios})

def cadastroUsuario(request):

    if(request.method == "POST"):
        nome = request.POST.get('nome')
        email = request.POST.get('email')

        novo_usuario = Usuario(nome=nome, 
                                email=email)
        novo_usuario.save()

        return HttpResponseRedirect('/tarefas/listarusuarios')

    return render(request, "cadastroUsuario.html")

def excluirAtividade(request, id):
    tarefa = Tarefa.objects.get(id=id)
    tarefa.delete()
    return HttpResponseRedirect('/tarefas/listartarefas')

def excluirUsuario(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return HttpResponseRedirect('/tarefas/listarusuarios')
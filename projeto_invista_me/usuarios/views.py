from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def novo_usuario(request):
    #tipo, validar, informar e salvar
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            #salvar
            formulario.save()
            #informar
            usuario = formulario.cleaned_data.get('username')
            messages.success(request, f'O usuario {usuario} foi criado com sucesso!')
            return redirect('investimentos')           
    return render(request, 'usuarios/registrar.html', {'formulario': formulario})


from dataclasses import dataclass
import email
from email import message
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm



# Create your views here.
def home(request):
    return render(request, 'home.html')

##Formumlário de usuários para cadastro.
def create(request):
    return render(request, 'create.html')

##inserindo dados de usuários no bd
def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'As senhas não conferem!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['name'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuário cadastrado com Sucesso'
        data['class'] = 'alert-sucess'    
    return render(request, 'create.html', data)

    ##Painel do Login.
def painel(request):
    return render(request, 'painel.html')

     ##Processamento de Login.
def mlogin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou senha inválidos!'
        data['class'] = 'alert-danger'  
        return render(request, 'painel.html', data)

   ##Dashboard inicial da pagina test.
def dashboard(request):
    return render(request, 'dashboard/home.html')        


  ##logout do usuário no sistema. Ò_Ó'
def mlogout(request):
    logout(request)
    return redirect('/painel/')   


  ##Trocando a senha. Amém 3x 
  ##quebrado. funcional mas sem exibição da html
def alterar_senha(request):
    data = {}
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            data['msg'] = 'Senha alterada com Sucesso'
            data['class'] = 'alert-sucess' 
            return render(request, 'painel.html', data)
    else:
        form_senha = PasswordChangeForm(request.user)
    return render(request, 'alterar_senha.html', {'form_senha': form_senha})


   
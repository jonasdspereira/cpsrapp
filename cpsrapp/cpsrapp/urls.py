"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from ast import Store
from email.mime import image
from venv import create
from django.contrib import admin
from django.urls import path, include
from cpsr.views import home, create, store, painel, mlogin, dashboard, mlogout, alterar_senha


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('create/', create),
    path('store/', store),
    path('painel/', painel),
    path('mlogin/', mlogin),
    path('dashboard/', dashboard),
    path('mlogout/', mlogout),
    path('alterar_senha/', alterar_senha, name='alterar_senha'),
    path('morador/', include('morador.urls')), 

 
 
    
]

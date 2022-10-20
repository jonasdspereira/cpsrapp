from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.shortcuts import render
from morador.models import Morador
from django.urls import reverse_lazy

class MoradorList(ListView):
    model = Morador
    queryset = Morador.objects.all()

class MoradorCreate(CreateView):
    model = Morador
    fields = '__all__'
    success_url = reverse_lazy('morador:list')

class MoradorUpdate(UpdateView):
    model = Morador
    fields = '__all__'
    success_url = reverse_lazy('morador:list')

class MoradorDetail(DetailView):
    queryset = Morador.objects.all()

class MoradorDelete(DeleteView):
    queryset = Morador.objects.all()
    success_url = reverse_lazy('morador:list')
from django.urls import path
from morador import views

app_name = 'morador'

urlpatterns = [
    path('', views.MoradorList.as_view(), name='list'),
    path('create/', views.MoradorCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.MoradorUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.MoradorDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.MoradorDelete.as_view(), name='delete'),
]
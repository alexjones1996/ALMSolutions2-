from django.urls import path
from . import views

urlpatterns = [
    path('', views.financeiro, name='financeiro'),
    path('<int:entrada_id>/', views.entrada, name='entradas'),
]
from django.urls import path
from . import views

app_name ='financeiro'
urlpatterns = [
    path('', views.consulta_evento, name='consulta_evento'),
    path('criar_evento', views.criar_evento, name='criar_evento'),
]
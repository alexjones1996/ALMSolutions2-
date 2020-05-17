from django.urls import path
from .views import consulta_evento, criar_evento, atualizar_evento, apagar_evento

urlpatterns = [
    path('', consulta_evento, name='consulta_evento'),
    path('criar_evento', criar_evento, name='criar_evento'),
    path('atualizar_evento/<int:id>/', atualizar_evento, name='atualizar_evento'),
    path('apagar_evento/<int:id>/', apagar_evento, name='apagar_evento'),
]
from django.urls import path
from . import views

app_name ='financeiro'
urlpatterns = [
    path('', views.financeiro, name='financeiro'),
    path('<int:entrada_id>/', views.entrada, name='entrada'),

]
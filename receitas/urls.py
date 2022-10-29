from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('receita<int:receita_id>', views.Receita, name="receita"),
]
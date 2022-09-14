from django.urls import path
from . import views

urlpatterns = [
    path('', views.Outros.as_view(), name='carros'),
    path('gerenciar/adicionar', views.Add_Car.as_view(), name='adicionar'),
]

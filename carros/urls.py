from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.Outros.as_view(), name='carros'),
    path('gerenciar/adicionar', views.Add_Car.as_view(), name='adicionar'),
    path('carro/<int:pk>/', views.car, name='carro'),
    path('allProducts/', views.Gerenciar.as_view(), name='gerenciar'),
    path('allProducts/edit/<int:pk>/', views.edit_car, name='editar'),
    path('allProducts/delete/<int:pk>/', views.remove, name='deletar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

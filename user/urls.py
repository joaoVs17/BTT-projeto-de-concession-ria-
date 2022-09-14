from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login_screen.as_view(), name='login'),
    path('createAccount/', views.CreateAccount_screen.as_view(), name='create_account'),
    path('exit/', views.exit, name='exit')
]

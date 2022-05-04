from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name='login'),
    path('editar/perfil/', views.editar, name='editar'),
    path('perfil/', views.perfil, name='perfil'), 
]
 
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/', views.Register, name="register"),
    path('login/', views.Login, name='login'),
    path('editar/perfil/', views.Editar, name='editar'),
    path('perfil/', views.Perfil, name='perfil'), 
]
 
from django.urls import path,include
from . import views


urlpatterns = [
    path('formulario_post/', views.Formulario_posteo, name='formulario_post'),
]
 
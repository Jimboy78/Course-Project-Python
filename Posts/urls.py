from django.urls import path
from . import views

urlpatterns = [
    path('formulario_post/', views.formulario_posteo, name='formulario_post'),
    path('lista_post/', views.lista_post, name='Lista_posts'),
    path(r'^delete_post/(?P<pk>\d+)/$', views.Delete_Post.as_view(), name='delete_posts'),
    path(r'^detalle_post/(?P<pk>\d+)/$', views.Detalle_Post.as_view(), name='detalle_posts'),
]
  
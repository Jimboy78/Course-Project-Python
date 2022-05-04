from django.urls import path
from . import views

urlpatterns = [
    path('formulario_post/', views.formulario_posteo, name='formulario_post'),
    path('lista_post/', views.lista_post, name='Lista_posts'),
    path(r'^delete_post/(?P<pk>\d+)/$', views.DeletePost.as_view(), name='delete_posts'),
    path(r'^detalle_post/(?P<pk>\d+)/$', views.DetallePost.as_view(), name='detalle_posts'),
]
  
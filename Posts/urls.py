from django.urls import path
from . import views

urlpatterns = [
    path('formulario_post/', views.Formulario_posteo, name='formulario_post'),
    path('lista_post/', views.Lista_post, name='Lista_posts'),
    path(r'^delete_post/(?P<pk>\d+)/$', views.Delete_post.as_view(), name='delete_posts'),
    path(r'^detalle_post/(?P<pk>\d+)/$', views.Detalle_post.as_view(), name='detalle_posts'),
]
  
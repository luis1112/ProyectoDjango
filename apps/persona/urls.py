from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.principal, name="persona"),
    path('registrar_persona/', views.registrar_persona,name="registrar_persona"),
    path('anuncios/', views.mostrar_anuncios, name="anuncios"),
    path('anuncios/postular', views.postular, name="postular"),
    path('anuncios/ver_postulaciones', views.ver_postulaciones, name="ver_postulaciones"),
    path('anuncios/crear_anuncio/', views.crear_anuncio, name="crearanuncios"),
    path('anuncios/buscar_anuncio/', views.buscar_anuncios, name="buscaranuncios"),
    path('anuncios/modificar_anuncio/', views.modificar_anuncio,name="modificaranuncios"),
    path('anuncios/eliminar_anuncio/', views.eliminar_anuncio,name="eliminaranuncios"),
] 
from django.urls import path
from .views import InicioListView, NosotrosTemplateView, ContactoTemplateView, ArtistaDetailView, ArtistaCreateView, ComentarioView, CancionListView, UserListView

app_name = 'apps.blog'

urlpatterns = [
    path(
        route='',
        view=InicioListView.as_view(),
        name='inicio'
    ),
    path(
        route='nosotros/',
        view=NosotrosTemplateView.as_view(),
        name='nosotros'
    ),
    path(
        route='contacto/',
        view=ContactoTemplateView.as_view(),
        name='contacto'
    ),
    path(
        route='artista/<slug:url>/',
        view=ArtistaDetailView.as_view(),
        name='detalle'
    ),
        path(
        route='carga_auto/',
        view=ArtistaCreateView.as_view(),
        name='carga_artista'
    ),
    path(
        route='comentario/',
        view=ComentarioView.as_view(),
        name='comentario'
    ),
    path(
        route='cancion/<int:cancion_id>/',
        view=CancionListView.as_view(),
        name='cancion'
    ),
    path(
        route='user/<str:nombre>/',
        view=UserListView.as_view(),
        name='user'
    ),
]
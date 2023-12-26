from django.urls import path
from .views import InicioListView, NosotrosTemplateView, ContactoFormView, ContactoTemplateView, ArtistaDetailView, ArtistaCreateView, ArtistaUpdateView, ArtistaDeleteView, ComentarioCreateView, ComentarioDeleteView, CancionListView, UserListView

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
        view=ContactoFormView.as_view(),
        name='contacto'
    ),    
    path(
        route='contactook/',
        view=ContactoTemplateView.as_view(),
        name='contactook'
    ),
    path(
        route='artista/<slug:url>/',
        view=ArtistaDetailView.as_view(),
        name='detalle'
    ),
        path(
        route='cargar_artista/',
        view=ArtistaCreateView.as_view(),
        name='cargar_artista'
    ),
        path(
        route='actualizar_artista/<slug:url>/',
        view=ArtistaUpdateView.as_view(),
        name='actualizar_artista'
    ),
        path(
        route='eliminar_artista/<slug:url>/',
        view=ArtistaDeleteView.as_view(),
        name='eliminar_artista'
    ),
    path(
        route='comentario/',
        view=ComentarioCreateView.as_view(),
        name='comentario'
    ),
    path(
        route='eliminar_comentario/<int:pk>/',
        view=ComentarioDeleteView.as_view(),
        name='eliminar_comentario'
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
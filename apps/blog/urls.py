from django.urls import path 
from .views import (
    DiscoListView, DiscoDetailView, DiscoCreateView, DiscoUpdateview, DiscoDeleteView,
    CancionListView, CancionDetailView, CancionCreateView, CancionUpdateview, CancionDeleteView,
    CancionDiscoListView, CancionDiscoDetailView, CancionDiscoCreateView, CancionDiscoUpdateview, CancionDiscoDeleteView,
    ArtistaListView, ArtistaDetailView, ArtistaCreateView, ArtistaUpdateview, ArtistaDeleteView,
    CompositorListView, CompositorDetailView, CompositorCreateView, CompositorUpdateview, CompositorDeleteView,
    ProduccionListView, ProduccionDetailView, ProduccionCreateView, ProduccionUpdateview, ProduccionDeleteView)
urlpatterns = [
    path('disco/list/', DiscoListView.as_view(), name= 'disco_list'),
    path('disco/<int:pk>/', DiscoDetailView.as_view(), name='disco_detail'),
    path('disco/create/', DiscoCreateView.as_view(), name='disco_create'),
    path('disco/<int:pk>/update/', DiscoUpdateview.as_view(), name='disco_update'),
    path('disco/<int:pk>/delete/', DiscoDeleteView.as_view(), name='disco_delete'),
    
    path('cancion/list/', CancionListView.as_view(), name= 'cancion_list'),
    path('cancion/<int:pk>/', CancionDetailView.as_view(), name='cancion_detail'),
    path('cancion/create/', CancionCreateView.as_view(), name='cancion_create'),
    path('cancion/<int:pk>/update/', CancionUpdateview.as_view(), name='cancion_update'),
    path('cancion/<int:pk>/delete/', CancionDeleteView.as_view(), name='cancion_delete'),
    
    path('cancion-disco/list/', CancionDiscoListView.as_view(), name= 'cancion_disco_list'),
    path('cancion-disco/<int:pk>/', CancionDiscoDetailView.as_view(), name='cancion_disco_detail'),
    path('cancion-disco/create/', CancionDiscoCreateView.as_view(), name='cancion_disco_create'),
    path('cancion-disco/<int:pk>/update/', CancionDiscoUpdateview.as_view(), name='cancion_disco_update'),
    path('cancion-disco/<int:pk>/delete/', CancionDiscoDeleteView.as_view(), name='cancion_disco_delete'),
    
    path('artista/list/', ArtistaListView.as_view(), name= 'artista_list'),
    path('artista/<int:pk>/', ArtistaDetailView.as_view(), name='artista_detail'),
    path('artista/create/', ArtistaCreateView.as_view(), name='artista_create'),
    path('artista/<int:pk>/update/', ArtistaUpdateview.as_view(), name='artista_update'),
    path('artista/<int:pk>/delete/', ArtistaDeleteView.as_view(), name='artista_delete'),
    
    path('compositor/list/', CompositorListView.as_view(), name= 'compositor_list'),
    path('compositor/<int:pk>/', CompositorDetailView.as_view(), name='compositor_detail'),
    path('compositor/create/', CompositorCreateView.as_view(), name='compositor_create'),
    path('compositor/<int:pk>/update/', CompositorUpdateview.as_view(), name='compositor_update'),
    path('compositor/<int:pk>/delete/', CompositorDeleteView.as_view(), name='compositor_delete'),
    
    path('produccion/list/', ProduccionListView.as_view(), name= 'produccion_list'),
    path('produccion/<int:pk>/', ProduccionDetailView.as_view(), name='produccion_detail'),
    path('produccion/create/', ProduccionCreateView.as_view(), name='produccion_create'),
    path('produccion/<int:pk>/update/', ProduccionUpdateview.as_view(), name='produccion_update'),
    path('produccion/<int:pk>/delete/', ProduccionDeleteView.as_view(), name='produccion_delete'),
]

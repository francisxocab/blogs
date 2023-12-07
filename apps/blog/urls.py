from django.urls import path 
from .views import (
    DiscoListView, DiscoDetailView, DiscoCreateView, DiscoUpdateview, DiscoDeleteView,
    CancionListView, CancionDetailView, CancionCreateView, CancionUpdateview, CancionDeleteView)
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
]

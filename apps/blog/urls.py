from django.urls import path 
from .views import (DiscoListView, DiscoDetailView, DiscoCreateView, DiscoUpdateview, DiscoDeleteView)
urlpatterns = [
    path('disco/list/', DiscoListView.as_view(), name= 'disco_list'),
    path('disco/<int:pk>/', DiscoDetailView.as_view(), name='disco_detail'),
    path('disco/create/', DiscoCreateView.as_view(), name='disco_create'),
    path('disco/<int:pk>/update/', DiscoUpdateview.as_view(), name='disco_update'),
    path('disco/<int:pk>/delete/', DiscoDeleteView.as_view(), name='disco_delete'),
]

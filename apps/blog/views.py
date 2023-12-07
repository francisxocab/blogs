from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Disco, Cancion

class DiscoListView(ListView):
    model = Disco
    template_name = 'blogs/discos/disco_list.html'
    context_object_name = 'discos'

class DiscoDetailView(DetailView):
    model = Disco
    template_name = 'blogs/discos/disco_detail.html'
    context_object_name = 'disco'

class DiscoCreateView(CreateView):
    model = Disco
    template_name = 'blogs/discos/disco_form.html'
    context_object_name = 'disco'
    fields = '__all__'
    success_url = reverse_lazy('disco_list')

class DiscoUpdateview(UpdateView):
    model = Disco
    template_name = 'blogs/discos/disco_form.html'
    context_object_name = 'disco'
    fields = '__all__'
    success_url = reverse_lazy('disco_list')

class DiscoDeleteView(DeleteView):
    model = Disco
    template_name = 'blogs/discos/disco_confirm_delete.html'
    context_object_name = 'discos'
    success_url = reverse_lazy('disco_list')

class CancionListView(ListView):
    model = Cancion
    template_name = 'blogs/canciones/cancion_list.html'
    context_object_name = 'canciones'

class CancionDetailView(DetailView):
    model = Cancion
    template_name = 'blogs/canciones/cancion_detail.html'
    context_object_name = 'cancion'

class CancionCreateView(CreateView):
    model = Cancion
    template_name = 'blogs/canciones/cancion_form.html'
    context_object_name = 'cancion'
    fields = '__all__'
    success_url = reverse_lazy('cancion_list')

class CancionUpdateview(UpdateView):
    model = Cancion
    template_name = 'blogs/canciones/cancion_form.html'
    context_object_name = 'cancion'
    fields = '__all__'
    success_url = reverse_lazy('cancion_list')

class CancionDeleteView(DeleteView):
    model = Cancion
    template_name = 'blogs/canciones/cancion_confirm_delete.html'
    context_object_name = 'cancion'
    success_url = reverse_lazy('cancion_list')
    

# Create your views here.

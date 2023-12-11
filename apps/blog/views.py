import os
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Disco, Cancion, CancionDisco, Artista, Compositor, Produccion

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
    context_object_name = 'disco'
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

class CancionDiscoListView(ListView):
    model = CancionDisco
    template_name = 'blogs/cancionesdiscos/cancion_disco_list.html'
    context_object_name = 'cancionesdiscos'

class CancionDiscoDetailView(DetailView):
    model = CancionDisco
    template_name = 'blogs/cancionesdiscos/cancion_disco_detail.html'
    context_object_name = 'canciondisco'

class CancionDiscoCreateView(CreateView):
    model = CancionDisco
    template_name = 'blogs/cancionesdiscos/cancion_disco_form.html'
    context_object_name = 'canciondisco'
    fields = '__all__'
    success_url = reverse_lazy('cancion_disco_list')

class CancionDiscoUpdateview(UpdateView):
    model = CancionDisco
    template_name = 'blogs/cancionesdiscos/cancion_disco_form.html'
    context_object_name = 'canciondisco' #el model del profe de relacion no tiene context
    fields = '__all__'
    success_url = reverse_lazy('cancion_disco_list')

class CancionDiscoDeleteView(DeleteView):
    model = CancionDisco
    template_name = 'blogs/cancionesdiscos/cancion_disco_confirm_delete.html'
    context_object_name = 'canciondisco' #el model del profe de relacion no tiene context
    success_url = reverse_lazy('cancion_disco_list')

class ArtistaListView(ListView):
    model = Artista
    template_name = 'blogs/artistas/artista_list.html'
    context_object_name = 'artistas'

class ArtistaDetailView(DetailView):
    model = Artista
    template_name = 'blogs/artistas/artista_detail.html'
    context_object_name = 'artista'

class ArtistaCreateView(CreateView):
    model = Artista
    template_name = 'blogs/artistas/artista_form.html'
    context_object_name = 'artista'
    fields = '__all__'
    success_url = reverse_lazy('artista_list')

class ArtistaUpdateview(UpdateView):
    model = Artista
    template_name = 'blogs/artistas/artista_form.html'
    context_object_name = 'artista'
    fields = '__all__'
    success_url = reverse_lazy('artista_list')

class ArtistaDeleteView(DeleteView):
   model = Artista
   template_name = 'blogs/artistas/artista_confirm_delete.html'
   context_object_name = 'artista'
   success_url = reverse_lazy('artista_list')
   
   def form_valid(self, form):
       artista = self.get_object()
       if artista.imagen:
           image_path = artista.imagen.path
           if os.path.exists(image_path):
                 os.remove(image_path)
       return super().form_valid(form)
   

class CompositorListView(ListView):
    model = Compositor
    template_name = 'blogs/compositores/compositor_list.html'
    context_object_name = 'compositores'

class CompositorDetailView(DetailView):
    model = Compositor
    template_name = 'blogs/compositores/compositor_detail.html'
    context_object_name = 'compositor'

class CompositorCreateView(CreateView):
    model = Compositor
    template_name = 'blogs/compositores/compositor_form.html'
    context_object_name = 'compositor'
    fields = '__all__'
    success_url = reverse_lazy('compositor_list')

class CompositorUpdateview(UpdateView):
    model = Compositor
    template_name = 'blogs/compositores/compositor_form.html'
    context_object_name = 'compositor'
    fields = '__all__'
    success_url = reverse_lazy('compositor_list')

class CompositorDeleteView(DeleteView):
    model = Compositor
    template_name = 'blogs/compositores/compositor_confirm_delete.html'
    context_object_name = 'compositor'
    success_url = reverse_lazy('compositor_list')

class ProduccionListView(ListView):
    model = Produccion
    template_name = 'blogs/producciones/produccion_list.html'
    context_object_name = 'producciones'

class ProduccionDetailView(DetailView):
    model = Produccion
    template_name = 'blogs/producciones/produccion_detail.html'
    context_object_name = 'produccion'

class ProduccionCreateView(CreateView):
    model = Produccion
    template_name = 'blogs/producciones/produccion_form.html'
    context_object_name = 'produccion'
    fields = '__all__'
    success_url = reverse_lazy('produccion_list')

class ProduccionUpdateview(UpdateView):
    model = Produccion
    template_name = 'blogs/producciones/produccion_form.html'
    context_object_name = 'produccion'
    fields = '__all__'
    success_url = reverse_lazy('produccion_list')

class ProduccionDeleteView(DeleteView):
    model = Produccion
    template_name = 'blogs/producciones/produccion_confirm_delete.html'
    context_object_name = 'produccion'
    success_url = reverse_lazy('produccion_list')

# Create your views here.

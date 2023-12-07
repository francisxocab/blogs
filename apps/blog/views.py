from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Disco

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
    

# Create your views here.

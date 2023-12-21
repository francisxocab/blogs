
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cancion, Artista, Comentario
from .forms import CrearComentarioForm, AutoForm

class ArtistaCreateView(CreateView):
    model = Artista 
    form_class = AutoForm
    template_name = 'blogs/artista/crear_artista.html'
    success_url = reverse_lazy('blog:inicio')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.perfil = self.request.user.perfil
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = 'Agregar Artista'
        return context

class ArtistaUpdateView(UpdateView):
    model = Artista
    form_class = AutoForm
    template_name = 'blogs/artista/crear_artista.html'
    slug_field = 'url'
    slug_url_kwarg = 'url'
    success_url = reverse_lazy('blog:inicio')


    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.perfil = self.request.user.perfil
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = 'Actualizar Artista'
        return context
    
class ArtistaDeleteView(DeleteView):
    model = Artista
    slug_field = 'url'
    slug_url_kwarg = 'url'
    success_url = reverse_lazy('blog:inicio')

class InicioListView(ListView):
    model = Artista
    template_name = 'blogs/index.html'
    context_object_name = 'artistas'
    paginate_by = 2
    ordering = ('-creado',)
    queryset = Artista.objects.filter(visible=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['canciones'] = Cancion.objects.all()
        context['artistas_destacados'] = Artista.objects.filter(
            destacado=True, visible=True)
        return context


class NosotrosTemplateView(TemplateView):
    template_name = 'blogs/nosotros.html'


class ContactoTemplateView(TemplateView):
    template_name = 'blogs/contacto.html'


class ArtistaDetailView(DetailView):
    model = Artista
    template_name = 'blogs/detalle.html'
    context_object_name = 'artista'
    slug_field = 'url'
    slug_url_kwarg = 'url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artistas'] = Artista.objects.filter(visible=True)
        context['canciones'] = Cancion.objects.all()
        context['comentarios'] = Comentario.objects.filter(
            visible=True, artista=self.get_object()).all()
        context['cantidad_comentarios'] = Comentario.objects.filter(
            visible=True, artista=self.get_object()).all().count()
        return context

class ComentarioView(UserPassesTestMixin, View):
    template_name = 'blogs/detalle.html'

    def test_func(self):
        allowed_groups = ['Colaborador', 'Administrador', 'Registrado']
        return self.request.user.is_authenticated and any(self.request.user.groups.filter(name=group).exists() for group in allowed_groups)

    def get(self, request, *args, **kwargs):
        return HttpResponse(status=405)

    def post(self, request, *args, **kwargs):
        url = request.POST.get('url')
        auto = {
            'user': request.user.id,
            'perfil': request.user.perfil.id,
            'comentario': request.POST.get('comentario'),
            'artista': request.POST.get('artista')
        }
        form = CrearComentarioForm(auto)
        if form.is_valid():
            form.save()
            return redirect('blog:detalle', url=url)
        else:
            return HttpResponse(status=500)


class CancionListView(ListView):
    model = Artista
    template_name = 'blogs/index.html'
    context_object_name = 'artistas'
    paginate_by = 2
    ordering = ('-creado',)

    def get_queryset(self):
        artista = None
        if self.kwargs['cancion_id']:
            cancion_id = self.kwargs['cancion_id']
            cancion = Cancion.objects.filter(id=cancion_id)[:1]
            artista = Artista.objects.filter(visible=True, cancion_disco__cancion=cancion)
        return artista

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['canciones'] = Cancion.objects.all()
        context['artistas_destacados'] = Artista.objects.filter(
            destacado=True, visible=True)
        return context


class UserListView(ListView):
    model = Artista
    template_name = 'blogs/index.html'
    context_object_name = 'artistas'
    paginate_by = 2
    ordering = ('-creado',)

    def get_queryset(self):
        artista = None
        if self.kwargs['nombre']:
            user_nombre = self.kwargs['nombre']
            user = User.objects.filter(username=user_nombre)[:1]
            artista = Artista.objects.filter(visible=True, user=user)
        return artista

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['canciones'] = Cancion.objects.all()
        context['artistas_destacados'] = Artista.objects.filter(
            destacado=True, visible=True)
        return context

import os
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cancion, Artista, Comentario
from .forms import CrearComentarioForm, AutoForm, ContactoForm

class ArtistaCreateView(UserPassesTestMixin, CreateView):
    model = Artista 
    form_class = AutoForm
    template_name = 'blogs/artista/crear_artista.html'
    success_url = reverse_lazy('blog:inicio')
    login_url = reverse_lazy('auth:login')

    def test_func(self):
        grupos = ['Administrador', 'Colaborador']
        return self.request.user.is_authenticated and any(self.request.user.groups.filter(name=grupo).exists() for grupo in grupos)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.perfil = self.request.user.perfil
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = 'Agregar Artista'
        return context

class ArtistaUpdateView(UserPassesTestMixin, CreateView):
    model = Artista
    form_class = AutoForm
    template_name = 'blogs/artista/crear_artista.html'
    slug_field = 'url'
    slug_url_kwarg = 'url'
    success_url = reverse_lazy('blog:inicio')
    login_url = reverse_lazy('auth:login')

    def test_func(self):
        grupos = ['Administrador']
        return self.request.user.is_authenticated and any(self.request.user.groups.filter(name=grupo).exists() for grupo in grupos) or self.request.user == self.get_object().user



    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.perfil = self.request.user.perfil
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = 'Actualizar Artista'
        return context
    
class ArtistaDeleteView(UserPassesTestMixin, CreateView):
    model = Artista
    slug_field = 'url'
    slug_url_kwarg = 'url'
    success_url = reverse_lazy('blog:inicio')
    login_url = reverse_lazy('auth:login')

    def test_func(self):
        grupos = ['Administrador']
        return self.request.user.is_authenticated and any(self.request.user.groups.filter(name=grupo).exists() for grupo in grupos) or self.request.user == self.get_object().user

    def form_valid(self, form):
        # Obtener el objeto Auto
        artista = self.get_object()

        # Eliminar la imagen adociada
        if artista.imagen:
            # Obtener la ruta completa del archivo de imagen
            image_path = artista.imagen.path

            # Verificar si el archivo existe y eliminarlo
            if os.path.exists(image_path):
                os.remove(image_path)

        return super().form_valid(form)



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

class ContactoFormView(FormView):
    form_class = ContactoForm
    template_name = 'blogs/contacto.html'
    success_url = reverse_lazy('blogs:contactook')

class ContactoTemplateView(TemplateView):
    template_name = 'blogs/contactook.html'


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

class ComentarioCreateView(UserPassesTestMixin, CreateView):
    model = Comentario
    form_class = CrearComentarioForm
    template_name = 'blogs/detalle.html'
    login_url = reverse_lazy('auth:login')

    def test_func(self):
        grupos = ['Colaborador', 'Administrador', 'Registrado']
        return self.request.user.is_authenticated and any(self.request.user.groups.filter(name=grupo).exists() for grupo in grupos)

    def get(self, request, *args, **kwargs):
        return HttpResponseForbidden("Acceso denegado. Método no permitido.")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.perfil = self.request.user.perfil
        return super().form_valid(form)

    def get_success_url(self):
        url = self.request.POST.get('url')
        return reverse_lazy('blog:detalle', kwargs={'url': url})

    def form_invalid(self, form):
        return HttpResponseServerError("Error interno al procesar el formulario.")


class ComentarioDeleteView(UserPassesTestMixin, DeleteView):
    model = Comentario
    login_url = reverse_lazy('auth:login')

    def test_func(self):
        grupos = ['Administrador']
        return self.request.user.is_authenticated and any(self.request.user.groups.filter(name=grupo).exists() for grupo in grupos) or self.request.user == self.get_object().user

    def get_success_url(self):
        url = self.object.artista.url
        return reverse_lazy('blog:detalle', kwargs={'url': url})



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

from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Comentario, Artista, Contacto


class CrearComentarioForm(forms.ModelForm):

    comentario = forms.CharField(required= True, widget=forms.Textarea)

    class Meta:
        model = Comentario
        fields = ('user', 'perfil', 'artista', 'comentario')


class AutoForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['titulo', 'resumen', 'contenido', 'destacado',
                  'visible', 'debut', 'imagen']

    titulo = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'})
    )
    resumen = forms.CharField(
        widget=CKEditorWidget(
            attrs={'class': 'form-control'})
    )
    contenido = forms.CharField(
        widget=CKEditorWidget(
            attrs={'class': 'form-control'})
    )
    destacado = forms.BooleanField(
        widget=forms.CheckboxInput(),
    
    )
    visible = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )    
    debut = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    imagen = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control-file'})
    )
    
class ContactoForm(forms.ModelForm):
        class Meta:
            model = Contacto
            fields = ('nombre', 'email', 'asunto', 'mensaje')

        nombre = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre y Apellido'}
        )
    )
        email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'}
        )
    )
        asunto = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Asunto'}
        )
    )
        mensaje = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Mensaje'}
        )
    )
#encoding:utf-8
from django.forms import ModelForm #utilizar los modelos ya declarados
from django import forms #declarar nuevas reglas para un formulario
from principal.models import Receta, Comentario #modelos de nuestra aplcacion principal

class ContactoForm(forms.Form):
	"""Este es mi primer formulario"""
	correo= forms.EmailField(label='Tu correo electronico')
	mensaje= forms.CharField(widget=forms.Textarea)



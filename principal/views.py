from principal.models import Receta, Comentario
from principal.forms import RecetaForm, ComentarioForm, ContactoForm
from django.shortcuts import render_to_response,get_object_or_404
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage

def inicio(request):
	recetas=Receta.objects.all()
	return render_to_response('inicio.html',{'recetas':recetas})

def sobre(request):
	html='<html><body>Proyecto de ejemplo en MDW</body></html>'
	return HttpResponse(html)

def usuarios(request):
	usuarios=User.objects.all()
	recetas=Receta.objects.all()
	return render_to_response('usuarios.html', {'usuarios':usuarios, 'recetas':recetas})

def lista_recetas(request):
	recetas=Receta.objects.all()
	return render_to_response('recetas.html',{'datos':recetas}, context_instance=RequestContext(request))

def detalle_receta(request,id_receta):
	dato=get_object_or_404(Receta,pk=id_receta)
	comentarios=Comentario.objects.filter(receta=dato)
	return render_to_response('receta.html',{'receta':dato, 'comentarios':comentarios}, context_instance=RequestContext(request))

def contacto(request):
	if request.method=='POST':
		formulario=ContactoForm(request.POST)
		if formulario.is_valid():
			titulo='Mensaje dede el recetario de Maestros del Web'
			contenido= formulario.cleaned_data['mensaje']+ "\n"
			contenido += 'Comunicarse a: ' + formulario.cleaned_data['correo']
			correo= EmailMessage(titulo, contenido, to=['danielrico.posada@gmail.com'])
			correo.send()
			return HttpResponseRedirect('/')
	else:
		formulario=ContactoForm()
	return render_to_response('contactoform.html',{'formulario':formulario}, context_instance=RequestContext(request))
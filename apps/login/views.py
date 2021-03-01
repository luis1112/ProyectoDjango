from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .forms import FormularioLogin

def ingresar(request):
	if request.method == 'POST':
		formulario = FormularioLogin(request.POST)
		if formulario.is_valid():
			usuario = request.POST['username']
			clave = request.POST['password']
			user = authenticate(username = usuario, password = clave)
			if user is not None:
				login(request, user)
				return HttpResponseRedirect(reverse('persona'))
			else:
				formulario = FormularioLogin()
				context = {
					'formulario' : formulario,
					'advertencia' : "Datos incorrectos",
					'color':"danger", 
				}
				return render (request, 'login/autenticar.html', context)	
	else:
		formulario = FormularioLogin()
		context = {
			'formulario' : formulario,
			'advertencia' : "Bienvenido, por favor inicia sesión!",
			'color':'success',
		}
		return render (request, 'login/autenticar.html', context)


def cerrar(request):
	logout(request)
	return HttpResponseRedirect(reverse('home_page'))


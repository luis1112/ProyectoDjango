from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .forms import FormularioLogin



def homePage(request):
	if request.method == 'POST':
		formulario = FormularioLogin(request.POST)
		if formulario.is_valid():
			usuario = request.POST['username']
			clave = request.POST['password']
			user = authenticate(username = usuario, password = clave)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect(reverse('persona'))
				else:
					print ('Usuario desactivado')
			else:
				print ('Usuario y/o contraseña incorrectos')		
	else:
		formulario = FormularioLogin()
		context = {
			'formulario' : formulario, 
		}
		return render(request,'home_page.html',context)

def cerrar(request):
	logout(request)
	formulario = FormularioLogin()
	context = {
		'formulario' : formulario, 
	}
	return render (request, 'home_page.html', context)

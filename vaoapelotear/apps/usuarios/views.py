from django.shortcuts import render, redirect
from .models import Perfil
from django.contrib.auth.models import User
from django.views.generic import FormView
from .forms import RegistroUsuarioForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.

def profile(request):
    if request.method == 'POST':
    	uid = request.session.get('user_id')
    	usu = User.objects.get(id=uid)
    	profile = Perfil(usuario=usu, dni=request.POST.get('txtDniUser'), celular=request.POST.get('txtCelularUser'))
    	profile.save()
    	backend = request.session['partial_pipeline']['backend']
    	return redirect('social:complete', backend=backend)

    return render(request, 'home/perfil.html')

def registrarUsuario(request):
	if request.method == 'POST':
		if request.POST.get('terminos') == '0':
			return render(request, 'home/registrousuario.html', {'errorTermino' : 'Para poder registrarse, debe de aceptar los Terminos y Condiciones.'})
		else:
			form = RegistroUsuarioForm(request.POST)
			if form.is_valid():
				form.save()
				return render(request, 'home/registrousuario.html', {'mensaje' : 'El usuario fue registrado correctamente.'})
	else:
		form = RegistroUsuarioForm()
	
	return render(request, 'home/registrousuario.html', {'form' : form})
		
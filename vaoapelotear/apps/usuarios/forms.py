from django import forms
from django.contrib.auth.forms import UserCreationForm   
from django.contrib.auth.models import User
from .models import Perfil

class RegistroUsuarioForm(UserCreationForm):
	email = forms.EmailField(required = True)
	first_name = forms.CharField(max_length=140)
	last_name = forms.CharField(max_length=140)
	dni = forms.CharField(max_length=8)
	celular = forms.CharField(max_length=15)

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'dni', 'celular', 'username', 'email', 'password1', 'password2')

	def clean_username(self):
		username = self.cleaned_data["username"]
		try:
			User._default_manager.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('El usuario ya existe, porfavor introduzca otro.')

	def clean_email(self):
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')
		if email and User.objects.filter(email=email).exclude(username=username).count():
			raise forms.ValidationError('El email introducido ya esta siendo utilizado por otro usuario.')
		return email

	def save(self, commit = True):
		user = super(RegistroUsuarioForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']

		if commit:
			user.save()
			perfil = Perfil()
			perfil.usuario = user
			perfil.dni = self.cleaned_data['dni']
			perfil.celular = self.cleaned_data['celular']
			perfil.save()
		return user
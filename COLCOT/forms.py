from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Ajout

class CreateUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	username = forms.CharField(required=True)
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	class Meta:
		model = User
		fields = ['username', 
				  'first_name', 
				  'last_name', 
				  'email',
				  'password1', 
				  'password2']

class AnnonceForm(forms.ModelForm):
	vendeur = forms.CharField(required=True).initial = 'admin'
	class Meta:
		model = Ajout
		fields = ['vendeur',
				  'titre',
				  'prix',
				  'category',
				  'modele',
				  'reference',
				  'Echelle',
				  'fabricant',
				  'description',
				  'je_possede',
				  'je_vend',
				  'je_recherche',
				  'docfile']
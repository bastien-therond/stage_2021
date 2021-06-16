from django.db import models
from django import forms
from django.conf import settings

# Create your models here.

class Product(models.Model):
	CATEGORY = (
			('Modelisme', 'Modelisme'),
			('Philatelie', 'Philatelie'),
            ('Oenologie', 'Oenologie'),
            ('Autres', 'Autres')
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

def group_based_upload_to(instance, filename):
    return "uploads/test/".format(instance.group.id, filename)

class Ajout(models.Model):
	CATEGORY = (
			('Modelisme', 'Modelisme'),
			('Philatelie', 'Philatelie'),
            ('Oenologie', 'Oenologie'),
            ('Autres', 'Autres')
			) 

	vendeur = models.CharField(max_length=200, null=True)
	titre = models.CharField(max_length=200, null=True)
	prix = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	modele = models.CharField(max_length=200, null=True, blank=True)
	reference = models.CharField(max_length=200, null=True)
	Echelle = models.FloatField(max_length=200, null=True)
	fabricant = models.CharField(max_length=200, null=True)
	description = models.CharField(max_length=1500, null=True, blank=True)
	je_possede = models.BooleanField()
	je_vend = models.BooleanField()
	je_recherche = models.BooleanField()
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	docfile = models.ImageField(upload_to='uploads/')

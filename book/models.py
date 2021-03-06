from django.conf import settings
from django.db import models

# Create your models here.

class Page_projet(models.Model):
	titre = models.CharField(max_length=200)
	text = models.TextField(blank=True)
	tag = models.CharField(max_length=200)
	description = models.TextField(default="")
	img_description = models.ImageField(upload_to = 'description_projets/', default = 'description_projets/no-img.jpg')


	def __str__(self):
		return self.tag

class Curivitae(models.Model):
	poste = models.CharField(max_length=200)
	poste_descrip = models.TextField(blank=True)
	date = models.CharField(max_length=200)
	entreprise = models.CharField(max_length=200, default="none")

	def __str__(self):
		return self.entreprise

class Skill(models.Model):
	nom = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	img = models.FileField(upload_to = 'image_skills/', default = 'image_skills/no-img.jpg')

	def __str__(self):
		return self.nom
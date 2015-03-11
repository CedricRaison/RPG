from django.db import models
from django.contrib.auth.models import User

def avatar_file_name(instance, filename):
	return '/'.join(['pnj', instance.nom, filename])

def item_file_name(instance, filename):
	return '/'.join(['item', instance.nom, filename])

class Quete(models.Model):
	nom = models.CharField(max_length=50)
	xp = models.IntegerField()
	item = models.ForeignKey('Item')
	
	def __str__(self):
		return self.nom

class Pnj(models.Model):
	nom = models.CharField(max_length=30)
	vie = models.IntegerField()
	force = models.IntegerField()
	xp = models.IntegerField()
	avatar = models.ImageField(upload_to=avatar_file_name)
	enigme = models.CharField(max_length=255)
	quete = models.ForeignKey('Quete')

	def __str__(self):
		return self.nom

class Reponse(models.Model):
	enigme = models.ForeignKey('Pnj')
	answer = models.CharField(max_length=255)

	def __str__(self):
		return self.answer

class Item(models.Model):
	nom = models.CharField(max_length=30)
	panoplie = models.CharField(max_length=30)
	vie = models.IntegerField()
	force = models.IntegerField()
	pourcXp = models.IntegerField()
	choices = (
		('arme', 'arme'),
		('chapeau', 'chapeau'),
		('cape', 'cape'),
		('botte', 'botte'),
	)
	typeOf = models.CharField(max_length=15, choices=choices)
	image = models.ImageField(upload_to=item_file_name)

	def __str__(self):
		return self.nom

class Sac(models.Model):
	personnage = models.ForeignKey('Personnage')
	item = models.ForeignKey('Item')

	def __str__(self):
		return self.personnage.nom + '-> ' + self.item.nom

class Shop(models.Model):
	item = models.ForeignKey('Item')
	inventaire = models.ForeignKey('Sac')

class Personnage(models.Model):
	nom = models.CharField(max_length=30, unique=True)
	xp = models.IntegerField()
	level = models.IntegerField()
	vie = models.IntegerField()
	force = models.IntegerField()
	arme = models.ForeignKey(Sac, related_name='arme', blank=True, null=True)
	chapeau = models.ForeignKey(Sac, related_name='chapeau', blank=True, null=True)
	cape = models.ForeignKey(Sac, related_name='cape', blank=True, null=True)
	botte = models.ForeignKey(Sac, related_name='botte', blank=True, null=True)
	inventaire = models.ManyToManyField(Item, through='sac', blank=True, null=True)
	user = models.ForeignKey(User)


	def __str__(self):
		return self.nom

class Profile(models.Model):
	user = models.OneToOneField(User)
	perso = models.ForeignKey(Personnage)

	def __str__(self):
		return self.perso.nom

class Etape(models.Model):
	personnage = models.ForeignKey(Personnage)
	quete = models.ForeignKey(Quete)
	etape = models.IntegerField()

	def __str__(self):
		return 'etapes: ' + str(self.etape)

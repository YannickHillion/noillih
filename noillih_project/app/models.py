from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

CHOICE_FORME_JURIDIQUE = (
	('Auto-entrepreneur','Auto-entrepreneur'),
	('EIRL','EIRL'),
	('EI','EI'),
	('SASU','SASU'),
	('SAS', 'SAS'),
	('SARL', 'SARL'),
	('EURL', 'EURL'),
	('SA', 'SA'),
	('SNC', 'SNC'),
	('CAE', 'CAE'),
	('Association', 'Association'),
	('SCI', 'SCI'),
	('Syndicat patronal', 'Syndicat patronal'),
)


CHOICE_STATUT_SERVICE = (
	('En cours','En cours'),
	('Terminé','Terminé'),
)

CHOICE_TYPE_DE_PAIEMENT = (
	('Comptant','Comptant'),
	('Mensuel','Mensuel'),
	('Annuel','Annuel'),
)

CHOICE_TYPE_DE_SERVICE = (
	('Développement','Développement'),
	('licence','licence'),
	('Hebergement','Hebergement'),
	('Maintenance','Maintenance'),
	('Conseil','Conseil'),
	('SEO & SEA','SEO & SEA'),
)

CHOICE_STATUT_FACTURE = (
	('Payé','Payé'),
	('En attente de paiement','En attente de paiement'),
	('En retard','En retard'),
)


# CONFIGURATION
class Entreprise(models.Model):
	#INFORMATIONS COMMERCIAL
	nom_commercial                = models.CharField(default="",max_length=200)
	logo                          = models.FileField(upload_to='logo_entreprise/', blank=True)
	#INFORMATIONS
	forme_juridique               = models.CharField(
	choices                       = CHOICE_FORME_JURIDIQUE, blank=True, null=True,max_length=200
	)
	raison_social                 = models.CharField(default="", max_length=200)
	capital_social                = models.CharField(default="", max_length=200)
	numero_SIREN                  = models.CharField(default="", max_length=100)
	adresse                       = models.CharField(default = "", max_length = 200)
	code_postal                   = models.CharField(default="", max_length=6)
	ville                         = models.CharField(default="", max_length=200)
	#INFORMATIONS DE CONTACT
	numero_de_telephone           = models.CharField(default="", max_length=100)
	adresse_email                 = models.CharField(default="", max_length = 200)
	#INFORMATIONS DU DIRIGEANT
	nom_dirigeant                 = models.CharField(default="", max_length = 200)
	prenom_dirigeant              = models.CharField(default="", max_length = 200)
	role_dirigeant                = models.CharField(default="", max_length = 200)
	numero_de_telephone_dirigeant = models.CharField(default="", max_length=100)
	adresse_email_dirigeant       = models.CharField(default="", max_length = 200)
	#Collaborateur
	collaborateur                 = models.ManyToManyField(User, related_name='collaborateur', blank=True)

	class Meta:
		verbose_name        = "Entreprise"
		verbose_name_plural = "Entreprises"
		ordering            = ['nom_commercial']

	def __str__(self):
		return self.nom_commercial




class Projet(models.Model):
	nom               = models.CharField(default="",max_length=200)
	descriptif        = models.TextField(default = "" ,null=True, blank=True)
	#Date
	date_modification = models.DateTimeField(auto_now=True)
	date_creation     = models.DateTimeField(auto_now_add=True)
	#Entreprise
	entreprise        = models.ForeignKey(Entreprise, on_delete=models.CASCADE, null=True)


	class Meta:
		verbose_name        = "Projet"
		verbose_name_plural = "Projets"
		ordering            = ['nom']

	def __str__(self):
		return self.nom



class Service(models.Model):
	type_de_service = models.CharField(
		choices = CHOICE_TYPE_DE_SERVICE,max_length=200
	)
	nom                           = models.CharField(default="",max_length=200)
	descriptif                    = models.TextField(default = "" ,null=True, blank=True)
	type_de_paiement = models.CharField(
		choices = CHOICE_TYPE_DE_PAIEMENT,max_length=200
	)
	prix_HT = models.FloatField(default="0.0")
	projet = models.ForeignKey(Projet, on_delete=models.CASCADE, null=True)
	statut = models.CharField(
		choices = CHOICE_STATUT_SERVICE,max_length=200
	)
	#Date
	date_debut = models.DateField(null=True)
	date_fin = models.DateField(null=True)
	#Date
	date_modification = models.DateTimeField(auto_now=True)
	date_creation = models.DateTimeField(auto_now_add=True)


	class Meta:
		verbose_name        = "Service"
		verbose_name_plural = "Services"
		ordering            = ['nom']

	def __str__(self):
		return self.nom




class Facture(models.Model):
	numero                    	  = models.CharField(default="",max_length=200)
	prix_HT = models.FloatField(default="0.00")
	fichier 		= models.FileField(upload_to='factures/', blank=True)
	statut = models.CharField(
		choices = CHOICE_STATUT_FACTURE,max_length=200
	)
	#Date
	date_modification = models.DateTimeField(auto_now=True)
	date_creation = models.DateTimeField(auto_now_add=True)
	#Entreprise
	service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)

	class Meta:
		verbose_name        = "Facture"
		verbose_name_plural = "Factures"
		ordering            = ['numero']

	def __str__(self):
		return self.numero

	def save(self, *args, **kwargs):
		self.prix_HT = round(self.prix_HT, 2)
		# self.fichier = "https://addons.prestashop.com/1371404-pbig/advance-invoice-delivery-credit-pdf-custom-number.jpg"
		super(Facture, self).save(*args, **kwargs)

	







# class Ticket(models.Model):
# 	numero                    	  = models.CharField(default="",max_length=200)
# 	prix_HT = models.FloatField(default="0.0")
# 	fichier 		= models.FileField(upload_to='factures/', blank=True)
# 	statut = models.CharField(
# 		choices = CHOICE_STATUT_FACTURE,max_length=200
# 	)
# 	#Date
# 	date_modification = models.DateTimeField(auto_now=True)
# 	date_creation = models.DateTimeField(auto_now_add=True)
# 	#Entreprise
# 	service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)

# 	class Meta:
# 		verbose_name        = "Facture"
# 		verbose_name_plural = "Factures"
# 		ordering            = ['numero']

# 	def __str__(self):
# 		return self.numero
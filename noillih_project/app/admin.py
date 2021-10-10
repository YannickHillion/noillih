from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import *
# Register your models here.

from django.utils.html import format_html
from django.urls import reverse

from django import forms
class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = [
            'prix_HT',
            'service',
            'statut',
        ]





class ProjetResource(resources.ModelResource):
	class Meta:
		model = Projet

class ServiceInline(NestedTabularInline):
	model = Service
	extra = 0

class ProjetAdmin(NestedModelAdmin,ImportExportModelAdmin):
	model = Projet
	list_display  = [field.name for field in model._meta.fields if field.name != "id"]
	list_filter   = [field.name for field in model._meta.fields if field.name != "id"]
	search_fields = [field.name for field in model._meta.fields if field.name != "id"]

	resource_class = ProjetResource
	inlines = [ServiceInline,]

	def get_queryset(self, request):
		qs = super(ProjetAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(entreprise__collaborateur__id=request.user.id)

admin.site.register(Projet, ProjetAdmin)




class EntrepriseResource(resources.ModelResource):
	class Meta:
		model = Entreprise

class EntrepriseAdmin(NestedModelAdmin,ImportExportModelAdmin):
	model = Entreprise
	list_display = ["entreprise_","nom_commercial","numero_de_telephone","adresse_email"]
	search_fields = ["nom_commercial"]

	resource_class = EntrepriseResource

	def entreprise_(self, obj):
		try:
			link = obj.logo.url
			html = '<img src="{}" width="30" height="30" style="border-radius:10px;"/>'.format(link)
		except:
			html = '<i class="fas fa-building"></i>'

		return format_html(html)


	def get_queryset(self, request):
		qs = super(EntrepriseAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(collaborateur__id=request.user.id)


admin.site.register(Entreprise, EntrepriseAdmin)








class FactureResource(resources.ModelResource):
	class Meta:
		model = Facture


class FactureAdmin(NestedModelAdmin,ImportExportModelAdmin):
	model = Facture
	form = FactureForm
	list_display = ["numero","statut_","service","prix_HT_","action"]
	list_filter = ["statut"]
	search_fields = ["statut"]
	# list_editable = ["service"]
	# date_hierarchy = 'date_creation'
	resource_class = FactureResource

	def statut_(self, obj):
	    colors = {
	        'Payé': '#38761d',
	        'En attente de paiement': '#ffe599',
	        'En retard': '#ff9999',       
	    }
	    return format_html(
	        '<b style="background:{};padding:5px;border-radius:5px;">{}</b>',
	        colors[obj.statut],
	        obj.statut,
	    )

	def prix_HT_(self, obj):
	    return format_html(
	        '<b >{} €</b>',
	        obj.prix_HT,
	    )

	def action(self, obj):
		try:
			link = obj.fichier.url
			html = '<a class="btn btn-outline-primary" href="{}" download/>Télécharger</a>'.format(link)
		except:
			html = '<button class="btn btn-outline-danger" disabled/>Non disponible</button>'
		return format_html(html)

	def get_queryset(self, request):
		qs = super(FactureAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(service__projet__entreprise__collaborateur__id=request.user.id)

admin.site.register(Facture, FactureAdmin)




admin.site.register(Service)
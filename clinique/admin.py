from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Patient)
admin.site.register(DossierMedical)
admin.site.register(RendezVous)
admin.site.register(Equipe)
admin.site.register(Tache)
admin.site.register(Medecin)
admin.site.register(Service)
admin.site.register(Departement)
admin.site.register(Clinique)
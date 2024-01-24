from django.db import models

class Patient(models.Model):
    NSS = models.CharField(max_length=16, primary_key=True)
    Nom = models.CharField(max_length=30)
    Prenom = models.CharField(max_length=30)
    DateDeNaissance = models.DateField(auto_now=True)

class DossierMedical(models.Model):
    NumDossier = models.IntegerField(primary_key=True, auto_created=True)

class Clinique(models.Model):
    NomClinique = models.CharField(max_length=30, primary_key=True)
    Adresse = models.CharField(max_length=200)

class RendezVous(models.Model):
    NumRdv = models.IntegerField(primary_key=True, auto_created=True)
    DateRdv = models.DateField()
    Cause = models.CharField(max_length=200)

class Departement(models.Model):
    NomDepartement = models.CharField(max_length=20, primary_key
                                      =True)
    
class Service(models.Model):
    NumService = models.IntegerField(primary_key=True, auto_created=True)

class Tache(models.Model):
    NumTache = models.IntegerField(primary_key=True, auto_created=True)

class Equipe(models.Model):
    NumEquipe = models.IntegerField(primary_key=True, auto_created=True)

class Medecin(models.Model):
    Nom = models.CharField(max_length=30, primary_key=True)
    Prenom = models.CharField(max_length=30)
    Specialite = models.CharField(max_length=20)



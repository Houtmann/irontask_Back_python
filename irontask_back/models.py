from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Benevole(models.Model):
    SEXE = (
        ('H', 'Homme'),
        ('F', 'Femme'),

    )
    id = models.AutoField(primary_key=True)

    nom = models.CharField(max_length=50)

    prenom = models.CharField(max_length=50)

    dateNaissance = models.DateField

    sexe = models.CharField(max_length=1, choices=SEXE)

    adresse = models.CharField(max_length=50)

    codePostal = models.CharField(max_length=5)

    ville = models.CharField(max_length=50)

    telephoneFixe = models.CharField(max_length=10)

    telephonePortable = models.CharField(max_length=10)

    email = models.EmailField

    def __str__(self):
        return self.nom + ' ' + self.prenom


class TypeTriathlon(models.Model):
    id = models.AutoField(primary_key=True)

    libelle = models.CharField(max_length=50, null=False, blank=False)

    distanceNatation = models.IntegerField(max_length=2, null=False, blank=False)

    distanceCyclisme = models.IntegerField(max_length=4, null=False, blank=False)

    distanceCoursePied = models.IntegerField(max_length=4, null=False, blank=False)
    def __str__(self):
        return self.libelle

class Triathlon(models.Model):
    id = models.AutoField(primary_key=True)

    date = models.DateField(null=False, blank=False)

    heureDepart = models.TimeField(null=False, blank=False)

    codePostal = models.CharField(max_length=5, null=False, blank=False)

    adresse = models.CharField(max_length=50, null=False, blank=False)

    ville = models.CharField(max_length=50, null=False, blank=False)
    typeTriathlon = models.ForeignKey(TypeTriathlon, on_delete=models.CASCADE)

    def __str__(self):
        return "Triathlon du "+ str(self.date) + ' a ' +self.ville



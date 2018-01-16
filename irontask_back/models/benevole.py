from django.db import models

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


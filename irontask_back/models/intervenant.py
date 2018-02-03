from django.db import models

class Intervenant(models.Model):
    siret = models.BigIntegerField(primary_key=True)

    raisonSocial = models.CharField(max_length=50)

    type = models.ForeignKey()

    adresse = models.CharField(max_length=50)

    codePostal = models.CharField(max_length=5)

    ville = models.CharField(max_length=50)

    telephoneFixe = models.CharField(max_length=10)

    telephonePortable = models.CharField(max_length=10)

    email = models.EmailField
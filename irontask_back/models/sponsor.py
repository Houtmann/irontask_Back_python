from django.db import models

class Sponsor(models.Model):

    siret = models.BigIntegerField(primary_key=True)

    raisonSocial = models.CharField(max_length=50)

    adresse = models.CharField(max_length=50)

    codePostal = models.CharField(max_length=5)

    ville = models.CharField(max_length=50)

    telephone = models.CharField(max_length=10)

    email = models.CharField(max_length=50)

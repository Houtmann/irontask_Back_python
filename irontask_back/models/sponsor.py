from django.db import models

class Sponsor(models.Model):
    siret = models.Big

    raisonSocial

    adresse

    codePostal

    ville

    telephone

    email

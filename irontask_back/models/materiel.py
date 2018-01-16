from django.db import models

class Materiel(models.Model):

    id_Matériel = models.AutoField(primary_key=True)

    nom = models.CharField(max_length=50)

    type = models.CharField(max_length=50)

    qteTotal = models.IntegerField

    lieuStockage = models.CharField(max_length=50)

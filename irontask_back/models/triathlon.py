from django.db import models
from ..models import typeTriathlon

class Triathlon(models.Model):
    id = models.AutoField(primary_key=True)

    date = models.DateField
    heureDepart = models.TimeField

    codePostal = models.CharField(max_length=5)

    adresse = models.CharField(max_length=50)

    ville = models.CharField(max_length=50)
    typeTriathlon = models.ForeignKey(typeTriathlon)


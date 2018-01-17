from django.db import models
from ..models import triathlon
from ..models import benevole

class Tache(models.Model):

    triathlon = models.ForeignKey(triathlon)
    typeTache = models.ForeignKey(typeTache)

 

    dateFin = models.DateField

    duree = models.TimeField
    nbJoursRappel = models.IntegerField
    tacheValider = models.BooleanField
    benevole = models.ForeignKey(benevole)

    class Meta:
         unique_together = (('triathlon', 'typeTache'),)
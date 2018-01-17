from django.db import models

class TypeTriathlon(models.Model):

    id = models.AutoField(primary_key=True)

    libelle = models.CharField(max_length=50)

    distanceNatation = models.IntegerField(max_length=2)

    distanceCyclisme = models.IntegerField(max_length=4)

    distanceCoursePied = models.IntegerField(max_length=4)

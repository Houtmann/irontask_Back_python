from django.db import models


class Catgorie(models.Model):
    id_catégorie = models.AutoField(db_column='Id_Catégorie', primary_key=True)  # Field name made lowercase.
    libellé = models.CharField(db_column='Libellé', max_length=50, blank=True, null=True)  # Field name made lowercase.
    agemin = models.IntegerField(db_column='AgeMin', blank=True, null=True)  # Field name made lowercase.
    agemax = models.IntegerField(db_column='AgeMax', blank=True, null=True)  # Field name made lowercase.
    sexe = models.IntegerField(db_column='Sexe', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'catégorie'

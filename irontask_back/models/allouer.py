from django.db import models


class Allouer(models.Model):
    id_matériel = models.CharField(db_column='Id_Matériel', primary_key=True,
                                   max_length=50)  # Field name made lowercase.
    id_triathlon = models.CharField(db_column='Id_Triathlon', max_length=50)  # Field name made lowercase.
    qtéutilisée = models.CharField(db_column='QteUtilise', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    id_bénévole = models.CharField(db_column='ID_Bénévole', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'allouer'
        unique_together = (('id_matériel', 'id_triathlon'),)

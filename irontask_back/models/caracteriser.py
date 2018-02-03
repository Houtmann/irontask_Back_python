from django.db import models


class Caracteriser(models.Model):
    id_triathlon = models.CharField(db_column='Id_Triathlon', primary_key=True,
                                    max_length=50)  # Field name made lowercase.
    id_catégorie = models.CharField(db_column='Id_Catégorie', max_length=50)  # Field name made lowercase.
    nbparticipant = models.CharField(db_column='NbParticipant', max_length=50, blank=True,
                                     null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'caracteriser'
        unique_together = (('id_triathlon', 'id_catégorie'),)

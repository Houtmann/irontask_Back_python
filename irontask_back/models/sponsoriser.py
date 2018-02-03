from django.db import models


class Sponsoriser(models.Model):
    id_triathlon = models.CharField(db_column='Id_Triathlon', primary_key=True,
                                    max_length=50)  # Field name made lowercase.
    siret = models.CharField(db_column='SIRET', max_length=50)  # Field name made lowercase.
    donation = models.IntegerField(db_column='Donation', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sponsoriser'
        unique_together = (('id_triathlon', 'siret'),)

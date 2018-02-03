from django.db import models


class Affecter(models.Model):
    benevole_id_bénévole = models.ForeignKey('Benevole', models.DO_NOTHING,
                                             db_column='benevole_ID_Bénévole',
                                             primary_key=True)  # Field name made lowercase.
    tache_id_triathlon = models.ForeignKey('Tache', models.DO_NOTHING,
                                           db_column='tache_Id_Triathlon')  # Field name made lowercase.
    tache_id_tachemodèle = models.ForeignKey('Tache', models.DO_NOTHING,
                                             db_column='tache_Id_TacheModèle')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'affecter'
        unique_together = (('benevole_id_bénévole', 'tache_id_triathlon', 'tache_id_tachemodèle'),)

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Benevole(models.Model):
    SEXE = (
        ('H', 'Homme'),
        ('F', 'Femme'),

    )
    id = models.AutoField(primary_key=True)

    nom = models.CharField(max_length=50)

    prenom = models.CharField(max_length=50)

    dateNaissance = models.DateField

    sexe = models.CharField(max_length=1, choices=SEXE)

    adresse = models.CharField(max_length=50)

    codePostal = models.CharField(max_length=5)

    ville = models.CharField(max_length=50)

    telephoneFixe = models.CharField(max_length=10)

    telephonePortable = models.CharField(max_length=10)

    email = models.EmailField



class TypeTriathlon(models.Model):
    id = models.AutoField(primary_key=True)

    libelle = models.CharField(max_length=50, null=False, blank=False)

    distanceNatation = models.IntegerField(max_length=2, null=False, blank=False)

    distanceCyclisme = models.IntegerField(max_length=4, null=False, blank=False)

    distanceCoursePied = models.IntegerField(max_length=4, null=False, blank=False)


class Triathlon(models.Model):
    id = models.AutoField(primary_key=True)

    date = models.DateField(null=False, blank=False)

    heureDepart = models.TimeField(null=False, blank=False)

    codePostal = models.CharField(max_length=5, null=False, blank=False)

    adresse = models.CharField(max_length=50, null=False, blank=False)

    ville = models.CharField(max_length=50, null=False, blank=False)
    typeTriathlon = models.ForeignKey(TypeTriathlon, on_delete=models.CASCADE)


class Tache(models.Model):
    triathlon = models.ForeignKey(Triathlon, on_delete=models.CASCADE)
    creer_par = models.ForeignKey(User, on_delete=models.CASCADE)
    dateFin = models.DateField(null=False, blank=False)

    duree = models.TimeField(null=False, blank=False)
    nbJoursRappel = models.IntegerField(null=False, blank=False)
    tacheValider = models.BooleanField(null=False, blank=False)
    benevole = models.ForeignKey(Benevole, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('triathlon', 'typeTache'),)


class Sponsor(models.Model):
    siret = models.BigIntegerField(primary_key=True)

    raisonSocial = models.CharField(max_length=50)

    adresse = models.CharField(max_length=50, null=False, blank=False)

    codePostal = models.CharField(max_length=5, null=False, blank=False)

    ville = models.CharField(max_length=50, null=False, blank=False)

    telephone = models.CharField(max_length=10, null=False, blank=False)

    email = models.CharField(max_length=50, null=False, blank=False)


class Sponsoriser(models.Model):
    id_triathlon = models.ForeignKey('Triathlon',
                                     db_column='ID_triathlon',
                                     primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.
    siret = models.ForeignKey(Sponsor, db_column='SIRET', max_length=50, primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.
    donation = models.IntegerField(db_column='Donation', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sponsoriser'
        unique_together = (('ID_triathlon', 'siret'),)


class Materiel(models.Model):
    id_Matériel = models.AutoField(primary_key=True)

    nom = models.CharField(max_length=50, null=False, blank=False)

    type = models.CharField(max_length=50)

    qteTotal = models.IntegerField(null=False, blank=False)

    lieuStockage = models.CharField(max_length=50, null=False, blank=False)


class Intervenant(models.Model):
    siret = models.BigIntegerField(primary_key=True)

    raisonSocial = models.CharField(max_length=50)



    adresse = models.CharField(max_length=50)

    codePostal = models.CharField(max_length=5)

    ville = models.CharField(max_length=50)

    telephoneFixe = models.CharField(max_length=10)

    telephonePortable = models.CharField(max_length=10)

    email = models.EmailField


class Catgorie(models.Model):
    id_catégorie = models.AutoField(primary_key=True)  # Field name made lowercase.
    libellé = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    agemin = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    agemax = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    sexe = models.IntegerField(blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'catégorie'


class Caracteriser(models.Model):
    id_triathlon = models.CharField(primary_key=True, max_length=50)  # Field name made lowercase.
    id_catégorie = models.CharField( max_length=50)  # Field name made lowercase.
    nbparticipant = models.CharField(max_length=50, blank=True,
                                     null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'caracteriser'
        unique_together = (('id_triathlon', 'id_catégorie'),)




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


class Affecter(models.Model):
    benevole = models.ForeignKey('Benevole', models.DO_NOTHING,
                                 db_column='benevole_ID_Bénévole',
                                 primary_key=True)  # Field name made lowercase.
    tache = models.ForeignKey('Tache', models.DO_NOTHING,
                              db_column='tache_Id_Triathlon')  # Field name made lowercase.
    tachemodèle = models.ForeignKey('Tache', models.DO_NOTHING,
                                    db_column='tache_Id_TacheModèle')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'affecter'
        unique_together = (('benevole_id_bénévole', 'tache_id_triathlon', 'tache_id_tachemodèle'),)

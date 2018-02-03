from django.db import models


class TypeTriathlon(models.Model):
    id = models.AutoField(primary_key=True)

    libelle = models.CharField(max_length=50)

    distanceNatation = models.IntegerField(max_length=2)

    distanceCyclisme = models.IntegerField(max_length=4)

    distanceCoursePied = models.IntegerField(max_length=4)


class Triathlon(models.Model):
    id = models.AutoField(primary_key=True)

    date = models.DateField
    heureDepart = models.TimeField

    codePostal = models.CharField(max_length=5)

    adresse = models.CharField(max_length=50)

    ville = models.CharField(max_length=50)
    typeTriathlon = models.ForeignKey(TypeTriathlon)


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


class Sponsor(models.Model):
    siret = models.BigIntegerField(primary_key=True)

    raisonSocial = models.CharField(max_length=50)

    adresse = models.CharField(max_length=50)

    codePostal = models.CharField(max_length=5)

    ville = models.CharField(max_length=50)

    telephone = models.CharField(max_length=10)

    email = models.CharField(max_length=50)


class Sponsoriser(models.Model):
    id_triathlon = models.ForeignKey('Triathlon', models.DO_NOTHING,
                                     db_column='ID_triathlon',
                                     primary_key=True)  # Field name made lowercase.
    siret = models.ForeignKey(Sponsor, db_column='SIRET', max_length=50, primary_key=True)  # Field name made lowercase.
    donation = models.IntegerField(db_column='Donation', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sponsoriser'
        unique_together = (('ID_triathlon', 'siret'),)


class Materiel(models.Model):
    id_Matériel = models.AutoField(primary_key=True)

    nom = models.CharField(max_length=50)

    type = models.CharField(max_length=50)

    qteTotal = models.IntegerField

    lieuStockage = models.CharField(max_length=50)


class Intervenant(models.Model):
    siret = models.BigIntegerField(primary_key=True)

    raisonSocial = models.CharField(max_length=50)

    type = models.ForeignKey()

    adresse = models.CharField(max_length=50)

    codePostal = models.CharField(max_length=5)

    ville = models.CharField(max_length=50)

    telephoneFixe = models.CharField(max_length=10)

    telephonePortable = models.CharField(max_length=10)

    email = models.EmailField


class Catgorie(models.Model):
    id_catégorie = models.AutoField(db_column='Id_Catégorie', primary_key=True)  # Field name made lowercase.
    libellé = models.CharField(db_column='Libellé', max_length=50, blank=True, null=True)  # Field name made lowercase.
    agemin = models.IntegerField(db_column='AgeMin', blank=True, null=True)  # Field name made lowercase.
    agemax = models.IntegerField(db_column='AgeMax', blank=True, null=True)  # Field name made lowercase.
    sexe = models.IntegerField(db_column='Sexe', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'catégorie'


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

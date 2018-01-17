from django.db import models
from ..models import triathlon

class Tache(models.Model):
    
    triathlon = models.ForeignKey(triathlon)
    typeTache = models.ForeignKey(typeTache)

   PRIMARY KEY(Id_Triathlon, Id_TypeTache),
   DateFin DATE,
   Durée SMALLINT,
   NbJoursRappel SMALLINT,
   TacheValidée LOGICAL,
   ID_Bénévole INT REFERENCES Benevole(ID_Bénévole) NOT NULL
from django.contrib.auth.models import User
from ..models import Benevole
from rest_framework import serializers

class BenevoleSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Benevole
        fields = ('id', 'nom', 'prenom', 'sexe', 'adresse', 'codePostal', 'ville', 'telephoneFixe', 'telephonePortable')



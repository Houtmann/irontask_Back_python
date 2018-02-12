from django.test import TestCase
from irontask_back.models import Triathlon, TypeTriathlon
from django.test import Client


class test_TriathlonCase(TestCase):
    c = Client()

    def setUp(self):
        tt = TypeTriathlon(libelle = 'Type 1', distanceNatation = 3000,
                           distanceCyclisme = 102, distanceCoursePied =48 )
        tt.save()

        Triathlon.objects.create(date = '2018-06-18', heureDepart = '10:00:00' ,codePostal = "88200",
                                 adresse = '5 rue de toulouse' , ville = 'toulouse', typeTriathlon = tt).save()



    def test__str__(self):
        t = Triathlon.objects.all()
        print(t.__str__())


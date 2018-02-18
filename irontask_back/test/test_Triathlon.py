from django.test import TestCase
from irontask_back.models import Triathlon, TypeTriathlon
from django.test import Client


class test_TriathlonCase(TestCase):


    def setUp(self):
        tt = TypeTriathlon(libelle='Type 1', distanceNatation=3000,
                       distanceCyclisme=102, distanceCoursePied=48)
        tt.save()
        Triathlon.objects.create(date='2018-06-18', heureDepart='10:00:00', codePostal="88200",
                             adresse='5 rue de toulouse', ville='toulouse', typeTriathlon=tt).save()



    def test__str__(self):
        t = Triathlon.objects.get(pk=1)
        self.assertEqual(t.__str__(), "Triathlon du 2018-06-18 à Toulouse")


    def test_formatVille(self):
            v = 'toulouse'
            self.assertEqual(Triathlon.formatVille(v), 'Toulouse')

    """def test_save(self):
        Triathlon.objects.create(date='2019-06-18', heureDepart='11:00:00', codePostal="88200",
                                 adresse='5 rue de toulouse', ville='toulouse', typeTriathlon=self.tt).save()
        triathlon2 = Triathlon.objects.get(date='2019-06-18')
        self.assertEqual(triathlon2.is_cool, True)"""
from django.test import TestCase
from irontask_back.models import Benevole
from django.test import Client


class test_BenevoleCase(TestCase):
    c = Client()

    def setUp(self):

        Benevole.objects.create(nom='HOUTMANN', prenom='hadrien', sexe='F'
                                , adresse="coucou", codePostal='88200', ville='remiremont',
                                telephoneFixe='0601403635', telephonePortable='0601403635')
        self.b = Benevole.objects.get(nom='HOUTMANN')


    def test__str__(self):
        print("test 3")
        b = Benevole.objects.get(nom='HOUTMANN')
        self.assertEqual(b.__str__(), 'HOUTMANN hadrien')

    def test_Attribut(self):
        print("test 4")
        self.assertEqual(self.b.nom, 'HOUTMANN')
        self.assertEqual(self.b.adresse, 'coucou')
        self.assertEqual(self.b.prenom, 'hadrien')
        self.assertEqual(self.b.codePostal, '88200')
        self.assertEqual(self.b.ville, 'remiremont')
        self.assertEqual(self.b.telephoneFixe, '0601403635')
        self.assertEqual(self.b.telephonePortable, '0601403635')
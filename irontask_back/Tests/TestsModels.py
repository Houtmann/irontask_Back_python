from django.test import TestCase
from irontask_back.models import Benevole
from django.test import Client


class TestBenevoleCase(TestCase):
    def setUp(self):
        Benevole.objects.create(nom='HOUTMANN', prenom='hadrien', sexe = 'F'
                                , adresse="coucou", codePostal='88200', ville='remiremont',
                                telephoneFixe = '0601403635', telephonePortable = '0601403635')
        b = Benevole.objects.get(nom='HOUTMANN')


    def testAttribut(self):
        """Animals that can speak are correctly identified"""

        b = Benevole.objects.get(nom='HOUTMANN')
        self.assertEqual(b.adresse, 'coucou')

    def testGetStr(self):
        b = Benevole.objects.get(nom='HOUTMANN')
        self.assertEqual(b.__str__(), 'HOUTMANN hadrien')

    def testApiReponse(self):
        c = Client()
        r = c.get('/benevole/')
        self.assertEqual(r.status_code, 200)


class TestAdminPanel(TestCase):
    def testAdminReponse(self):
        c = Client()
        r = c.get('/admin/')
        self.assertEqual(r.status_code, 302)
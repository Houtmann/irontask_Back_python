from django.test import TestCase
from ..models import Benevole
from django.test import Client


class test_BenevoleCase(TestCase):
    c = Client()

    def setUp(self):
        Benevole.objects.create(nom='HOUTMANN', prenom='hadrien', sexe = 'F'
                                ,adresse="coucou", codePostal='88200', ville='remiremont',
                                telephoneFixe = '0601403635', telephonePortable = '0601403635')
        self.b = Benevole.objects.get(nom='HOUTMANN')


    def test_Attribut(self):
        self.assertEqual(self.b.nom, 'HOUTMANN')
        self.assertEqual(self.b.adresse, 'coucou')
        self.assertEqual(self.b.prenom, 'hadrien')
        self.assertEqual(self.b.codePostal, '88200')
        self.assertEqual(self.b.ville, 'remiremont')
        self.assertEqual(self.b.telephoneFixe, '0601403635')
        self.assertEqual(self.b.telephonePortable, '0601403635')


    def __str__(self):
        b = Benevole.objects.get(nom='HOUTMANN')
        self.assertEqual(b.__str__(), 'HOUTMANN hadrien')


    def test_GetBenevoleIdReponse(self):
        r = self.c.get('/benevole/1/')
        self.assertEqual(r.status_code, 200)

    def test_GetBenevoleIdJSONReposne(self):
        r = self.c.get('/benevole/1/')
        self.assertEqual(r.content,
                         b'{"id":1,"nom":"HOUTMANN","prenom":"hadrien",'
                         b'"sexe":"F","adresse":"coucou","codePostal":"88200",'
                         b'"ville":"remiremont","telephoneFixe":"0601403635",'
                         b'"telephonePortable":"0601403635"}')

    def test_ApiReponse(self):

        r = self.c.get('/benevole/')
        self.assertEqual(r.status_code, 200)

    def testApiJSONReponse(self):
        r = self.c.get('/benevole/')
        self.assertEqual(r.content,
                         b'[{"id":1,"nom":"HOUTMANN","prenom":"hadrien",'
                         b'"sexe":"F","adresse":"coucou","codePostal":"88200",'
                         b'"ville":"remiremont","telephoneFixe":"0601403635",'
                         b'"telephonePortable":"0601403635"}]')









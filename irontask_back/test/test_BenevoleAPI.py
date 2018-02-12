from django.test import TestCase
from irontask_back.models import Benevole
from django.test import Client


class test_BenevoleAPICase(TestCase):
    c = Client()

    def setUp(self):
        Benevole.objects.create(nom='HOUTMANN', prenom='hadrien', sexe='F'
                                , adresse="coucou", codePostal='88200', ville='remiremont',
                                telephoneFixe='0601403635', telephonePortable='0601403635')
        self.b = Benevole.objects.get(nom='HOUTMANN')



    def test_GetBenevoleIdReponse(self):
        print("test 5")
        r = self.c.get('/benevole/1/')
        self.assertEqual(r.status_code, 200)

    def test_GetBenevoleIdJSONReposne(self):
        print("test 6")
        r = self.c.get('/benevole/1/')
        self.assertEqual(r.content,
                         b'{"id":1,"nom":"HOUTMANN","prenom":"hadrien",'
                         b'"sexe":"F","adresse":"coucou","codePostal":"88200",'
                         b'"ville":"remiremont","telephoneFixe":"0601403635",'
                         b'"telephonePortable":"0601403635"}')

    def test_ApiReponse(self):
        print("test 8")
        r = self.c.get('/benevole/')
        self.assertEqual(r.status_code, 200)

    def testApiJSONReponse(self):
        print("test 9")
        r = self.c.get('/benevole/')
        self.assertEqual(r.content,
                         b'[{"id":1,"nom":"HOUTMANN","prenom":"hadrien",'
                         b'"sexe":"F","adresse":"coucou","codePostal":"88200",'
                         b'"ville":"remiremont","telephoneFixe":"0601403635",'
                         b'"telephonePortable":"0601403635"}]')

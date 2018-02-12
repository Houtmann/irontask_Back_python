from django.test import TestCase
from django.test import Client

class TestAdminPanel(TestCase):
    c = Client()

    def testAdminReponseNotAuthenticated(self):
        print("test 1")
        r = self.c.get('/admin/')
        self.assertEqual(r.status_code, 302)



import django
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import HabitsListView, index, HabitsListSetup, HabitsCreateView, HabitsUpdateView, HabitsDeleteView
from django.contrib.auth.models import User

class TestUrls(SimpleTestCase):

    def test_list_of_urls(self):
        index = self.client.get('/')
        self.assertEqual(index.status_code, 200)


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_authenticated)




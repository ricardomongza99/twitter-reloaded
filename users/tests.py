from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserRegistrationCase(TestCase):
    def test_registration(self):

    #create a test user
        username = 'testuser'
        password = 'testpassword'
        email = 'testuser@example.com'

        User.objects.create_user(username=username, password=password, email=email)

    # Retrieve the user from the database
        user = User.objects.get(username=username)

    # Assert that the user exists in the database
        self.assertIsNotNone(user)

        pass

class UserLoginTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_correct_credentials(self):
        user = authenticate(username=self.username, password=self.password)
        self.assertIsNotNone(user)
        self.assertEqual(user, self.user)

    def test_incorrect_credentials(self):
        user = authenticate(username=self.username, password='wrongpassword')
        self.assertIsNone(user)
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test to create a user with email"""
        email = "hammadarshad834@gmail.com"
        password = "TestPass123"
        user = User.objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'hammad@HASHINGDEV.COM'
        user = User.objects.create_user(email, 'TestPass')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            User.objects.create_user(None, 'TestPass')

    def test_new_super_user(self):
        """Test to create a new super user"""
        user = User.objects.create_superuser(
            'hammad@GITHUB.com',
            'testPass'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

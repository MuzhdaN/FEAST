from django.test import TestCase
from django.conf import settings
import os


class djnagoTest(TestCase):
    def test_strength_secret_key(self):
        settings.SECRET_KEY
        SECRET_KEY = os.environ.get('SECRET_KEY')
        self.assertNotEqual(SECRET_KEY, 'my_super^secret@key')

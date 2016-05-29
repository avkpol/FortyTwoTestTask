from django.test import TestCase
from . models import UserData




class UserDataView(TestCase):

    """Test functions from util module"""
    def setUp(self): # create user
        user, created = UserData.objects.get_or_create(
            id=1,
            name="Andriy")

    def test_user_data_view(self):


        name = UserData.objects.get(id=1)
        self.assertTrue(name, 'Andriy')



from django.test import TestCase
from . models import User_data




class UserDataView(TestCase):

    """Test functions from util module"""
    def setUp(self): # create user
        user, created = User_data.objects.get_or_create(
            id=1,
            name="Andriy")

    def test_user_data_view(self):


        name = User_data.objects.get(id=1)
        self.assertTrue(name, 'Andriy')



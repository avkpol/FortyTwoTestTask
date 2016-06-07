from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from models import UserData, RequestLog, ModelLog


class UserDataTestCase(TestCase):

    """Check whether user data are proper
    """
    fixtures = ['init_data.json']

    def setUp(self):

        self.url = reverse('avkpol4:home')

    def test_create_new_profile(self):
        self.requests = RequestLog.objects.all()
        self.all_users = UserData.objects.all()
        self.one_user = self.all_users[0]
        self.assertEquals(
            self.one_user.name,
            "Andriy"
        )
        self.assertEquals(
            self.one_user.last_name,
            "Kravchenko"
        )

    def test_template(self):

        """ Check  template
        """
        response = self.client.get(self.url)
        # check we've used the right template
        self.assertTemplateUsed(response, 'home.html')

    def test_view(self):

        """ Response code should be 200
        """
        response = self.client.get(self.url)
        # check page status code
        self.assertEqual(response.status_code, 200)


class UserEditTestCase(TestCase):

    def setUp(self):

        """create admin user
        """

        self.form_url = reverse('avkpol4:user_edit')

        # crete super user
        self.user = 'k'
        self.password = '123'
        self.email = 'qq@qq.qq'
        UserData.objects.all().delete()
        admin = User.objects.create_superuser(self.user, self.email, self.password)
        admin.save()

    def test_admin_login(self):

        """ Check if admin user able to log-in
        """

        self.assertEqual(Client().login(username=self.user, password=self.password), True)

class HttpRequestsTestCase(TestCase):

    """Check requests
    """

    def setUp(self):

        self.url = reverse('avkpol4:home')

    fixtures = ['init_data.json']
    def test_create_new_http_request(self):
        all_requests = RequestLog.objects.all().count()
        one_request = RequestLog.objects.all()[0]
        self.assertEquals(len(RequestLog.objects.all()), all_requests)

        self.assertEquals(
            one_request.status,
           1
        )
        self.assertEquals(
            one_request.requested_url,
           'http://127.0.0.1:8000' + self.url
        )

    def test_home_url_http_request(self):
        response = self.client.get(reverse('avkpol4:home'))
        self.assertEqual(response.status_code, 200)


class SignalTestCase(TestCase):

    fixtures = ['init_data.json']

    def test_signal_on_create(self):

        """ Check sending signal work on object creation event
        """
        obj = UserData.objects.create(name="Bruce")
        count = ModelLog.objects.all().count()
        obj.save()
        new_count = ModelLog.objects.all().count()
        self.assertEqual(count + 1, new_count)


    def test_signal_on_delete(self):

        """ Check if signals work on object deletion  event
        """
        usr = UserData.objects.first()
        count = ModelLog.objects.all().count()
        usr.delete()
        new_count = ModelLog.objects.all().count()
        self.assertEqual(count + 1, new_count)

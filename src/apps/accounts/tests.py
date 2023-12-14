"""
https://docs.djangoproject.com/en/4.0/topics/testing/tools.html

Run the test as follows:
manage.py test accounts.tests
"""


from django.test import Client, TestCase


class AccountTestCase(TestCase):
    
    fixtures = ['accounts.json',]

    def setUp(self):
        
        # Every test needs a client.
        self.client = Client(HTTP_USER_AGENT='Mozilla/5.0')

    def test_account_detail(self):
        
        # Issue a GET request.
        response = self.client.get('/account/3/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

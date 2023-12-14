"""
https://docs.djangoproject.com/en/4.0/topics/testing/tools.html

Run the test as follows:
manage.py test gatepasses.tests
"""


from django.test import Client, TestCase


class GatepassTestCase(TestCase):
    
    fixtures = ['gatepasses.json',]

    def setUp(self):
        
        # Every test needs a client.
        self.client = Client(HTTP_USER_AGENT='Mozilla/5.0')

    def test_gatepass_detail(self):
        
        # Issue a GET request.
        response = self.client.get('/gatepass/3/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

"""
https://docs.djangoproject.com/en/4.0/topics/testing/tools.html

Run the test as follows:
python manage.py test apps.assets.tests
"""


from django.test import Client, TestCase


class AssetTestCase(TestCase):
    
    fixtures = ['assets.json',]

    def setUp(self):
        
        # Every test needs a client.
        self.client = Client(HTTP_USER_AGENT='Mozilla/5.0')

    def test_asset_detail(self):
        
        # Issue a GET request.
        response = self.client.get('/asset/3/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

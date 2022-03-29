from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


# Create your tests here.
class TestApi(APITestCase):
    def test_api_post(self):
        data = {'name': 'name Sample'}
        response = self.client.post(reverse('name'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_get(self):
        response = self.client.get(reverse('view'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

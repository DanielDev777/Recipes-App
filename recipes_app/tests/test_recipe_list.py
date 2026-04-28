from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class RecipeListHappyTestCase(APITestCase):
    """Happy path tests for /recipes-list/ endpoint"""

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.url = reverse('recipe-list')
    
    def test_get_recipes_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_post_recipe(self):
        data = {
            'title': 'Authenticated Recipe',
            'description': 'Created by authenticated user',
            'author': self.user.id
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class RecipeListUnhappyTestCase(APITestCase):
    """Unhappy path tests for /recipes-list/ endpoint"""

    def setUp(self):
        self.url = reverse('recipe-list')

    def test_get_recipes_list_without_auth(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_post_recipe_without_auth(self):
        data = {
            'title': 'Test Recipe',
            'description': 'A test recipe description',
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
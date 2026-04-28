from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class RecipeListHappyTestCase(APITestCase):
    """Happy path tests for /recipes-list/ endpoint"""
    
    def test_get_recipes_list(self):
        url = reverse('recipe-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class RecipeListUnhappyTestCase(APITestCase):
    """Unhappy path tests for /recipes-list/ endpoint"""
    
    def test_post_recipe_without_auth(self):
        url = reverse('recipe-list')
        data = {
            'title': 'Test Recipe',
            'description': 'A test recipe description',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
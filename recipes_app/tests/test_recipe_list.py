from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class RecipeListTests(APITestCase):

    def setUp(self):
        self.url = reverse('recipe-list')
    
    def test_get_recipes_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_recipe_creates_recipe(self):
        user = User.objects.create_user(username='testuser', password='testpass123')
        
        data = {
            'title': 'Test Recipe',
            'description': 'A test recipe description',
            'author': user.id
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
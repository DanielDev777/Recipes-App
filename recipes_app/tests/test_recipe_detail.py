from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from recipes_app.models import Recipe

class RecipeDetailHappyTestCase(APITestCase):
    """Happy path tests for /recipes-detail/<id>/ endpoint"""
    
    def test_get_recipe_detail_with_auth(self):
        user = User.objects.create_user(username='detailuser', password='testpass123')
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        
        recipe = Recipe.objects.create(
            title='Detail Recipe',
            description='Recipe for detail test',
            author=user
        )
        
        url = reverse('recipe-detail', kwargs={'pk': recipe.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
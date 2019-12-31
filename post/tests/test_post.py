from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from post.models import Post


class TestPostCreate(APITestCase):
    def setUp(self):
        self.posts = Post.objects.all()

    def test_criar_post(self):
        """
            Teste para garantir a criação de um novo post.
        """
        total_post = self.posts.count()
        url = reverse('post-list')
        data = {
            "titulo": "Testando",
            "descricao": "teste",
            "conteudo": "teste"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(self.posts.count(), total_post + 1)

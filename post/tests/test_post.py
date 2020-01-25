from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from post.models import (Post, Tag, PostTag)


class TestPostCreate(APITestCase):
    def setUp(self):
        self.posts = Post.objects.all()
        self.tag = Tag.objects.all()
        self.post_tag = PostTag.objects.all()

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

    def test_criar_post_repetido(self):
        """
            Testando a criação de um post com titulo já
            existente.

            O teste deve falhar.

            título -> unique
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
        response = self.client.post(url, data, format='json')
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        self.assertEqual(self.posts.count(), total_post + 1)
        self.posts.filter(
            titulo='Testando'
        ).delete()

    def test_titulo_mais_cem(self):
        """
            Teste para verificar a criação de post com
            titulo com mais de 100 carácteres.

            O teste deve falhar.
        """
        url = reverse('post-list')
        data = {
            "titulo": "1pvpiwvT25SZ9zV0T2RvX4S33iFSy8BLIG6i2TitNbjNW3CO9MYZcsp6OhyKcIGpIO4BqdbNjlVYTIHoE19MEMBshgwBUYaWsjpVm",
            "descricao": "teste",
            "conteudo": "teste"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_descricao_mais_trezentos(self):
        """
            Teste para verificar a criação de post com
            descricao com mais de 300 carácteres.

            O teste deve falhar.
        """
        url = reverse('post-list')
        data = {
            "titulo": "Testando",
            "descricao": "lMVJHgkXvCBPSTQqV5sAThTUtmeJNO9RQxosF8T974OirxW1boAHNw4TwYqRX4Ck7MEVshGznvYPpGrC4nObdcA2HzKew4ETVE0jxAiI3YhtOch6X9Dn3VDw6Zp2taedHsa7tYLGzobBwWi7EtoBAt1SddVZs0FodVP0uFrXsue13rbXqnvFScpYroRphsiLZ5cWShiEcLXtl47jAT2SigHYcRZTUj17ZRCe4aZAWpz38cVFf6KJfW51PCnGlC3Q20iMUhzMRLO8IFQx99eJMl7sRh3NaWR9xiPvG5hLku3NC",
            "conteudo": "teste"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_conteudo_mais_mil(self):
        """
            Teste para verificar a criação de post com
            conteudo com mais de 1000 carácteres.

            O teste deve falhar.
        """
        url = reverse('post-list')
        data = {
            "titulo": "Testando",
            "descricao": "teste",
            "conteudo": "06ey8MFdFaaRkFcinkKErLw6nbtvYWJ8QoRhw3YAhhbNmr7sHbYbo5WYicgndmqNhdtBQ7ZEUwPne4w9YjU17nwr187JQufrRhzlkpqKHxJzDlOkHpSA02GAy6CynjZrOI8CTQdfIXKjmF3oOqGCek9xxfffzJMKzAT46iHzr9KGnir5JutaXx0lCve21YCYPvucTwcpesnsw1gDxmimlle0cPbxTv9Ydr2MMcNy6O67L9s5aSKyMjDGfv6Z9zgvYUDMevtnJ8WWb0wQ1iMQAQ3CZWIRelyp8OiMNXUUy9TPj51kNIyodjSc9pNFrIWFbYHHQ2GB4kOn9IKQvBtwOVK7GICW7M3wCyYPpo6u9IUdjGbjb6mMubKLxKygvFSGyTPljKgaZNs3jttGmQu0uBDsWABEtXaEhbb4QLQ9Qd3fFEF3XFbm9mTUlvUYPCUxSB7YpgzCSsbf2IkScmsL5ENhFNemalmTpBC9jMAM6kTAsdBusr4nmgwZm0vVajQhwuF9pPxI8bns2i0D4ftLFWTY28a12LMoSb2aZ5iJyqCYjZgLEb1aUfPgmSPJFvs3QlcIJPUr39o8dC0sRU4ySxrTnz7MIJJFNolqbaom6YsIEwqswdAZUqM0yu7DGYAFKCMjZrqhmS52rGbI7bXYEeCopUyC24XiiOtPZnTTRaGkvZt25fRxZckxIVJlkuErNJk1fC7yMyK5atjDb5Bn1m7kkKLasIK4R2mQtgBKUuuZ2cQIfFDw1XpUPCHPPQFa2ILI1cXRGfIggV0tjydlxyXYqT68kfRkqnkgx3T2RvMNluFM0qH0pscrbeTxMgKAnt03dmdXFsnPs85fKuvZesybcYS8yT92VwT30lYZrqpZFt9swbt7VCOX6vSMSupzg5YcquEpzdg9fv4pDytVuikPkCCPnHPtuBPE8leWhTxBhyoOqjlPzKHirxvoo1B8yTvgn8ieiUPdVYog1bXxLBewY5sokcVpJyWvGbxy2"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_post_com_tag(self):
        """
            Testa a criação de posts com tags.
        """
        total_post = self.posts.count()
        url = reverse('post-list')
        data = {
            "titulo": "test post",
            "descricao": "teste",
            "conteudo": "teste",
            "tags": [
                {
                    "nome": "first tag"
                },
                {
                    "nome": "second tag"
                }
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(self.posts.count(), total_post + 1)

    def test_post_com_tag_existente(self):
        """"
            Testando a criação de post com tag existente.
            Caso a tag passada já exista, a aplicação deve utilizar
            as tags já existentes para o post criado.
        """

        total_post = self.posts.count()

        url = reverse('post-list')
        data = {
            "titulo": "Post Tag",
            "descricao": "teste",
            "conteudo": "teste",
            "tags": [
                {
                    "nome": "first tag"
                },
                {
                    "nome": "second tag"
                }
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(self.posts.count(), total_post + 1)

        total_post = self.posts.count()
        total_tag = self.tag.count()
        total_post_tag = self.post_tag.count()

        data = {
            "titulo": "Post Tag existente",
            "descricao": "teste",
            "conteudo": "teste",
            "tags": [
                {
                    "nome": "first tag"
                },
                {
                    "nome": "second tag"
                }
            ]
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(self.posts.count(), total_post + 1)
        self.assertEqual(self.tag.count(), total_tag)
        self.assertEqual(self.post_tag.count(), total_post_tag + 2)

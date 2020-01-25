from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

from post.serializers import PostSerializer


class PostViewSet(GenericViewSet, CreateModelMixin):
    """
        View simples para crud de posts
    """
    serializer_class = PostSerializer

    def create(self, request):
        return super(PostViewSet, self).create(request)

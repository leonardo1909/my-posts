from rest_framework.viewsets import ModelViewSet

from post.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    """
        View simples para crud de posts
    """
    serializer_class = PostSerializer

    def create(self, request):
        return super(PostViewSet, self).create(request)

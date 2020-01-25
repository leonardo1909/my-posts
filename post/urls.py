from django.urls import include, path
from rest_framework_nested import routers

from post.viewsets import PostViewSet

router = routers.DefaultRouter()

router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
]

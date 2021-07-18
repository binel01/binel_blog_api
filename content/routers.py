from rest_framework import routers
from .viewsets import CategoryViewSet, PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

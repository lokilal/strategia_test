from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet

router_v1 = DefaultRouter()

router_v1.register('posts', PostViewSet)
router_v1.register(r'posts/(?P<post_id>[^/.]+)/comments',
                   CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router_v1.urls))
]

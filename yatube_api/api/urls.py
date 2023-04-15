from rest_framework import routers

from django.urls import include, path

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('groups', GroupViewSet, basename='group')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comment'
                )
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]

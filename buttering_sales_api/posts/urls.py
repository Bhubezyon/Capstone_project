from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from django.urls import path
from .views_user import RegisterView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('api', include(router.urls)),
    path('api/', include('posts.urls')),
    path('register/', RegisterView.as_view(), name='register'),
]

urlpatterns += [
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like_post'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike_post'),
]
